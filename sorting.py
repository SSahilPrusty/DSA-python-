'''the process of arranging data into meaninfull oredr so that you can analzye it more effecitvely'''
#---------------BUBBLE SORT--------------------
'''comparision based adjustment based on the element and we have to move the largest elementto the right '''
#CODE
def bubble_sort(arr):
    n=len(arr)
    for i in range (n-1):
        for j in range (n-1-i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
#above code will run n to square time irrestive if the code is alredy sorted, so improved code             
def bubble_sort_enchaed(arr) :
    def bubble_sort(arr):
     n=len(arr)
     
     for i in range (n-1):
        sorted = True
        for j in range (n-1-i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j] 
        if sorted:
         break                                     

arr=[1,5,3,7,2,8,9,4,6] 
arr1=[1,2,3,4,5,6,7,8,9]         
bubble_sort(arr) 
print("bubble sort")
print(arr)  
bubble_sort_enchaed(arr1) 
print("bubble sort enchaed")
print(arr1)  
bubble_sort_enchaed(arr) 
print("bubble sort enchaed")
print(arr)  

#the code give us a stable sorted array