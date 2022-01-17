def percentage(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if kwargs.get('percentage', False):
            return result * 100
        return result
    return inner
