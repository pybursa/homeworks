__author__ = 'm_shalamov'


def palindrome(str_sample):
    if type(str_sample) is str:
        if str_sample == str_sample[::-1]:
            return True
        else:
            return False
    else:
        return "Unsupported object type"


if __name__ == '__main__':
    print palindrome('abba')
    print palindrome('abab')
    print palindrome([1, 2, 3])