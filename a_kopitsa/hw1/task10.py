def myfunction():
    name = raw_input("Please, enter your string: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    name = name.lower()
    count = 0
    for i in name:
        if(i in vowels):
            count += 1
    print "The string contains " + str(count) + " vowels"
    ask()


def ask():
    ifcontinue = raw_input("Continue? (yes/no) ")
    if(ifcontinue == "yes"):
        myfunction()
    elif(ifcontinue != "no"):
        print "Please, enter corrent answer."
        ask()

myfunction()

