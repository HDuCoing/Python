
class BSTMap:
        def __init__(self):
                self._root = None
                self._size = 0


        def add(self, key, value):
                node = self._bstSearch(self._root, key)
                if node is not None:
                        node.value = value
                        return False
                else:
                        self._root = self._bstInsert(self._root, key, value)
                        self._size += 1
                        return True

        def _bstInsert(self, subtree, key, value):
                if subtree is None:
                        subtree = _BSTMapNode(key, value)
                elif key < subtree.key:
                        subtree.left = self._bstInsert(subtree.left, key, value)
                elif key > subtree.key:
                        subtree.right = self._bstInsert(subtree.right, key, value)
                        return subtree
        def valueOf(self, key):
            node = self._bstSearch(self._root, key)
            assert node is not None, "Invalid map key."
            return node.value

        def valuesOf(self,min, max):
            node = self._bstSearchRange(self._root, min, max)
            assert node is not None, "Invalid map key."
            bstdict = {key:node.value}
            return bstdict
#Searches for a specific target
        def _bstSearch(self, subtree, target):
                if subtree is None:
                        return None
                elif target < subtree.key:
                        return self._bstSearch( subtree.left, target)
                elif target > subtree.key:
                        return self._bstSearch(subtree.right, target)
                else:
                        return subtree
#Searches for a range of items
        def _bstSearchRange(self, subtree, min, max):
                results = []
                if subtree is None:
                        return []
                if subtree.key >= min and subtree.key <= max:
                        results.append(subtree)
                if min < subtree.key:
                        results.extend(self._bstSearchRange(subtree.left, min, max))
                if max > subtree.key:
                        results.extend(self._bstSearchRange(subtree.right, min, max))
                        return results

class _BSTMapNode :
    def __init__( self, key, value ):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
