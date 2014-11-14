# only works on lists of lists
def flatten(l):
    return sum(l, [])

print flatten([[1,2,3],[4,5,6], [7], [8,9]])