import math

def KLDivergence(d1, d2, sample_num):
    dic1_keys, dic2_keys = list(d1.keys()), list(d2.keys())
    keys = set(dic1_keys + dic2_keys)
    new_d1, new_d2 = dict(), dict()
    for i in dic1_keys:
        new_d1[i] = (d1.get(i, 0) + 0.01) / sample_num
    for j in dic2_keys:
        new_d2[j] = (d2.get(j, 0) + 0.01) / sample_num
    H = 0
    for k in keys:
        H -= new_d1.get(k, 0.001) * (math.log2(new_d2.get(k, 0.001) / new_d1.get(k, 0.001)))
    return H

def JSDivergence(d1, d2, sample_num):
    dic1_keys, dic2_keys = list(d1.keys()), list(d2.keys())
    keys = set(dic1_keys + dic2_keys)
    M = {}
    for k in keys:
        M[k] = (d1.get(k, 0) + d2.get(k, 0)) / 2
    H = KLDivergence(d1, M, sample_num) + KLDivergence(d2, M, sample_num)
    return H/2