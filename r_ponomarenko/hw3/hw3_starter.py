import utils
import os
import sys

first_sentence = "Proin eget tortor risus. " + \
    "Cras ultricies ligula sed magna dictum porta. " + \
    "Proin eget tortor risus. " + \
    "Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. " + \
    "Donec rutrum congue leo eget malesuada. "

second_sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " + \
    "Nulla quis lorem ut libero malesuada feugiat. " + \
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " + \
    "Donec rutrum congue leo eget malesuada. " + \
    "Cras ultricies ligula sed magna dictum porta."

def main():
    print utils.get_max_vowels(first_sentence)
    print 
    print utils.get_max_len(first_sentence)
    print 
    print utils.reverse(second_sentence)
    print 
    print utils.get_info_for_obj(os)
    print 
    print utils.get_info_for_obj(sys)
    print 
    print utils.get_pseudo_sum(124)
    print 
    print utils.get_primes(10000)

if __name__ == '__main__':
    main()