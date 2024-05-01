import unittest
from unittest.mock import patch, MagicMock

from tests.facts_api import get_random_fact, get_len_of_fact


class TestFactApi(unittest.TestCase):
    @patch('tests.facts_api.get_random_fact')
    def test_len_of_fact(self, mock_get_fact):
        mock_get_fact.return_value = 'Cats have nine lives'
        self.assertEqual(get_len_of_fact(), 20)

    @patch('tests.facts_api.requests')
    def test_get_fact(self, mock_request):
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = [{'fact': 'I love dogs so much'}]
        mock_request.get.return_value = mock_response
        self.assertEqual(get_random_fact(), 'I love dogs so much')

    @patch('tests.facts_api.requests')
    def test_fail_get_fact(self, mock_request):
        mock_response = MagicMock(status_code=403)
        mock_response.json.return_value = {'message': 'Error 403'}
        mock_request.get.return_value = mock_response
        mock_request.exceptions.HTTPError = IOError
        self.assertRaises(IOError, get_random_fact)


if __name__ == '__main__':
    unittest.main()
