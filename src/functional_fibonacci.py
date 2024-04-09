from functools import reduce
from src.validate_position import validate_position
    
@validate_position    
def functional_fibonacci(position):    
    return reduce(lambda pair, _: (pair[1], sum(pair)), range(position - 1), (1, 1))[1]
