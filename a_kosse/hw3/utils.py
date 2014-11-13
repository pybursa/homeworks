def get_discr(a,b,c):
    d = b * b - 4 * a * c
    return d

def get_eq_root(a,b,c,order=1):
    if order == 1:
        x = (-b + d ** (1/2.0)) / (2 * a)
    else:
        x = (-b + d ** (1/2.0)) / (2 * a)
    return x

def input_parametr(parametr_name):
    while True:
        a = raw_input("Enter th parameter of the equation: %s = "
            % parametr_name)
        if a.replace('.','').isdigit() and float(a) != 0:
            return float(a)
        else:
            print "repeat..."

def input_text():
    a = raw_input("Enter the text. (Empty string == default text): ")
    if not a:
        a = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada"""
#        a = "Mama mila ramu. A dolzna bila mit okno"
    return a

def consonants():
    cons = []
    for i in range(ord('a'), ord('z')+1):
        cons.append(chr(i))
    cons.remove("a")
    cons.remove('e')
    cons.remove('i')
    cons.remove("o")
    cons.remove('u')
    cons.remove('y')
    return ''.join(cons)

