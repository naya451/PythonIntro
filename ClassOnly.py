import itertools

_allowed_fields = {''.join(i) for i in itertools.product('abcd', repeat=4)}


class Struct:
    __slots__ = []
    
    def __getattribute__(self, attr):
        if attr in _allowed_fields:
            return attr
        raise AttributeError
    
