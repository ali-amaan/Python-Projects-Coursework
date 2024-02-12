# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
import unittest
import random

from stack import Stack
from docent import alpha_order

class TestDocent(unittest.TestCase):
    """
    Unit tests for the stack_sort function.
    """

    def setUp(self):
        self.stack = Stack()

    def test01_pair(self):
        """Pair of books is ordered correctly. (5p)"""

        book1 = "Java"
        book2 = "C++"

        s = self.stack
        s.push(book1)
        s.push(book2)

        alpha_order(s)
        ordered = []
        ordered.append(s.pop())
        ordered.append(s.pop())
        expected = [book2, book1]
        self.assertListEqual(ordered, expected,
            "The books should be in alphabetical order from A to Z.")

        self.assertTrue(s.is_empty(),
            "The stack should be empty after popping two items.")

    def test02_finished_pair(self):
        """Pair of books remains untouched if they are already ordered. (5p)"""

        book1 = "C"
        book2 = "C++"

        s = self.stack
        s.push(book1)
        s.push(book2)

        alpha_order(s)
        ordered = []
        ordered.append(s.pop())
        ordered.append(s.pop())
        expected = [book1, book2]
        self.assertListEqual(ordered, expected,
            "The books should be in alphabetical order from A to Z.")

        self.assertTrue(s.is_empty(),
            "The stack should be empty after popping two items.")

    def test03_four_books(self):
        """Five books are ordered correctly. (10p)"""

        book1 = "Lambdas"
        book2 = "C++"
        book3 = "Compilers"
        book4 = "Quantization"
        book5 = "Algebra"

        s = self.stack
        s.push(book1)
        s.push(book2)
        s.push(book3)
        s.push(book4)
        s.push(book5)

        alpha_order(s)
        ordered = []
        while (s.is_empty() == False):
            ordered.append(s.pop())

        expected = [book5, book2, book3, book1, book4]
        self.assertListEqual(ordered, expected, "When calling pop() for the "
            "stack repeatedly, the books should come in alphabetical order "
            "from A to Z.")

        self.assertTrue(s.is_empty(),
            "The stack should be empty after popping two items.")

    #​‌​‌‌​​​‌​‌​​​‌ def test_stack_sort_with_small_set(self):
    #​‌​‌‌​​​‌​‌​​​‌     """alpha_order function orders the stack correctly with small set of random integers (10p)"""
    #​‌​‌‌​​​‌​‌​​​‌
    #​‌​‌‌​​​‌​‌​​​‌     n = 10
    #​‌​‌‌​​​‌​‌​​​‌     s = self.stack
    #​‌​‌‌​​​‌​‌​​​‌     imitation_list = [random.randint(-10, 50) for i in range(n)]
    #​‌​‌‌​​​‌​‌​​​‌     for i in range(10):
    #​‌​‌‌​​​‌​‌​​​‌         s.push(imitation_list[i])   # add values to stack
    #​‌​‌‌​​​‌​‌​​​‌
    #​‌​‌‌​​​‌​‌​​​‌     imitation_list.sort()
    #​‌​‌‌​​​‌​‌​​​‌     alpha_order(s) # sort the stack
    #​‌​‌‌​​​‌​‌​​​‌
    #​‌​‌‌​​​‌​‌​​​‌     for i in range(n):
    #​‌​‌‌​​​‌​‌​​​‌         pop_value = s.pop()
    #​‌​‌‌​​​‌​‌​​​‌         expected = imitation_list[i]
    #​‌​‌‌​​​‌​‌​​​‌         self.assertEqual(
    #​‌​‌‌​​​‌​‌​​​‌             pop_value,
    #​‌​‌‌​​​‌​‌​​​‌             expected,
    #​‌​‌‌​​​‌​‌​​​‌             ("Pushed {} numbers onto stack S and then called alpha_order(S).\n"
    #​‌​‌‌​​​‌​‌​​​‌              "After the function call, popped values from S\n"
    #​‌​‌‌​​​‌​‌​​​‌              "and compared to sorted model values:\n"
    #​‌​‌‌​​​‌​‌​​​‌              "S.pop() call number {} returned {} but {} was expected."
    #​‌​‌‌​​​‌​‌​​​‌             ).format(n, i+1, pop_value, expected)
    #​‌​‌‌​​​‌​‌​​​‌         )
    #​‌​‌‌​​​‌​‌​​​‌
    #​‌​‌‌​​​‌​‌​​​‌     #If reached, stack should be empty
    #​‌​‌‌​​​‌​‌​​​‌     self._assert_empty(s, n)


if __name__ == "__main__":
    #​‌​‌‌​​​‌​‌​​​‌ Run the tests
    unittest.main(verbosity = 2)

