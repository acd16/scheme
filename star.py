#!/usr/bin/env python
import pdb
def car(l):
    try:
        return l[0]
    except IndexError:
        return []

def car_none(l):
    try:
        return l[0]
    except IndexError:
        return None

def cdr(l):
    return l[1:]

def cons_list(a,b):
    print "cons list", a, b
    if a is None:
        return b
    if b is None:
        return a
    a.append(b)
    return a

def cons(a,b):
    print "cons", a, b
    if a is None:
        return b
    if b is None:
        return a
    return a+b

def rember_star(a, l):
    if not l:
        return []
    elif not isinstance(car(l), list):
        if car(l) == a:
            return rember_star (a, cdr(l))
        else:
            return cons([car(l)], rember_star(a, cdr(l)))
    else:
        return cons([rember_star(a,car(l))], rember_star(a, cdr(l)))

def insr_star(old, new, lat):
    print "gg", isinstance(car(lat),list),"car: ", car(lat), "cdr: ", cdr(lat)
    if not lat:
        print "done"
        return
    elif not isinstance(car(lat), list):
        if car(lat) == old:
            return cons(cons_list([old],new), insr_star(old, new, cdr(lat)))
        else:
            return cons([car(lat)], insr_star(old,new,cdr(lat)))
    else:
        print "yo", car(lat)
        return cons([insr_star(old,new,car(lat))], insr_star(old,new,cdr(lat)))

def insr_rep(old,new,lat):
    if not lat:
        return
    else:
        if car(lat) == old:
            return cons(cons_list([old],new), insr_rep(old,new,cdr(lat)))
        else:
            return cons([car(lat)],insr_rep(old,new,cdr(lat)))

def occur_star(key, lat):
    if not lat:
        return 0
    elif not isinstance(car(lat), list):
        if car(lat) == key:
            #pdb.set_trace()
            return 1+occur_star(key, cdr(lat))
        else:
            return occur_star(key, cdr(lat))
    else:
        return occur_star(key ,car(lat)) + occur_star(key,cdr(lat))

def subt_star(a, b, l):
    if not l:
        return []
    elif not isinstance(car(l), list):
        if car(l) == b:
            return cons([a], subt_star (a, b, cdr(l)))
        else:
            return cons([car(l)], subt_star(a, b, cdr(l)))
    else:
        return cons([subt_star(a,b,car(l))], subt_star(a, b,cdr(l)))

def member(a, l):
    if not l:
        return False
    elif not isinstance(car(l), list):
        if car(l) == a:
            return True
        else:
            return member(a, cdr(l))
    else:
        return member(a, car(l)) or  member(a, cdr(l))

def insl_star(old, new, lat):
    if not lat:
        return
    elif isinstance(car(lat), list):
        return cons([insl_star(old,new,car(lat))], insl_star(old,new,cdr(lat)))
    else:
        if car(lat) == old:
            return cons(cons_list([new], old), insl_star(old, new, cdr(lat)))
        else:
            return cons([car(lat)], insl_star(old, new, cdr(lat)))

def leftmost(l):
    if not l:
        return False
    elif not isinstance(car(l), list):
        return car(l)
    else:
        return leftmost(car(l))


def eqlist(l,m):
    #pdb.set_trace()
    if not l and not m:
        return True
    elif not isinstance(car_none(l), list) and not isinstance(car_none(l), list):
        if car_none(l) == car_none(m):
            return eqlist(cdr(l), cdr(m))
        else:
            return False
    elif isinstance(car_none(l), list) and isinstance(car_none(l), list):
        return eqlist(car_none(l), car_none(m)) and eqlist(cdr(l), cdr(m))
    else:
        return False

#l = ['is', ['is', ['is']]]
l=['a', ['b', ['c']]]
m=['a', ['b', ['c']]]
print eqlist(l, m)
'''
print insl_star('it', 'his', l)
l = ['is', ['is', 'also']]
print rember_star('it', l)

print insr_star('is', 'his', l)
print rember_star('is',l)
'''
