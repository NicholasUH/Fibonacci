from parameterized import parameterized

class BaseFibonacciTest:
    @parameterized.expand([(0, 1), (1, 1), (2, 2), (5, 8), (8, 34), (10, 89)])
    def test_fibonacci(self, position, expected_result):
       self.assertEqual(self.get_fibonacci_function()(position), expected_result)
    
    def test_fibonacci_negative_position(self):
        self.assertRaisesRegex(ValueError, "position must be positive", self.get_fibonacci_function(), -1)
