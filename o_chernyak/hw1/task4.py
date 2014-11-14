s = 'sabrrtuwacaddabra'

curindex = 1

startindex = 0


result = s[startindex]

sb = s[startindex]


while curindex < len(s):

    if s[startindex] <= s[curindex]:

        sb += s[curindex]

    elif s[curindex] < s[startindex]:

        sb = s[curindex]

    if len(sb) > len(result):

        result = sb

    curindex += 1

    startindex += 1



print result
