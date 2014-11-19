# -*- coding: utf8 -*-

u"""
Отображает разницу в поведении старых классов и классов нового стиля
(object-based).

Попробуйте попереключаться (перекомментировать строки 17/18) и сравнить
принты в конце модуля.

Обратите внимание на вывод атрибута "z".
Какие выводы из этого можно сделать?
"""

__author__ = 'wowkalucky'


# class A(object):
class A():
    x = "Ax"
    y = "Ay"
    z = "Az", "old-style classes"


class B(A):
    """B class definition"""
    x = "Bx"
    y = "By"


class C(A):
    x = "Cx"
    y = "Cy"
    z = "Cz", "new-style classes"

class D(B, C):
    x = "Dx"


obj = D()


print obj.x
print obj.y
print obj.z
print "+" * 79


print dir(obj)
print obj.__dict__
print D.__dict__
print C.__dict__
print B.__dict__
print A.__dict__
print "+" * 79


print obj.__class__
print D.__bases__
print type(obj)
print type(D)
print getattr(D, "__mro__", None)     # new style classes only


