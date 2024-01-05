import sys

text = sys.stdin.buffer.read()

encodings = ['KOI8-R', 'CP1251', 'CP866', 'ISO-8859-5', 'MACCYRILLIC', 'CP855']


def find_enc_list():
    lev = 'Лев НиколачТстй.АнКрМмщ,здВыьпхжугя-шОбЖюфцъПэД;С"?!:IlmiotesrГИ()ЧЭУЯЕRandЗРЦФБХcЩ\'ШLTybpuzvgHhwMBAPCf1qxUjkN28DXVKS705364Q9JEOFYZWЮ\n'

    lev = lev.encode('KOI8-R')
    proc = {lev : []}
    ch = True
    while ch:
        ch = False
        newdict = dict()
        for a in proc.keys():
            for dec in encodings:
                try:
                    dec_levin = a.decode(dec)
                except:
                    continue
                for enc in encodings:
                    if (enc == dec):
                        continue
                    try:
                        new_levin = dec_levin.encode(enc)
                    except:
                        continue
                    if not (new_levin in proc) and not (new_levin in newdict):
                        newdict[new_levin] = proc[a] + [dec, enc]
                        ch = True
        proc.update(newdict)
    return proc
    

a = find_enc_list()
k = 0
for i in a.keys():
    lev = "Левин"
    lev = lev.encode("KOI8-R")
    k = 0
    for j in a[i]:
        if (k % 2 == 0):
            lev = lev.decode(j)
        else:
            lev = lev.encode(j)
        k+=1
    if (lev in text):
        tmp = a[i]
    

for i in tmp[::-1]:
    if (k % 2 == 0):
        text = text.decode(i)
    else:
        text = text.encode(i)
    k+=1

text = text.decode('KOI8-R')
    
#text = text.decode('KOI8-R')
print(text)

#a = "Левин"
#a = a.encode('KOI8-R').decode('CP1251').encode('KOI8-R')
#a = a.decode('CP1251').encode('CP866')
#a = a.decode('CP855').encode('MACCYRILLIC')

#print(a in text)

#text = text.decode('MACCYRILLIC').encode('CP855')
#text = text.decode('CP866').encode('CP1251')
#text = text.decode('KOI8-R').encode('CP1251').decode('KOI8-R')