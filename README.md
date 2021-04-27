# KeyValueStore


## Description:
* A Key-Value store implemented from scratch using the B+ Tree Data structure in Python.
* We can access and update the key-value store using python dictionary like syntax.
* We can add new key-value pairs to it or update existing keys with new values in O(log N) time.
* We can iterate over all key-value pairs present in the data structure in O(N) time.
* We can perform range queries on the keys.
* We can fetch existing values for a key or check for the existence of a key using the "in" operator in O(log N) time.

## Artifacts
* Demonstration.ipynb: Jupyter notebook that tests and demonstrates the usage of the key-value store
* Node.py: Contains the abstract base class Node which is extented by the LeafNode and InternalNode classes.
* LeafNode.py: Contains the LeafNode class, which is used to model the leaf node of the B+ tree
* InterNode.py: Contains the InternalNode class, which is used to model the non-leaf internal nodes of the B+ Tree
* BPlusTree.py: Contains the BPlusTree class, which is used to construct, update and query the data structure

