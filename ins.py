def car(lat):
    try:
        return lat.split(' ', 1)[0]
    except IndexError:
        return ""

def cdr(lat):
    try:
        return lat.split(' ', 1)[1]
    except IndexError:
        return ""

def cons(stub, lat):
    if not lat:
        return stub
    return stub+" "+lat

def insr(old, new, lat):
    if lat == "":
        return
    else:
        if car(lat) == old:
            return cons(car(lat), cons(new, cdr(lat)))
        else:
            return cons(car(lat), insr(old,new,cdr(lat)))

def insl(old, new, lat):
    if lat == "":
        return
    else:
        if car(lat) == old:
            return cons(new, lat)
        else:
            return cons(car(lat), insl(old,new,cdr(lat)))

def minsl(old, new, lat):
    if lat == "":
        return
    else:
        if car(lat) == old:
            return cons(cons(new, old), minsl(old,new, cdr(lat)))
        else:
            return cons(car(lat), minsl(old,new,cdr(lat)))

def minsr(old, new, lat):
    if lat == "":
        return
    else:
        if car(lat) == old:
            return cons(cons(new, old), minsr(old,new, cdr(lat)))
        else:
            return cons(car(lat), minsr(old,new,cdr(lat)))

def subt(old, new, lat):
    if lat == "":
        return
    else:
        if car(lat) == old:
            return cons(new, cdr(lat))
        else:
            return cons(car(lat), subt(old,new,cdr(lat)))

def msubt(old, new, lat):
    if lat == "":
        return
    else:
        if car(lat) == old:
            return cons(new, msubt(old, new, cdr(lat)))
        else:
            return cons(car(lat), msubt(old,new,cdr(lat)))

if __name__ == "__main__":
    gg = "all this is this it"
    print gg
    '''
    print insr("this", "that", gg)
    print insl("this", "that", gg)
    print subt("this", "that", gg)
    print msubt("this", "that", gg)
    '''
    print insl("this", "that", gg)
    print minsl("this", "that", gg)
