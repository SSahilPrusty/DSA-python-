'''function calling itself is called recursion
steps:-
1)base condition
2)logic/recursive call
3)recursive call/ logic'''
def print_(arr,si):
 #base conditon 
 if(si>=len(arr)):
  return
 #logic
 print(arr[si])
 #recursive call
 print_(arr,(si+1))

def print_revers(arr,si):
 #base conditon 
 if(si>=len(arr)):
  return
 #recursive call
 print_revers(arr,si+1)
 #logic
 print(arr[si])

arr=[1,2,3,4,5,6,7,8,9]
print("array")
print_(arr,0) 
print("reversed array")
print_revers(arr,0)
