def compose(f, g):
    def wrapper(*args):
        return f(g(*args), g(*args[::-1]))
    return wrapper

