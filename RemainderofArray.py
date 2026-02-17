#Python Program for Find remainder of array multiplication divided by n

'''
input: arr[] = {100, 10, 5, 25, 35, 14}, 
            n = 11
Output: 9

'''
def Remainder(arr):
    multiple = 1
    for i in arr:
        multiple = multiple * i
    return multiple % 11

#Initializing the value and calling the function..    
arr = [100, 10, 5, 25, 35, 14]
result= Remainder(arr)
print("Remainder of given Arrays:", result)
