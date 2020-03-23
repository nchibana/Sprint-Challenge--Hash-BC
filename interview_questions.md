## Explain in detail the workings of a dynamic array:

A dynamic array is different from a normal array in that its size can be dynamically modified when needed. With a normal array, a contiguous block of memory is assigned for its contents, so its size does not change
automatically when space runs out. With a dynamic array, a bigger space is allocated once the slots have been filled.

In order to do this, the dynamic array automatically allocates a bigger space, usually twice the size of the original, and copies over the elements of the original array one by one. This new array is now where the
new elements will be inserted into.

### What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
The runtime complexity to access an array is constant, O(1).
The runtime complexity to add or remove from the front is O(n) because all the rest of the elements would need to be shifted one space.
The runtime complexity to add or remove from the back is O(1) if it is a dynamic array. Otherwise, if there is no space, we would need to copy all elements every time it is full so it would be O(n).

### What is the worse case scenario if you try to extend the storage size of a dynamic array?
The runtime complexity in worst-case scenario is O(n).

## Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
A blockchain is structured in a way that is similar to a linked list. Each block has an index,
a timestamp, a proof, a list of transactions, and a hash of the previous block. Since each block contains a hash of the previous block, we say that they are linked in a chain. This means that if any previous block is changed, then the hashes for all subsequent ones would be incorrect and
therefore alert users that the chain has been compromised.

When you instantiate a blockchain, you begin with a genesis block, which has no predecessors.

## Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Proof of work is how new blocks are created in the blockchain. The goal is to find an arbitrarily
difficult problem to solve that is easy to check if it is correct. The proof of work algorithm
is what miners race to solve in order to win coins. This protects the chain from attack because it would take too much time and resources to not only find proof of work for one block, but for all previous blocks in order to alter the chain. For example, if a blockchain has 1000 blocks and we want to alter block 100 to give ourselves more money, then we'd have to make new blocks and make a longer chain because only the longest chain wins.