"""
Some custom helpers for random optimizations
"""
class lazyproperty:
    """
    A descriptor class to decorate read only class
    attributes (properties) to be computed once on
    access then store that computed value on the instance.
    Saving multiple computations of the same property if
    it is accessed multiple times. Thanks Beazley:)
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return None
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
