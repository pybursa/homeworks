start_list = [1,4,8,6,3,7,1]

for i in range(len(start_list)):
    for j in range(len(start_list)):
        if start_list[j] > start_list[i]:
            start_list[i], start_list[j] = start_list[j], start_list[i]
        if start_list[i]%2 !=0 and start_list[j]%2 ==0:
            start_list[i], start_list[j] = start_list[j], start_list[i]
        if start_list[i]%2 ==0 and start_list[j]%2 ==0 and start_list[i] > start_list[j]:
            start_list[i], start_list[j] = start_list[j], start_list[i]
            

        
print start_list
