# coding=utf-8

while 1:
    try:
        num = int(raw_input("Enter natural digit:\n"))
        break
    except ValueError:
        print "Enter natural digit."
summ = 0

for i in list(str(num)):
    summ = add(summ, int(num))
print summ
# не знаю почему, но код не работает. оператор add нашел здесь https://docs.python.org/2/library/operator.html
