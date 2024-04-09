import unittest
from src.imperative_fibonacci import imperative_fibonacci
from test_base_fibonacci import BaseFibonacciTest

class TestImperativeFibonacci(BaseFibonacciTest, unittest.TestCase):
    def canary_test(self):
        self.assertTrue(True)

    def get_fibonacci_function(self):
        return imperative_fibonacci
