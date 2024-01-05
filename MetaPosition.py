# class positioned(type):
#     def __new__(cls, name, bases, dct):
#         annotations = dct.get('__annotations__', {})
#         fields = [f"{field}={value}" for field, value in annotations.items()]
#         dct['__str__'] = lambda self: ' '.join(fields)
#         def init(self, *args):
#             for i, arg in enumerate(args):
#                 if i < len(fields):
#                     setattr(self, list(annotations.keys())[i], arg)
#         dct['__init__'] = init
#         return super().__new__(cls, name, bases, dct)

# class C(metaclass=positioned):
#     a: int = 1
#     b: float = 42.0

# for c in C(), C(4), C(100.0, 500), C(7, 2):
#     print(c)
#     match c:
#         case C(1):
#             print("C1", c.b)
#         case C(b=42):
#             print("C42", c.a)
#         case C(100, 500):
#             print("C100500")
#         case C():
#             print("C", c)

