#!/usr/bin/python3
"""test for class base
"""


import unittest
base = __import__("models/base").Base


class TestBase(unittest.TestCase):
    """class inheritance for unittest
    """
    def doc_module(self):
        """doc module verify
        """
        doc = __import__("models/base").__doc__
        self.assertTrue(len(doc) > 1)

    def doc_class(self):
        """doc for class verify
        """
        doc = __import__("models/base").Base.__doc__
        self.assertTrue(len(doc) > 1)

    def doc_init(self):
        """doc for function init verify
        """
        doc = __import__("models/base").Base.__init__.__doc__
        self.assertTrue(len(doc) > 1)
