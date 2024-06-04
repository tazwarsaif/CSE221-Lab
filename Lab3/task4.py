input_file = open("input4.txt","r")
output_file = open("output4.txt","w")

def max1(arr,s,e):
    if s == e:
        return s
    mid = (s+e)//2
    num1 = max1(arr,s,mid)
    num2 = max1(arr,mid+1,e)
    if abs(arr[num1]) > abs(arr[num2]):
        return num1
    elif abs(arr[num2]) > abs(arr[num1]):
        return num2
    elif abs(arr[num1]) == abs(arr[num2]):
        return max(num1,num2)
def max2(arr,s1,e1,maxed):
    if s1 == e1:
        return s1
    mid1 = (s1+e1)//2
    num1 = max2(arr,s1,mid1,maxed)
    num2 = max2(arr,mid1+1,e1,maxed)
    if (num1 != None and (arr[num1]) > (arr[num2]) and num1 != maxed):
        return num1
    elif (num2 != None and (arr[num1]) < (arr[num2]) and num2 != maxed):
        return num2
    elif num2 == maxed:
        return num1
    elif num1 == maxed:
        return num2

l = int(input_file.readline())
arr = [int(i) for i in input_file.readline().split(" ")]

first = max1(arr,0,l-1)
if first == 0:
    second = max2(arr,first+1,l-1,first)
    output_file.write(f"{arr[first]+arr[second]**2}")
else:
    second = max2(arr,0,first-1,first)
    output_file.write(f"{arr[second]+arr[first]**2}")

output_file.close()
input_file.close()

#Task 4:
#In the formula we can easily see that the best case is always depending of
#A[j]. So whatever is A[j] is, we need to search for the absolute greatest number.
#As per the condition, we need to find any j for any i where i<j.
#So where we find the greatest value of A[j] we need to find the second maximum
#value within the index j of that array. However, if the gratest number is found in 
#index 0, we will assign it to the value of A[i] and find A[j] within the rest of the array