a = "Proin eget tortor risus . Cras ultricies ligula sed magna dictum porta . Proin eget tortor risus . Curabitur non nulla sit amet nisl tempus convallis quis ac lectus . Donec rutrum congue leo eget malesuada .".split()
b = "aeiou"
b = [sum(k in b for k in word) for word in a]
print max(b)
