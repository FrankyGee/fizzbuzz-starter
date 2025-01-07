import unittest
from parameterized import parameterized

import validate_fizzbuzz
from fizzbuzz import apply_fizzbuzz

def test_name_func(the_test, index, params):
    return f"{the_test.__name__} - {params.args[0]}"

class MyTestCase(unittest.TestCase):
    def test_r01_01_simple_fizz(self):
        expected = "Fizz"
        actual = apply_fizzbuzz(3)
        self.assertEqual(expected, actual)

    def test_r01_02_simple_buzz(self):
        expected = "Buzz"
        actual = apply_fizzbuzz(5)
        self.assertEqual(expected, actual)

    def test_r01_02_simple_fizzbuzz(self):
        expected = "FizzBuzz"
        actual = apply_fizzbuzz(15)
        self.assertEqual(expected, actual)

    def test_r01_03_simple_none(self):
        expected = "2"
        actual = apply_fizzbuzz(2)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ("1", "1"),
        ("2", "2"),
        ("3", "Fizz"),
        ("4", "4"),
        ("5", "Buzz"),
        ("6", "Fizz"),
        ("7", "7"),
        ("8", "8"),
        ("9", "Fizz"),
        ("10", "Buzz"),
        ("11", "11"),
        ("12", "Fizz"),
        ("13", "13"),
        ("14", "14"),
        ("15", "FizzBuzz"),
    ], name_func=test_name_func)
    def test_r01_04_more(self, test_value, expected):
        actual = apply_fizzbuzz(test_value)
        self.assertEqual(expected, actual)

    def test_x_from_cli(self):
        self.assertEqual(0, validate_fizzbuzz.run_tests("../fizzbuzz.py", validate_fizzbuzz.test_cases))



if __name__ == '__main__':
    unittest.main()
