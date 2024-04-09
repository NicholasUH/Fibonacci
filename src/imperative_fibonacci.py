from src.validate_position import validate_position

@validate_position
def imperative_fibonacci(position):    
    previous, current = 1, 1

    for _ in range(position - 1):
        previous, current = current, current + previous
    
    return current
