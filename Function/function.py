#import strin
#print(strin. f(1))

def new_string(symbol,count = 3):
    return symbol*count
print(new_string('!',5))  #!!!!!
print(new_string('!'))    #!!!
print(new_string(4))      #12

def concatenation (*params):
    res:str=""
    for item in params:
        res+=item
    return res
print(concatenation('a','b','c','d'))
print(concatenation('a','1','b','3'))

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)
list=[]
for e in range(1,10):
    list.append(fib(e))
print(list)    
