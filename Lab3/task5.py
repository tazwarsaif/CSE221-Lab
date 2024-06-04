input_file = open("input5.txt","r")
output_file = open("output5.txt","w")


def QuickSort(arr,start,end):
    if end <= start:
        return
    q = Partition(arr,start,end)
    QuickSort(arr,start,q-1)
    QuickSort(arr,q+1,end)

def Partition(arr,start,end):
    pivot = arr[end]
    i = start-1
    j = start
    while True:
        if j == end:
            i += 1
            temp = arr[i]
            arr[i] = arr[end]
            arr[j] = temp
            break
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1
    return i


l = int(input_file.readline())
arr = [int(i) for i in input_file.readline().split(" ")]
QuickSort(arr,0,l-1)
str1 = ""
for i in arr:
    str1 += str(i) + " "
output_file.write(f"{str1}")

output_file.close()
input_file.close()


#Task 5
#The main QuickSort Function mainly recieves the the value from Partition function and recursively calls again with the same array without
#the index found from partion function. In the Partition fuction, we select a pivot and according to that pivot we leave all the smaller 
#elements on the left and larger or equal ones to the right. Then we reuturn the index of the pivot. This whole this is a kind of inplace sort.