#!/usr/bin/python3

"""
    unittest for function max_integer
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
        test class for max_integer
        subclass of de unittest
    """

    def doc_module(self):
        """
            docstring of module verificaton
        """
        m = __import__("6-max_integer").__doc__
        self.assertTrue(len(m) > 1)


    def doc_function(self):
        """
            docstring of function verification
        """
        m = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(m) > 1)


    def example1(self):
        """
            empty list
        """
        n = []
        self.assertIsNone(max_integer(n))


    def example2(self):
        """
            list of [1, 2, 3]
        """
        n = [1, 2, 3]
        self.assertEqual(max_integer(n), 3)


    def example3(self):
        """
            list of [7, -12, 4.7, 0]
        """
        n = [7, -12, 4.7, 0]
        self.assertEqual(max_integer(n), 7)


    def example4(self):
        """
            list of [2.8]
        """
        n = [2.8]
        self.assertEqual(max_integer(n), 2.8)


    def example5(self):
        """
            list of [7, "miami", [4, -85], 0]
        """
        n = [7, "miami", [4, -85], 0]
        with self.assertRaises(TypeError):
            max_integer(n)



if __name__ == "__main__":
    unittest.main()
