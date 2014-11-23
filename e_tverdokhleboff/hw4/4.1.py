# -*- coding: utf-8 -*-
""" Задание 1: Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные
приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта
буква встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec
rutrum congue leo eget malesuada.
"""

text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
Donec rutrum congue leo eget malesuada.'
text = "aab+-*b ."
low_text = text.lower()
all_letters = len(text) - text.count(' ') - text.count('.') + 0.0
uniq_symbols = list(set(text.lower()))
uniq_symbols.remove(' ')
uniq_symbols.remove('.')
percents = []
for i in uniq_symbols:
    c = low_text.count(i) / all_letters * 100
    percents.append(round(c, 1))
res_dict = dict(zip(uniq_symbols, percents))
print res_dict
