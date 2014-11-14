#!usr/bin/python

#my_string=raw_input("Please enter a string: ")
my_string="sabrrtuwacaddabra"


def find_longest_substring_in_alphabetical_order(s):
    groups = []
    cur_longest = ''
    prev_char = ''
    for c in s.lower():
        if prev_char and c < prev_char:
            groups.append(cur_longest)
            cur_longest = c
        else:
            cur_longest += c
        prev_char = c
    return max(groups, key=len)


print find_longest_substring_in_alphabetical_order(my_string)