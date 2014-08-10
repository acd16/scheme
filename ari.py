import sys

def add(m, n):
    if n==0:
        return m
    else:
        return 1 + add(m, n-1)

def sub(m, n):
    if n==0:
        return m
    else:
        return sub(m, n-1) - 1

def car(tup):
    return tup[0]

def cdr(tup):
    return tup[1:]

def addtup (tup):
    if not tup:
        return 0
    else:
        return car(tup) + addtup(cdr(tup))

def mul(m,n):
    if n==0:
        return 0
    else:
        return m + mul(m, n-1)

def cons(m, n):
    try:
        o = m+n
    except:
        return m
    return o

def tupa(m, n):
    if not m and not n:
        return
    elif(m and n):
        return cons([car(m)+car(n)], tupa(cdr(m), cdr(n)))
    else:
        print "unequal list size"
        sys.exit(0)

def gra(m,n):
    if n == 0:
        return "T"
    elif m == 0:
        return "F"
    else:
        return gra(m-1, n-1)

def less(m,n):
    if m == 0:
        return "T"
    elif n == 0:
        return "F"
    else:
        return less(m-1, n-1)

def exp(m, n):
    if n == 1:
        return m
    else:
        return (mul(m, exp(m,n-1)))

def div (m, n):
    if (m<n):
        return 0
    else:
        return 1+div(m-n,n)

def len(m):
    if not m:
        return 0
    else:
        return 1 + len(cdr(m))

def pick(m, n):
    if n==1:
        return car(m)
    else:
        return pick(cdr(m), n-1)

def rempick(m,n):
    if n == 1:
        return list(cdr(m))
    else:
        return cons([car(m)], rempick(cdr(m), n-1))

def remnums(m):
    if not m:
        return None
    else:
        if isinstance(car(m), int):
            return remnums(cdr(m))
        else:
            return cons([car(m)], remnums(cdr(m)))

def onlynums(m):
    if not m:
        return None
    else:
        if isinstance(car(m), int):
            return cons([car(m)], onlynums(cdr(m)))
        else:
            return onlynums(cdr(m))

def count (a, tup):
    if not tup:
        return 0
    else:
        if car(tup) == a:
            return 1+count(a, cdr(tup))
        else:
            return count(a, cdr(tup))

def nrempick(n, lat):
    if not lat:
        return None
    else:
       if n==1:
           return nrempick(n-1, cdr(lat))
       else:
           return cons([car(lat)], nrempick(n-1, cdr(lat)))
'''
print add (12,16)
print sub (16,12)
print addtup((1,2,3))
print mul (61,2)
n = (3,2,1,4,5)
print tupa (m,n)
print less(16,26)
print exp(5,3)
print len((1,2,3,4,9))
print div(20,5)
print rempick(m,3)
print onlynums(m)
'''

m = ("this",8,"that",9,8)
print nrempick(2,m)
