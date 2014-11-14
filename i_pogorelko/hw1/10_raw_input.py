def main_ask():
    test_string2 = ""
    while True:
        if test_string2 == "":
            test_string2 = raw_input("Continue? (yes/no): ")

        if test_string2 == "yes":
            print "Okay!"
            main_question()
            main_ask()
            return False
        elif test_string2 == "no":
            print "OK! It was nice to count your vowels!"
            return False
            quit
        else:
            test_string2 = raw_input("Please, enter corrent answer. Continue? (yes/no): ")
            #return False


def main_question():
    while True:
        
        test_string = raw_input("Please, enter your string: ")
        l  = test_string.lower()
        vocal_num = 0
        for i in l:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                vocal_num +=1

        if vocal_num > 0:    
            print "The string contains ", vocal_num, "lowels"
            return False
        else:
            print "The string doesn't contain vowels"
            return False

main_question()
main_ask()


    
