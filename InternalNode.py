import Node


class InternalNode(Node.Node):

    def __init__(self, keys=None, children=None, parent=None):
        super().__init__(keys, parent)
        self.children = children

    def insert_key(self, index, key):
        self.keys.insert(index, key)

    def insert_child(self, index, child):
        self.children.insert(index, child)

    def split(self):
        if self.parent:
            return self._split_with_parent()
        return self._split_without_parent()

    def _split_node(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]

        right_node = InternalNode(self.keys[split_index + 1:],
                                  self.children[split_index + 1:])

        for child in right_node.children:
            child.parent = right_node

        self.keys = self.keys[:split_index]
        self.children = self.children[:split_index + 1]
        right_node.parent = self.parent

        return key_to_move_up, right_node

    def _split_without_parent(self):
        key_to_move_up, right_node = self._split_node()

        parent_node = InternalNode([key_to_move_up], [self, right_node])

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
        return False


