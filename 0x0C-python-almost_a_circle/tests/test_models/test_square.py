#!/usr/bin/python3
"""unittest for Square()
"""

import unittest
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """inhiterance"""

    def test_module_doc(self):
        n = square.__doc__
        self.assertTrue(len(n) > 1)

    def test_module_class(self):
        n = Square.__doc__
        self.assertTrue(len(n) > 1)

    def test_module_func(self):
        n = [
            Square.__init__.__doc__,
            Square.__str__.__doc__,
            Square.size.getter.__doc__,
            Square.size.setter.__doc__,
            Square.update.__doc__,
            Square.to_dictionary.__doc__
        ]

        for i in n:
            self.assertTrue(len(i) > 1)

    def test_instance1(self):
        s = Square(4, 0, 0)
        self.assertEqual(s.__str__, "[Square] (1) 0/0 - 4")

    def test_instance2(self):
        s = Square(4, 0, 0, 3)
        self.assertEqual(s.__str__, "[Square] (3) 0/0 - 4")

    def test_instance3(self):
        s = Square(4, 8, 1, 3)
        self.assertEqual(s.__str__, "[Square] (3) 8/1 - 4")

    def test_instance4(self):
        s = Square(2)
        s.size = 7
        self.assertEqual(s.size, 7)

    def test_instance5(self):
        s = Square(7)
        s.update(1, 2, 0)
        self.assertEquals([s.id, s.height, s.x], [1, 2, 0])
    
    def test_instance6(self):
        s = Square(2)
        s.update(8)
        self.assertEquals([s.id, s.width, s.x, s.y], [8, 2, 0, 0])

    def test_instance7(self):
        s = Square(1)
        d = {'size': 4, 'x': 2}
        s.update(d)
        self.assertEquals([s.id, s.height, s.x], [1, 4, 2])

    def test_instance8(self):
        s = Square(3)
        n = [1, 7, 5, 2]
        d = {'id': 2, 'size': 5}
        s.update(n, d)
        self.assertEquals([s.id, s.height, s.x], [1, 7, 5])

    def test_instance9(self):
        self.assertEquals(Square(10, 4, 12, 3).to_dictionary(),
            {'id': 3, 'size': 10, 'x': 4, 'y': 12})



class TestSquareFail(unittest.TestCase):
    """test fails"""

    def test_fail0(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_fail1(self):
        with self.assertRaises(TypeError):
            Square("mariam", 0, 0)

    def test_fail2(self):
        with self.assertRaises(TypeError):
            Square(1, [2], 1, 8)

    def test_fail3(self):
        with self.assertRaises(ValueError):
            Square(5, 2, -1)
    
    def test_fail4(self):
        with self.assertRaises(ValueError):
            Square(1).size = -7

    def test_fail5(self):
        with self.assertRaises(TypeError):
            Square(2).size = [0, "5"]

    def test_fail6(self):
        with self.assertRaises(TypeError):
            Square(4).update("4")

    def test_fail7(self):
        with self.assertRaises(ValueError):
            Square(4).update(12, 7, -1)

    def test_fail8(self):
        d = {'id': 2, 'size': [12, 0]}
        with self.assertRaises(TypeError):
            Square(4).update(d)
