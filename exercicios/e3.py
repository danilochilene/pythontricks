# coding: utf-8
"""
>>> all(m)
False
>>> all(n)
True
>>> any(m)
True
>>> any(n)
True
>>> sum(n)
60
>>> sum(m+n)
76
>>> sum(a*b for (a,b) in enumerate(n))
80
>>> all(x for (x,y) in zip(m, n))
True
>>> sum(x*y for (x,y) in zip(m, n))
320
"""

m = [5, 3, 7, 2, 0, -1]
n = [10, 20, 30]

if __name__=='__main__':
    import doctest
    doctest.testmod()