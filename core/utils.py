def validate_value(value,cls):
    if not isinstance(value,cls):
        raise TypeError(f'{value} must be in type {cls}')
    return True
