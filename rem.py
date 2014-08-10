from ins import *

def rem(tok, string):
    if not string:
        return
    else:
        if(car(string) == tok):
            return cdr(string)
        else:
            return cons(car(string), rem(tok, cdr(string)))

def mrem(tok, string):
    if not string:
        return
    else:
        if(car(string) == tok):
            return mrem(tok, cdr(string))
        else:
            return cons(car(string), mrem(tok, cdr(string)))


print rem("it", "this is it and it also")
print mrem("it", "this is it and it also")
