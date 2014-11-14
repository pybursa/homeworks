#hw 1/ task5/ Sergei Shybkoi

def typerr(x):
    print "typerr(",x,")==",type(x).__name__
    return

typerr(10)
typerr('asd')
typerr([1, 2, 3])
typerr(typerr)