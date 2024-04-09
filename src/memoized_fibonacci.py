from src.recursive_fibonacci import recursive_fibonacci

def memoized_fibonacci(position, cache=None): 
    if cache is None:
        cache = {0: 1, 1: 1}

    if position not in cache:
        cache[position] = recursive_fibonacci(position, lambda _ : memoized_fibonacci(_, cache))
        
    return cache[position]
