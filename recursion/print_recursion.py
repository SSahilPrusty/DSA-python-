#printing n to 1
def funcn(n):
    # Base Case
    if n == 0:
        return
    
    # Work
    print(n)
    
    # Recursive Call
    funcn(n - 1)

def func1(n):
    if n>0:
        func1(n-1)   #for n to 1 just reverse the 15 no and 16 no line of code 
        print(n)



print(func1(5))
