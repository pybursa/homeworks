__author__ = 'maln'

#string
str = "sabrrtuwacaddabra"

length = len(str)

#counters
cnt = 1
cnt_max = 0
end_of_sequence = 0

for i in range(length-1):
    if str[i+1] >= str[i]:
        cnt = cnt + 1
        print str[i]
    else:
        print str[i]
        print('-----')
        if cnt > cnt_max:
            cnt_max = cnt
            end_of_sequence = i
        cnt = 1
print 'Count max: {} with text "{}!"'.format(cnt_max, str[end_of_sequence-cnt_max + 1:cnt_max + 1])

