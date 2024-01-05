import functools

def DefArgs(*constants):
    def decorator(func):
        if len(constants) < func.__code__.co_argcount:
            raise TypeError("Not enough constants for function parameters")
        #print('call dec')
        def wrapper(*args):
            #print('call mult')
            #print(*constants, *args)
            #print(func(2, 3))
            
            # Определения списка параметров с учетом заданных констант
            parameters = list(args) + list(constants[len(args):func.__code__.co_argcount])
            #print(parameters)
            #print(func(*parameters))
            # Проверяем количество входных параметров
            if len(parameters) > func.__code__.co_argcount:
                raise TypeError("Too many parameters provided for function")

            # Проверяем типы параметров
            for i, (param, const) in enumerate(zip(parameters, constants)):
                if not isinstance(param, type(const)):
                    raise TypeError(f"Parameter at position {i+1} is of type {type(param).__name__}, whereas expected type is {type(const).__name__}")
            
            return func(*parameters)
        return wrapper
    return decorator

