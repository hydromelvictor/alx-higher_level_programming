#!/usr/bin/python3
"""test for class base
"""

import json
import unittest
from models.base import Base
import os



class TestBaseDoc(unittest.TestCase):
    """class inheritance for unittest"""

    def test_doc_module(self):
        """doc module verify
        """
        doc = Base.__doc__
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

    def test_doc_tojson(self):
        doc = Base.to_json_string.__doc__
        self.assertTrue(len(doc) > 1)

    def test_doc_save(self):
        doc = Base.save_to_file.__doc__
        self.assertTrue(len(doc) > 1)

    def test_doc_fromjson(self):
        doc = Base.from_json_string.__doc__
        self.assertTrue(len(doc) > 1)

    def test_doc_create(self):
        doc = Base.create.__doc__
        self.assertTrue(len(doc) > 1)

    def test_doc_load(self):
        doc = Base.load_from_file.__doc__
        self.assertTrue(len(doc) > 1)


class TestBase(unittest.TestCase):
    """test proprement dite"""

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

    def test_to_json1(self):
        self.assertEqual(Base(2).to_json_string([{'name': 'victor', 'age': 14}]),
            '[{"name": "victor", "age": 14}]')

    def test_to_json2(self):
        self.assertEqual(Base().to_json_string([]), '[]')

    def test_save1(self):
        r1 = {'id': 10, 'code': 7}
        r2 = {'name': 'victor', 'prof': 'garden', 'code': 14}
        Base(1).save_to_file([r1, r2])
        file = "Base.json"
        liste = []
        self.assertTrue(os.path.exists(file))
        with open(file, "r", encoding="utf-8") as f:
            for i in f:
                liste.append(f.readline())
        self.assertTrue(len(liste) > 1)

    def test_save2(self):
        Base().save_to_file([])
        file = "Base.json"
        liste = []
        self.assertTrue(os.path.exists(file))
        with open(file, "r", encoding="utf-8") as f:
            for i in f:
                liste.append(f.readline())
        self.assertTrue(len(liste) == 0)

    def test_from1(self):
        s = json.dumps([1, 0, 5, 2])
        self.assertEqual(Base.from_json_string(s), [1, 0, 5, 2])

    def test_from2(self):
        s = Base().to_json_string([])
        self.assertEqual(Base.from_json_string(s), [])


class TestBaseFail(unittest.TestCase):
    """fail test start"""

    def test_fail0(self):
        pass