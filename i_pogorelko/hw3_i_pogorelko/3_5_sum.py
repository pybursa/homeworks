def summa():
    while True:
        a = raw_input("enter a digit: ")

        if a.isdigit():
            print a
            sum = 0
            for i in a:
                sum = sum + int(i)
            print 'sum = ', sum

            ask = raw_input("do you want to continue?(yes/no): ")
            ask = ask.lower()
            while True:
                if ask == 'yes':
                    print 'OK!'
                    break
                elif ask == 'no':
                    print 'OK! Good bye'
                    return False
                else:
                    ask =  raw_input('you enter not correct answer.please write\
again(yes/no):')
        
        else:
            print 'this is not digit. please input again'
summa()
