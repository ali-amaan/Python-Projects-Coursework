# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ A class to describe a list node object
#​‌​‌‌​​​‌​‌​​​‌ The node object has the following attributes: obj, follower and predecessor

class ListNode:
    """
    The LinkedList uses ListNode objects to store added values.
    This class will not be tested by the grader.

    Attributes:
      obj: Any object that needs to be stored.
      follower: A ListNode object that follows this (self) ListNode object
        in the linked list.
      predecessor: A ListNode object that precedes this (self) ListNode object
        in the linked list.
    """
    def __init__(self, obj):
        """Initialize a list node object with the value obj."""
        self.obj = obj
        self.follower = None
        self.predecessor = None

    def get_obj(self):
        return self.obj

    def get_follower(self):
        return self.follower

    def get_predecessor(self):
        return self.predecessor

    def add_after(self, node):
        """Adds node 'node' as the follower of self node."""
        tmp = self.follower
        self.follower = node
        node.predecessor = self
        node.follower = tmp
        if tmp:
            tmp.predecessor = node

    def add_before(self, node):
        """Adds node 'node' as the predecessor of self node."""
        node.predecessor = self.predecessor
        node.follower = self
        tmp = self.get_predecessor()
        self.predecessor = node
        tmp.follower = node

    def remove_after(self):
        """Removes the follower of this node."""
        if self.follower:
            self.follower = self.follower.follower
            if self.follower:
                self.follower.predecessor = self


class UnderflowError(Exception):
    """An error raised when trying to remove one of guardian nodes."""
    def __init__(self):
        super().__init__("Can't remove from an empty list!")


class LinkedList:
    """
    An implementation of a doubly linked list that uses ListNode objects
    to represent nodes in the list. List indexes start from zero.

    The list contains one head and one tail guardian node with the values None.
    These can be used to check if the head or tail has been reached.
    The guardian nodes should not be included when counting the size of the list.
    """
    def __init__(self):
        """Initialize the linked list."""
        self.ListNode = ListNode
        self.head = self.ListNode(None)
        self.tail = self.ListNode(None)
        #​‌​‌‌​​​‌​‌​​​‌ An empty list should only have one head node followed by a tail node
        self.head.add_after(self.tail)
        self.size = 0

    def _get_at(self, n):
        """Return the node at position 'n'."""
        curr = self.head.get_follower()
        for i in range(n):
            curr = curr.get_follower()
        return curr

    def add_first(self, obj):
        """Add the object 'obj' as the first node."""
        first_node = ListNode(obj)
        self.head.add_after(first_node)
        self.size += 1

    def add_last(self, obj):
        """Add the object 'obj' as the last node."""
        last_node = ListNode(obj)
        self.tail.get_predecessor().add_after(last_node)
        self.size += 1

    def add_position(self, n, obj):
        """Insert the object 'obj' as the 'n'th node."""
        new_obj = ListNode(obj)
        node_at_n = self._get_at(n)
        if n == 0:
            self.add_first(obj)
        elif node_at_n is self.tail:
            self.add_last(obj)
        else:
            node_at_n.get_predecessor().add_after(new_obj)
        self.size += 1

    def remove_position(self, n):
        """Remove the node at the 'n'th position."""
        node_at_n = self._get_at(n)
        #​‌​‌‌​​​‌​‌​​​‌Prevent from removing guardian nodes.
        if node_at_n is self.tail or node_at_n is self.head:
            raise UnderflowError()

        predecessor = node_at_n.get_predecessor()
        if predecessor:
            predecessor.remove_after()
        self.size -= 1

    def get_position(self, n):
        """Return the value of the node at the 'n'th position or None
        if there is no node at that position."""
        node = self._get_at(n)
        return node.obj if node else None

    def get_size(self):
        """Return the number of objects in the list."""
        return self.size

    def get_max(self):
        """Return the value of the largest node in the list."""
        largest_node = self.head.get_follower()
        curr = self.head.get_follower()
        for i in range(1, self.get_size() - 1):
            curr = curr.get_follower()
            if largest_node.obj < curr.get_follower().obj:
                largest_node = curr.get_follower()
        return largest_node.obj

