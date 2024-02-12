# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ Implement the missing functions here below

from linkedlist import LinkedList

class Queue:

    #​‌​‌‌​​​‌​‌​​​‌ An implementation of a queue structure which utilizes the LinkedList class.

    #​‌​‌‌​​​‌​‌​​​‌ Attributes:
    #​‌​‌‌​​​‌​‌​​​‌ queue (LinkedList): A linked list that is used to store the objects added into the queue.


    def __init__(self):
        """ Initialize the queue """
        self.queue = LinkedList()


    def enqueue(self, obj):
        """ Adds the object 'obj' at the end of the queue """
        self.queue.add_last(obj)


    def dequeue(self):
        """ Removes and returns the first object in the queue """
        if self.queue.get_size() == 0:
            return None
        popped = self.queue.get_position(0)
        self.queue.remove_position(0)
        return popped

    def first(self):
        """ Returns the first object in the queue """
        return self.queue.get_position(0)


    def last(self):
        """ Returns the last object in the queue """
        return self.queue.get_position(self.queue.get_size() - 1)


    def is_empty(self):
        """ Returns true if the queue is empty, otherwise false """
        return self.queue.get_size() == 0
