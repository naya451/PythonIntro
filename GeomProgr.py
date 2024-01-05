import sys

class Geom:
    def __init__(self, base, ratio):
        self.base = base
        self.ratio = ratio
        self.curr = 1

    def __iter__(self):
        current = self.base
        while True:
            yield current
            current *= self.ratio   

    def hellp(self, res):
        for i in res:
            curr = i
            yield i     
        while True:
            curr *= self.ratio  
            yield curr
             

    def __getitem__(self, index):
        if isinstance(index, slice):
            if (index == slice(None, None, None)):
                return self[...]
            start, stop, step = index.indices(sys.maxsize)
            return [self[i] for i in range(start, stop, step)]
        if isinstance(index, int):
            return self.base * (self.ratio ** index)
        if index is Ellipsis:
            return self.__iter__()
        if isinstance(index, tuple): 
            res = []
            st = index[0]
            l = len(index)
            for i in range(l):
                if index[i] is Ellipsis:
                    if i > 0 and i < l - 1:
                        res += self[index[i - 1]: index[i + 1]]
                    elif i > 0:
                        return self.hellp(res + [self.__getitem__(index[i - 1])])
                    elif i < l:
                        res += self[:index[i + 1]]
                    else:
                        return self.hellp(res)
            return res


