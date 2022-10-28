#!/usr/bin/python3
"""test for class base
"""


import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """class inheritance for unittest
    """
    def doc_module(self):
        """doc module verify
        """
        doc = __import__("base").__doc__
        self.assertTrue(len(doc) > 1)

    def doc_class(self):
        """doc for class verify
        """
        doc = __import__("base").Base.__doc__
        self.assertTrue(len(doc) > 1)

    def doc_init(self):
        """doc for function init verify
        """
        doc = __import__("base").Base.__init__.__doc__
        self.assertTrue(len(doc) > 1)

    def base1(self):
        """test1
        """
        b = Base()
        self.assertEqual(print(b.id), 1)

    def base2(self):
        """test2
        """
        b = Base(4)
        self.assertEqual(print(b.id), 4)




if __name__ == "__main__":
    unittest.main()