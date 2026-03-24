# "dsa"
#  all the subset of string "dsa"
#1 " "
#2 "d" "s" "a"
#3 "ds" "da" "sa"
#4 "dsa" 

def subset(s,current="",index=0):
    if index==len(s):
        print(current)
        print("-----------------")
        return 
    
    subset(s,current+s[index],index+1)
    subset(s,current,index+1)


subset("dsa")    

