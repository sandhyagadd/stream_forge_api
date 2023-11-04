def addition(n):
    return n+n

##number = [1,2,3,4,5]
##result = map(addition, number)
##print(list(result))




def lambda_fun(n):
    return lambda n:n+10


a = lambda_fun(10)
##print(a(20))
##print(a(30))

number = (10,20,30,40)

result = map(lambda n:n+10, number)
##print(list(result))

##result = map(lambda_fun, number)
##
##print(list(result))


a = [1,4,7]
b = [2,5,8]

result = map(lambda x,y: x+y, a, b)
print(list(result))

