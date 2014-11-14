__author__ = 'alex'


def task_22():

    def check_reverse(string):
        if string == string[::-1]:
            return True
        else:
            return False

    string21 = "abba"
    string22 = "arbat"

    print string21 + " " + string21[::-1] + " " + str(check_reverse(string21))
    print string22 + " " + string22[::-1] + " " + str(check_reverse(string22))


task_22()
