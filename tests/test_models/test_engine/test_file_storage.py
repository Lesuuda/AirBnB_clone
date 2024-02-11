#!/usr/bin/python3

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_attributes(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all_method(self):
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(result, FileStorage._FileStorage__objects)

    def test_new_method(self):
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        self.assertIn("BaseModel." + b.id, models.storage.all().keys())
        self.assertIn(b, models.storage.all(). values())
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all(). values())
        self.assertIn("State." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all(). values())
        self.assertIn("Place." + p.id, models.storage.all().keys())
        self.assertIn(p, models.storage.all(). values())
        self.assertIn("City." + c.id, models.storage.all().keys())
        self.assertIn(c, models.storage.all(). values())
        self.assertIn("Amenity." + a.id, models.storage.all().keys())
        self.assertIn(a, models.storage.all(). values())
        self.assertIn("Review." + r.id, models.storage.all().keys())
        self.assertIn(r, models.storage.all(). values())

    def test_save_method(self):
        test_instance = BaseModel()
        self.file_storage.new(test_instance)
        self.file_storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_method(self):
        test_instance = BaseModel()
        self.file_storage.new(test_instance)
        self.file_storage.save()
        self.file_storage.reload()
        key = f"{test_instance.__class__.__name__}.{test_instance.id}"
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_reload_method_empty_file(self):
        empty_file_path = "empty_file.json"
        with open(empty_file_path, 'w') as empty_file:
            empty_file.write("")
        self.file_storage._FileStorage__file_path = empty_file_path
        self.file_storage.reload()


if __name__ == '__main__':
    unittest.main()
