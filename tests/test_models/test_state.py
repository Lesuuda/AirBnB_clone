import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes_types(self):
        state = State()
        self.assertIsInstance(state.name, str)

    def test_id_generation(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_created_updated_at(self):
        state = State()
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict_method(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('id', state_dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)


if __name__ == '__main__':
    unittest.main()
