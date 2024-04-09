import unittest
import timeit
from src.memoized_fibonacci import memoized_fibonacci
from src.recursive_fibonacci import recursive_fibonacci
from test_base_fibonacci import BaseFibonacciTest

def measure_execution_time(function, position):
    start_time = timeit.default_timer()
    function(position)
    end_time = timeit.default_timer()

    return end_time - start_time


class TestMemoizedFibonacci(BaseFibonacciTest, unittest.TestCase):
    def get_fibonacci_function(self):
        return memoized_fibonacci
    
    def test_speed_for_position(self):
        self.assertLess(measure_execution_time(memoized_fibonacci, 30) * 10, measure_execution_time(recursive_fibonacci, 30))
        
    def test_speed_for_small_position(self):
        self.assertLessEqual(abs(measure_execution_time(memoized_fibonacci, 3) - measure_execution_time(recursive_fibonacci, 3)), 1e-4)
        