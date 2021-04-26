import bisect


class Node:

    def __init__(self, keys=None, parent=None):
        self.keys = keys or []
        self.parent = parent

    def set_parent(self, parent):
        self.parent = parent

    def contains(self, key):
        return key in self.keys

    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_key(self, index, key):
        self.keys.insert(index, key)

    def is_leaf_node(self):
        pass

    def __len__(self):
        return len(self.keys)
