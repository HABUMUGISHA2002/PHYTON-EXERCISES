def perfect(num) :
    my_list=[]
    for i in range(1,num) :
        sum=0
        for j in range (1,i) :
            if i%j==0 :
                sum+=j
        if sum==i :
            my_list.append(i)
    return my_list
a=perfect(10000)
print(a)