class empty(type):
    def __new__(cls, name, bases, dct):
        def is_empty(self):
            return all(value for value in self.__dict__.values())
        dct['__bool__'] = is_empty
        return super().__new__(cls, name, bases, dct)

