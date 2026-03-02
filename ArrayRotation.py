'''
Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output: arr[] = [3, 4, 5, 6, 7, 1, 2] 

''' 
#Function to reverse Array[]
def rverseArray(arr,d):
    c = arr[d:] + arr[:d] 
    return c

#Driver function to test the above function
arr =[1,2,3,4,5,6,7,8,9,10]
d = 2
result = rverseArray(arr,d) #calling the function
print("The Array Rotation is",result)
