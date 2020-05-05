#!/usr/bin/python3
def weight_average(my_list=[]):
    def muli(x):
        for j in range(len(x) - 1):
           num = x[j] * x[j+1]
        return num
    def dec(p):
        for v in range(len(p) - 1):
            s= sum(p[v + 1])
        print(s)
        return s
    l = []
    for x in my_list:
        l.append(list(x))
    for i in l:
        m = muli(i)
        f = dec(l)
    return m / f

    




my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
print(weight_average(my_list))