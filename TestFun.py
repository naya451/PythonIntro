class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed=[]):
        ex1 = 0
        ex2 = 0
        for args in suite:
            try:
                self.fun(*args)
            except tuple(allowed):
                ex1 += 1
            except:
                ex2 += 1
        if (ex2):
            return 1
        if (ex1):
            return -1
        return 0


