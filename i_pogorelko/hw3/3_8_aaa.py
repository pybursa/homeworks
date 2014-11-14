text = "Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh"

text = text.replace(",","")
text = text.replace(".","")
text1 = text.split(" ")

prohibit = ['a', 'e', 'i', 'o', 'u', 'y']
n = 0


for i in text1:
    for j in range(len(i)):
        if (j == 0) or (j == (len(i) - 1)):
            pass
        elif "a" in i[j]:
            if ((i[j-1]) in prohibit) or ((i[j+1]) in prohibit):
                pass
            else:
                print 'n'+str(j+1), i[j], i
                n +=1
    #    else:
            #print 'j = ', j, 'i = ', i
print ''
print 'total number = ', n
#print text1
