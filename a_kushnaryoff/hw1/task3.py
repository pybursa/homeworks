__author__ = 'alex'


def task_3():
    def my_count(st, subst):
        string_size = len(st)
        substring_size = len(subst)
        count = 0
        for i in range(0, string_size - substring_size + 1):
            if st[i:i+substring_size] == subst:
                count += 1
        return count

    st = raw_input("Enter your string: ")
    subst = raw_input("Enter your substring: ")
    print "Result: " + str(my_count(st, subst))


task_3()
