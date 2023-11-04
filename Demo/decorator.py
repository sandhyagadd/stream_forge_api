###########Decorator###############
##Example 1
##def decore(fun):
##    def inner(a,b):
##        lsum = fun(a,b)
##        lfinal = lsum+10
##        return lfinal
##    return inner
##        
##
##
##@decore
##def add(a,b):
##    return a+b
##
##
##x = add(2,5)
##print("Result: ", x)


##example 2
##def decore(fun):
##    def inner(a,b):
##        result = fun()
##        get_updated_num = result+a+b
##        return get_updated_num
##    return inner
##
##@decore
##def get_num():
##    return 10
##
##
##x = get_num(10,20)
##print(x)


##def decore_fun(fun,x):
##    temp = fun(x)
##    return temp
##    
##
##def add(x):
##    return x + 1
##
##
##def sub(x):
##     return x - 1
##
##
##add_res = decore_fun(add,10)
##print("Add fun called: ",add_res)
##
##sub_res = decore_fun(sub,20)
##print("Add fun called: ",sub_res)


def decore_fun(fun):
    def inner(a, b):
        if a<b:
            a, b = b,a
        return fun(a,b)
    return inner


@decore_fun
def div(a,b):
    return a/b





div_result = div(2,10)
print("div_result:: ", div_result)


























