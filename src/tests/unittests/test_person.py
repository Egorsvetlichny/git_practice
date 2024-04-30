import unittest
from tests.person import Person


class TestPerson(unittest.TestCase):
    def test_work(self):
        test_cases = [
            {
                'arguments': {'sleep_time': 9.5 * 60 * 60, 'got_eat': True},
                'result': True
            },
            {
                'arguments': {'got_eat': True},
                'result': True
            },
            {
                'arguments': {'sleep_time': 8.5 * 60 * 60},
                'result': True
            },
            {
                'arguments': {},
                'result': True
            },
            {
                'arguments': {'sleep_time': 5.5 * 60 * 60, 'got_eat': True},
                'result': False
            },
            {
                'arguments': {'sleep_time': 9.5 * 60 * 60, 'got_eat': False},
                'result': False
            },
        ]

        for test_case in test_cases:
            person = Person('Person')

            self.assertIs(person.work(**test_case['arguments']), test_case['result'])
