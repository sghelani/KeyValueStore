import LeafNode
import bisect


class IterObject:
    def __init__(self, node=None, counter=0):
        self.node = node
        self.counter = counter


class BPlusTree:

    def __init__(self, split_threshold):
        self.root = None
        self.split_threshold = split_threshold
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size

    def _find_node(self, current_node, key):
        if current_node.is_leaf_node():
            return current_node

        index = current_node.get_insert_index(key)
        return self._find_node(current_node.children[index], key)

    def __contains__(self, key):
        node = self._find_node(self.root, key)
        if key in node.keys:
            return True
        return False

    def __getitem__(self, key):
        node = self._find_node(self.root, key)
        if key not in node.keys:
            raise KeyError(f"Key {key} does not exist")
        index = node.keys.index(key)
        return node.values[index]

    def __setitem__(self, key, value):
        if not self.root:
            self.root = LeafNode.LeafNode()

        node = self._find_node(self.root, key)
        if key in node.keys:
            self._replace(node, key, value)
        else:
            self._add(node, key, value)

    def __iter__(self):
        self.iter_object = IterObject(self._find_node(self.root, float("-inf")), -1)
        return self

    def __next__(self):
        cur_node, counter = self.iter_object.node, self.iter_object.counter

        counter += 1

        if counter >= len(cur_node):
            cur_node = cur_node.next_node
            counter = 0

        if not cur_node or not len(cur_node):
            raise StopIteration

        self.iter_object.node, self.iter_object.counter = cur_node, counter

        return cur_node.keys[counter], cur_node.values[counter]

    def range_query(self, key_low, key_up):

        node, counter = self._find_node(self.root, key_low), 0
        ret = []

        while node and node.keys[counter] <= key_up:

            if node.keys[counter] >= key_low:
                ret.append((node.keys[counter], node.values[counter]))
            counter += 1

            if counter >= len(node):
                node = node.next_node
                counter = 0

        return ret

    def _replace(self, node, key, value):
        index = node.keys.index(key)
        node.values[index] = value

    def _add(self, node, key, value):

        node.insert_entry(key, value)
        self.size += 1

        while len(node) > self.split_threshold:
            parent = node.split()
            if self.root == node:
                self.root = parent
                self.height += 1
            node = parent
