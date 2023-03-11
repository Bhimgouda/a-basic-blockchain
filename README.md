This is a Simple representation of How blockchain would look in the terms of data structure, and the basic idea of how blockchain might look unde the hood

In this small project of creating a really basic blockchain we can understand
1. How each block is connected to it's previous block 
2. How the cryptographic hash is generated using the data, nonce, previous block's hash, which indeed gives it the immutability 

There a 2 files one is a js file and the other is py file but both have exact same functionality but in different languages, and they get us a basic blockchain with only 10 blocks.

Here is a basic data structure of a blockchain that we get from the javascript file


[  

    Block {
      data: '0',
      hash: '322b6723fac77c56446e99304b4a7b7edb1fd0857a0f2c452b5315f02a3022c1',   
      prevHash: '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    },
    Block {
      data: '1',
      hash: '6b85d12fcfe15bb76345eec13568daaf9f3891296e87840c613a5f822cb288e7',   
      prevHash: '322b6723fac77c56446e99304b4a7b7edb1fd0857a0f2c452b5315f02a3022c1'
    },
    Block {
      data: '2',
      hash: 'acf289fbf795dd6b290c1e3755b3869792ca84a94186f104c1391c85d5a5e98e',
      prevHash: '6b85d12fcfe15bb76345eec13568daaf9f3891296e87840c613a5f822cb288e7'
    },
    Block {
      data: '3',
      hash: 'f1aff577bed5a16282986b6de81eee3fa8e4ef4814b021d7c38c59f40974ca7a',
      prevHash: 'acf289fbf795dd6b290c1e3755b3869792ca84a94186f104c1391c85d5a5e98e'
    },
    Block {
      data: '4',
      hash: '7e57056d9274acad2de9b83ef0b313373870a78fc0f243806c362b742c8d14c0',
      prevHash: 'f1aff577bed5a16282986b6de81eee3fa8e4ef4814b021d7c38c59f40974ca7a'
    },
    Block {
      data: '5',
      hash: '3f94865d2491ccab7c4c372528ae1570cded61eb4b287763b9d7c3862ecba4e2',
      prevHash: '7e57056d9274acad2de9b83ef0b313373870a78fc0f243806c362b742c8d14c0'
    },
    Block {
      data: '6',
      hash: 'be955bda3cfeab7e41fc9fdc03ecf15b1a7d6c80be0b17576fa135e28249a32a',
      prevHash: '3f94865d2491ccab7c4c372528ae1570cded61eb4b287763b9d7c3862ecba4e2'
    },
    Block {
      data: '7',
      hash: 'b400501cabcf7761b809908ea1e7f610a65bb67fc94647cae5f5ae945f8bad88',
      prevHash: 'be955bda3cfeab7e41fc9fdc03ecf15b1a7d6c80be0b17576fa135e28249a32a'
    },
    Block {
      data: '8',
      hash: '288c7128dcb963856095077995751af72805ed24e93688ce530c82a4daf084a3',
      prevHash: 'b400501cabcf7761b809908ea1e7f610a65bb67fc94647cae5f5ae945f8bad88'
    },
    Block {
      data: '9',
      hash: '55de58b0ea4dd6f9573968e45bbd2ae9ad0dd301dfb3a5b09677627f899e7feb',
      prevHash: '288c7128dcb963856095077995751af72805ed24e93688ce530c82a4daf084a3'
    },
    Block {
      data: '10',
      hash: '428ea76d921ed3a330a8447e841df2fc2a87481331bb220f83271caaeda42bd7',
      prevHash: '55de58b0ea4dd6f9573968e45bbd2ae9ad0dd301dfb3a5b09677627f899e7feb'
    }
    
  ]
