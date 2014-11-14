def myfunction(s):
    for i in s:
        if(s.count(i) >= 2):
            s.remove(i)
    print s
    s.sort()
    print s
myfunction(["a", 5, 2, 5, (1, "a"), "a"])
