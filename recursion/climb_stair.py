
def climb_stairs(n):
    if n==0:
        return 0
    elif n<=3:
        return n
    else:
        return (climb_stairs(n-1)+climb_stairs(n-2))
    


print(climb_stairs(4)  )  