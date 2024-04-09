def validate_position(func):
    def validate_and_execute(*args, **kwargs):
        if args[0] < 0:
            raise ValueError("position must be positive")

        return func(*args, **kwargs)

    return validate_and_execute
