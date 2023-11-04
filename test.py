##lst = []
##
##for i in range(10):
##    lst.append(i)
##
##print(lst)
##print(type(lst))
##
##ltuple = tuple(lst)
##print(ltuple)
##print(type(ltuple))


##std = ['saurabh', 'saurabh', 'Saurabh', 'Rahul', 'rahul', 3,4,3,100,2]
##
##
##print(type(std))
##
##lset = set(std)
##print(lset)


##lst = [45,65,21,12,50,5]
##sort_list= lst.sort()
##print(sort_list)
##print(lst)



##lst = [45,65,21,12,50,5]
##sort_list = []
##temp = 0
##
##for i in range(0,len(lst)):
##    for j in range(i+1, len(lst)):
##        if lst[i] > lst[j]:
##            temp = lst[i]
##            lst[i] = lst[j]
##            lst[j] = temp
##
##print(lst)


N = int(input("Enter a number: ").strip())

if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")

##if N % 2 != 0:
##    print ("Weird")
##else:
##    if N >= 2 and N <= 5:
##        print ("Not Weird")
##    elif N >= 6 and N <= 20:
##        print ("Weird")
##    elif N > 20:
##        print ("Not Weird")    

    
    
    



























    

