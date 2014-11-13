__author__ = 'andrey'

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. " \
       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. " \
       "Cras ultricies ligula sed magna dictum porta."



def myfunction(var):
    new = []
    for i in var.split(".")[::-1]:
        for a in i.split(" ")[::-1]:
            new.append(a[::-1])
    print " ".join(new)

myfunction(text)

print text[::-1]