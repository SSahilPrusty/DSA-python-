def func(n):
    # Base Case
    if n == 0:
        return
    
    # Work
    print(n)
    
    # Recursive Call
    func(n - 1)




print(func(5))