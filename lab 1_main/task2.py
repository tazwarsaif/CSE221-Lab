#Task 2 

input_file = open("input2.txt","r")
output_file = open("output2.txt","w")
def bubbleSort(arr):
  # flag = True
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        # flag = False
    # if flag == True:
    #   return
  return arr
arr = [2,5,7,9,1]
a = bubbleSort(arr)
print(a)
# print(arr)
# n = int(input_file.readline())
# lis1 = [int(i) for i in input_file.readline().split()]
# a = bubbleSort(lis1)
# for i in range(n):
#   output_file.write(f"{lis1[i]} ")
# input_file.close()
# output_file.close()

'''''''''
Task 2: For any sorting algorithm, the best case is if the array is sorted already. Here To use the bubble sort  
for the best case, we need to initiate a flag. If for the first iteration the condition of inner loop  
never fulfills then, we can easily say that the array is already sorted and we don't change the flag. Eventually, 
if the flag doesn't change, then we can easily return from there. The time complexity will be O(n) as the function 
returns after first iteration for the best case.
'''''