def joinseq2(*seqs):
    seqs_iter = [0 for seq in seqs]
    flag = True
    while flag:
        i = 0
        while i < len(seqs) and seqs_iter[i] == -1:
            i += 1
        if (i == len(seqs_iter)):
            flag = False
            continue
        min_seq = seqs[i][seqs_iter[i]]
        i_seq = i
        for i in range(1, len(seqs)):
            if (seqs_iter[i]  > -1):
                if (seqs[i][seqs_iter[i]] < min_seq):
                    min_seq = seqs[i][seqs_iter[i]]
                    i_seq = i
                    
        if (seqs_iter[i_seq] == len(seqs[i_seq]) - 1):
            seqs_iter[i_seq] = -1
            yield min_seq
        elif (i_seq == -1):
            flag = False
        else:
            seqs_iter[i_seq] += 1
            yield min_seq

def my_min(args, key):
    i = 0
    mi = key(args[i])
    while i < len(args) and not mi:
        i += 1
        mi = key(args[i])
        print("mi:", mi)
    if (i == len(args)):
        return None
    while (i < len(args)):
        a = key(args[i])
        if a and a < mi:
            mi = a
        i += 1
        print("mi:", mi)
    return a


def find_min_i(args):
    mi = args[0]
    mii = 0
    i = 0
    while i < len(args):
        if mi > args[i]:
            mi = args[i]
            mii = i
        i += 1
    return mii

def joinseq(*seqs):
    seqs1 = [iter(seq) for seq in seqs]
    vals = [next(i, None) for i in seqs1]
    for i in range(0, len(vals)):
        if vals[i] is None:
            seqs1.remove(seqs1[i])
            vals.remove(vals[i])
    
    while vals:
        i = find_min_i(vals)
        yield vals[i]
        vals[i] = next(seqs1[i], None)
        if vals[i] is None:
            seqs1.remove(seqs1[i])
            vals.remove(vals[i])
