#!/usr/bin/python3
"""test for rectangle
"""


import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """class inheritance for unittest
    """
    def doc_module(self):
        """doc module verify
        """
        n = __import__("rectangle").__doc__
        self.assertTrue(len(n) > 1)

    def doc_class(self):
        """doc module verify
        """
        n = __import__("rectangle").Rectangle.__doc__
        self.assertTrue(len(n) > 1)

    def doc_init(self):
        """doc module verify
        """
        n = __import__("rectangle").Rectangle.__init__.__doc__
        self.assertTrue(len(n) > 1)

    def rect1(self):
        """test1
        """
        r = Rectangle(4, 1)
        self.assertEqual(r.id, 1)
        #self.assertEqual(r.width(), 4)
        #self.assertEqual(r.height(), 1)
        #self.assertEqual(r.x(), 0)
        #self.assertEqual(r.y(), 0)
        
    def rect2(self):
        """test2
        """
        r = Rectangle(4, 1, 7, 2, 0)
        self.assertEqual(r.id, 0)
        #self.assertEqual(r.width(), 4)
        #self.assertEqual(r.height(), 1)
        #self.assertEqual(r.x(), 7)
        #self.assertEqual(r.y(), 2)




if __name__ == "__main__":
    unittest.main()
