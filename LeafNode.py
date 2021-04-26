import bisect
import Node
import InternalNode


class LeafNode(Node.Node):

    def __init__(self, keys=None, values=None, parent=None, next_node=None):
        super().__init__(keys, parent)
        self.values = values or []
        self.next_node = next_node

    def insert_entry(self, key, value):
        index = self.get_insert_index(key)
        self.insert_key(index, key)
        self.values.insert(index, value)
        return index

    def split(self):
        if self.parent:
            return self._split_with_parent()
        return self._split_without_parent()

    def _split_node(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]

        right_node = LeafNode(self.keys[split_index:], self.values[split_index:],
                              None, self.next_node)

        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]

        self.next_node = right_node
        right_node.parent = self.parent

        return key_to_move_up, right_node

    def _split_without_parent(self):
        key_to_move_up, right_node = self._split_node()
        parent_node = InternalNode.InternalNode([key_to_move_up],
                                                [self, right_node])

        self.parent, right_node.parent = parent_node, parent_node

        return parent_node

    def _split_with_parent(self):
        key_to_move_up, right_node = self._split_node()
        parent_node = self.parent

        index = parent_node.get_insert_index(key_to_move_up)

        parent_node.insert_key(index, key_to_move_up)
        parent_node.insert_child(index + 1, right_node)

        return parent_node

    @staticmethod
    def is_leaf_node():
        return True
