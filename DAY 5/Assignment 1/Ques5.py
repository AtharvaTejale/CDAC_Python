list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
k=(len(list2)-1)
for i in range(len(list1)):
    print(list1[i],list2[k],sep=" ",)
    k = k-1