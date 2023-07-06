class _DoubleLinkedBase:
    """ A base class providing a doubly linked list representation."""

    class _Node:
        """ Lightweight, nonpublic class for storing a doubly linked node"""
        __slots__ = '_element', '_prev', '_next' # streamline memory

        def __init__(self, element, prev, next): # initialize node's fields
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0 # number of elements

    def __len__(self):
        """Return the number of elements in the list"""
        n = self._header._next
        len = 0
        while (n._next is not None):
            len=len+1
            n=n._next
        return len

    def is_empty(self):
        """Return true if list is empty"""
        n = self._header._next._next
        if n is not None:
          return False
        else:
          return True
          
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node"""
       

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its elements"""
        k = node._element
        n = self._header._next
        if n._next is None :
            return None
        else : 
           while n is not node:
             n = n._next
           n._prev._next = n._next
           n._next._prev = n._prev
           return k