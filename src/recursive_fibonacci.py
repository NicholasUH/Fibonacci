from src.validate_position import validate_position

@validate_position
def recursive_fibonacci(position, fibonacci_function = lambda _ : recursive_fibonacci(_)):
    return 1 if position in [0, 1] else fibonacci_function(position - 1) + fibonacci_function(position - 2)
