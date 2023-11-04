##lst = [5,8,4,6,9,2]
##n = 9

##for i in lst:
##    if i == n:
##        print(lst.index(i))
##        print("found")

pos = -1 
def linear_search(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i +=1
    return False

if __name__ == "__main__" :

    l = [2,8,9,4,10,50]
    find = 100
    result = linear_search(l,find)
    if result:
        print(f"Find_status: {result} and position or index is {pos}")
    else:
        print("Not found")
    
