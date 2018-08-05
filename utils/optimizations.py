"""
Some custom helpers for random optimizations
"""
class lazyproperty:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return None
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
