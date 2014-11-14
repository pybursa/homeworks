from collections import deque

# Recursive reversion.
# @param str text Text to revers.
# @return str
def reverse_1(text):
    if len(text) <= 1:
        return text
    return reverse_1(text[1:]) + text[0]

c = "ecnalubma"
print reverse_1(c)

# Second version reversion.
# @param str text Text to revers.
# @return str
def reverse_2(text):
    d = deque()
    d.extendleft(text)
    return ''.join(d)

d = "ecnalubma"
print reverse_2(d)

# Third reversion.
a = "ecnalubma"
a_reversed = a[::-1] 
print a_reversed

# Fourth embodiment reversion
b = "ecnalubma"
print ''.join([b[i] for i in xrange(len(b)-1, -1, -1)])


