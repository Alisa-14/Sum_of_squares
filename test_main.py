import unittest
from main import process_numbers

class TestProcessNumbers(unittest.TestCase):
    def test_process_numbers(self):
        assert process_numbers([1, 2, 3, 4, 5, -2, -4]) == 20

    def test_process_numbers_empty(self):
        assert process_numbers([]) == 0

    def test_process_numbers_no_numb(self):
        assert process_numbers([1, 3, 5, -2, -4]) == 0

if __name__ == '__main__':
    unittest.main()
