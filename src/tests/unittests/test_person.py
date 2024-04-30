import unittest
from tests.person import Person

person = Person('Person')


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
            self.assertIs(person.work(**test_case['arguments']), test_case['result'])

    def test_work_exceptions(self):
        test_cases = [
            {
                'arguments': {'sleep_time': -9.5 * 60 * 60, 'got_eat': True},
                'exc': ValueError
            },
            {
                'arguments': {'sleep_time': 0, 'got_eat': True},
                'exc': ValueError
            },
            {
                'arguments': {'sleep_time': 11.5 * 60 * 60},
                'exc': ValueError
            },
            {
                'arguments': {'sleep_time': '11 * 60 * 60'},
                'exc': TypeError
            },
            {
                'arguments': {'sleep_time': 11 * 60 * 60, 'got_eat': [4, 5, 1]},
                'exc': TypeError
            },
            {
                'arguments': {'sleep_time': True},
                'exc': TypeError
            },
            {
                'arguments': {'sleep_time': {}},
                'exc': TypeError
            },
        ]

        for test_case in test_cases:
            self.assertRaises(test_case['exc'], person.work, **test_case['arguments'])
