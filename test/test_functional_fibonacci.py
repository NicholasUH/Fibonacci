import unittest
from src.functional_fibonacci import functional_fibonacci
from test_base_fibonacci import BaseFibonacciTest

class TestFunctionalFibonacci(BaseFibonacciTest, unittest.TestCase):
    def get_fibonacci_function(self):
        return functional_fibonacci
    