def largest(arr,num):

    max= arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max    


arr = [10,324,45,90,9808]
num = len(arr)
result = largest(arr,num)
print ("The largest number in the given array is ",result)

''''
Working Example with Your Array:
Initialize max to arr[0] = 10.
Loop starts from i = 1 and goes through the array:
For i = 1, arr[1] = 324. Since 324 > 10, max = 324.
For i = 2, arr[2] = 45. 45 is not greater than 324, so max remains 324.
For i = 3, arr[3] = 90. 90 is not greater than 324, so max remains 324.
For i = 4, arr[4] = 9808. Since 9808 > 324, max = 9808.
After the loop finishes, max = 9808, and the function returns 9808.'

'''

#Second way to solve this problem.
arr = [10,324,45,90,9808]
arr.sort()
print(arr[-1])
