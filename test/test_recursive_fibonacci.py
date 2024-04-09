import unittest
from src.recursive_fibonacci import recursive_fibonacci
from test_base_fibonacci import BaseFibonacciTest

class TestRecursiveFibonacci(BaseFibonacciTest, unittest.TestCase):
    def get_fibonacci_function(self):
        return recursive_fibonacci
