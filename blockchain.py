import hashlib

# To generate a hash from the given input
def hashGenerator(data):
        result=hashlib.sha256(data.encode())
        return result.hexdigest()

# Creating a block
class Block:
        def __init__(self, data, hash, prev_hash):
                self.data = data
                self.hash = hash
                self.prev_hash = prev_hash

# Creating the blockchain
class Blockchain:
    def __init__(self):
            # Genesis block random hash to start
            hashLast=hashGenerator('gen_last')
            hashStart=hashGenerator('gen_hash')

            # made a genesis block using Block class
            genesis=Block('gen-data', hashStart, hashLast)

            # Added it the array at position 0 (Now our array is the chain starting with this genesis block)
            self.chain=[genesis]

            # Adding a new block to the chain with the hash of previous block in the prev_hash field
    def add_block(self, data):
                    prev_hash=self.chain[-1].hash
                    hash=hashGenerator(data+prev_hash)
                    block=Block(data, hash, prev_hash)
                    self.chain.append(block)

# Adding random data to blockchain
bc=Blockchain()

# Adding 10 random blocks
for i in range(10):
        bc.add_block(str(i))

for block in bc.chain:
       print(block.__dict__)

                