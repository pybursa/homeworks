__author__ = 'm_shalamov'

s = "hApPyHalLOweEn!"

chars_list = list(s)

reference = ['a', 'e', 'i', 'o', 'u']

result = 0

for char_item in chars_list:
    if str(char_item).lower() in reference:
        result += 1

print result