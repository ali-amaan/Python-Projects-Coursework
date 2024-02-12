import unittest
from jump import jump


# Implement a test inside the given function that shows a flaw in the function "jump"
# the test should pass when the "jump" function works accordingly.

class TestJumpFunction(unittest.TestCase):
    # Implement your function here:
    def test_jump_pass(self):
        self.assertEqual(jump(228), "The jumper qualifies for the final.")


if __name__ == '__main__':
    unittest.main()
