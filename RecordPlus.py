def Record(st, **field_values):
    def RecordClass(cls):
        dct = cls.__dict__.copy()
        a = set(dct['__slots__'])
        a = a.union(set(st.split(' ')))
        for i in a:
            if i in dct.keys():
                dct.pop(i)
        a = tuple(sorted(list(a)))
        dct['__slots__'] = a

        for k in field_values.keys():
            dct[k] = field_values[k]


        def funiter(self):
            tmp = set()
            for slot in sorted(list(set(dct['__slots__']))):
                if not slot.startswith('_'):
                    tmp.add(slot)
            for key in field_values.keys():
                tmp.add(key)
            for key in dct.keys():
                if not key.startswith('_'):
                    tmp.add(key)
            for i in sorted(list(tmp)):
                yield i
        

        dct['__iter__']  = funiter
        
        def funrepr(self):
            res = ""
            for i in self.__iter__():
                j = ""
                if i in dct.keys(): 
                    if not i.startswith('_'):
                        j = f"|{i}:" + f"{getattr(self, i)}"
                elif i in dct:
                    j = f"|{i}" + f"={dct[i]}"
                elif i in field_values.keys():
                    j = f"|{i}" + f"={field_values[i]}"
                else:
                    t = getattr(self, i, "nope")
                    if (t != "nope"):
                        j = f"|{i}=" + f"{t}"
                    else:
                        j = "|" + i
                
                res = res + j
            return res[1::]

        dct['__repr__']  = funrepr


        return type(cls)(cls.__name__, cls.__bases__, dct)
    return RecordClass


