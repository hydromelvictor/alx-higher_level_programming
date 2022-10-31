#!/usr/bin/python3
"""test for class base
"""

import unittest
from models import base
Base = base.Base



class TestBase(unittest.TestCase):
    """class inheritance for unittest"""

    def test_doc_module(self):
        """doc module verify
        """
        doc = base.__doc__
        self.assertTrue(len(doc) > 1)

    def test_doc_class(self):
        """doc for class verify
        """
        doc = Base.__doc__
        self.assertTrue(len(doc) > 1)

    def test_doc_init(self):
        """doc for function init verify
        """
        doc = Base.__init__.__doc__
        self.assertTrue(len(doc) > 1)

    def test_base1(self):
        """test1
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_base2(self):
        """test2
        """
        b = Base(4)
        self.assertEqual(b.id, 4)
