import bisect

import abc


class Node(abc.ABC):

    def __init__(self, keys=None, parent=None):
        self.keys = keys or []
        self.parent = parent

    def __len__(self):
        return len(self.keys)

    def set_parent(self, parent):
        self.parent = parent

    def contains(self, key):
        return key in self.keys

    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_key(self, index, key):
        self.keys.insert(index, key)

    def split(self):
        if self.parent:
            return self._split_with_parent()
        return self._split_without_parent()

    @abc.abstractmethod
    def _split_without_parent(self):
        pass

    @abc.abstractmethod
    def _split_node(self):
        pass

    @abc.abstractmethod
    def _split_with_parent(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def is_leaf_node(self):
        pass
