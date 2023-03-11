const { createHash } = require('crypto');

function hashGenerator(string) {
  return createHash('sha256').update(string).digest('hex');
}

class Block{
    constructor(data,prevHash){
        this.data = data;
        this.hash = hashGenerator(data+prevHash); // A combination of prev hash and block data gets us the current hash
        this.prevHash = prevHash;
    }
}

class Blockchain{
  constructor(genesisData){
    // Getting prevHash for genesis block
    const prevHash = hashGenerator(genesisData);

    const genesisBlock = new Block(genesisData, prevHash);
    console.log(genesisBlock)
    this.chain = [genesisBlock];
  }

  addBlock(data){
    const prevHash = this.chain[this.chain.length-1].hash;
    const block  = new Block(data, prevHash)
    this.chain.push(block)
  }
}

let bc = new Blockchain('0');

for(let i=1; i<11; i++){
  bc.addBlock(`${i}`);
}

for(let block of bc.chain){
  console.log(block)
}
