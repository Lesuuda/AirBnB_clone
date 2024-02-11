import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):

    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes_types(self):
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_id_generation(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_updated_at(self):
        user = User()
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('id', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

if __name__ == '__main__':
    unittest.main()
