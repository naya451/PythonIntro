str1 = '''/1\\
|"|
\-/'''


class Smile:
    def __init__(self, s):
        self.s = s

    def __neg__(self):
        return Smile(-self.s)
    
    def __abs__(self):
        return abs(self.s)
    def __mul__(self, other):
        return Smile(self.s * other)
    def __add__(self, other):
        return Smile(self.s + other.s)

    def __sub__(self, other):
        return Smile(self.s - other.s)
    
    def __str__(self):
        if (self.s == 0):
            return ""
        if (self.__abs__() == 1):
            return str1
        strs = self.__abs__() + 2
        cols = (self.__abs__() - 1) * 2 + 3
        eyes = self.__abs__() // 4
        mod = f'{self.__abs__()}'
        res = ""
        res += ("/"+mod+("-" * (cols - len(mod) - 2))+ "\\\n")
        if (self.s < 0):
            for i in range(0, eyes):
                res += ("|"+" " * (cols - 2) +"|\n")
            res += ("|" + " " * (eyes + 1) + "-" * (cols - 2 * (eyes + 1) - 2) + 
                " " * (eyes + 1) + "|\n")
            for i in range(0, strs - eyes * 2 - 4):
                res += ("|"+" " * (cols - 2) +"|\n")
            res += ("|" + " " * eyes + "O"  + " " * (cols - 2 * eyes - 4) + 
                "O" + " " * eyes + "|\n")
            for i in range(0, eyes):
                res += ("|"+" " * (cols - 2) +"|\n")
        else:
            for i in range(0, eyes):
                res += ("|"+" " * (cols - 2) +"|\n")
            res += ("|" + " " * eyes + "O"  + " " * (cols - 2 * eyes - 4) + 
                "O" + " " * eyes + "|\n")
            for i in range(0, strs - eyes * 2 - 4):
                res += ("|"+" " * (cols - 2) +"|\n")
            res += ("|" + " " * (eyes + 1) + "-" * (cols - 2 * (eyes + 1) - 2) + 
                " " * (eyes + 1) + "|\n")
            
            for i in range(0, eyes):
                res += ("|"+" " * (cols - 2) +"|\n")
        res += ("\\" + "-" * (cols - 2) + "/")
        return res


