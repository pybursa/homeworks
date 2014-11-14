vowel_num = []

def count_vowels(i):
    num = i.lower().count('a') + i.lower().count('e') + i.lower().count('i') + i.lower().count('o') + i.lower().count('u') + i.lower().count('y')
    return num

def main():
    text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
    for i in (text.split(' ')):
        vowel = count_vowels(i)
        vowel_num.extend([vowel])
        print i, "-", vowel
    print "Max number of vowels -", max(vowel_num)

main()
