import unittest
from src.ans import EventManager

class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event = EventManager("Tech Conference")

    def test_add_participant(self):
        self.event.add_participant("Alice")
        self.assertIn("Alice", self.event.participants)

    def test_remove_participant(self):
        self.event.add_participant("Bob")
        self.event.remove_participant("Bob")
        self.assertNotIn("Bob", self.event.participants)

    def test_get_participant_list(self):
        self.event.add_participant("Alice")
        self.event.add_participant("Bob")
        expected_list = ["Alice", "Bob"]
        self.assertEqual(self.event.get_participant_list(), expected_list)


if __name__ == '__main__':
    unittest.main()
