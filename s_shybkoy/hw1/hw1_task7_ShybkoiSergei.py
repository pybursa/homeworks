#hw 1/ task7/ Sergei Shybkoi

def unique(l, initial_order):
    try:
        res = list([l[0]])
    except IndexError:
        print "No list!"
        return
    for x in l:
        if x not in res:
            res.append(x)
    if not initial_order:
        res.sort()
    print res, "ordered: ", initial_order
    return

ls = [7, 1, 1, 'dfg', 'a', (1, 'a'), 'dfg']
print "Initial list: ", ls
unique(ls, False)
unique(ls, True)