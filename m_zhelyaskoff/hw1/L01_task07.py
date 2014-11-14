# -*- coding: cp1251 -*-

# Задание 7: уникальный набор.
# УСЛОВИЕ:
# Реализовать функцию, которая принимает список елементов и убирает
# из него все дубликаты (формирует список уникальных элементов).
# Сделать вариант с сохранением порядка следования элементов
# и вариант, в кот. сортировка элементов не принципиальна.
# Пример:
# а) assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")]
# б) assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]
# =========================================================================


print "==== Task 7: Unique Set  ===="
print 'INPUT: ["a", 5, 2, 5, (1, "a"), "a"]'

input_list = ["a", 5, 2, 5, (1, "a"), "a"]

def unique_ordered(arg):
    res = []
    for x in arg:
        if x in res:
            continue            
        res.append(x) 
    return res


def unique_disordered(arg):
    return list(set(arg))


print "unique_ordered:", unique_ordered(input_list)
print "unique_disordered:", unique_disordered(input_list)

raw_input()



        
            
            













