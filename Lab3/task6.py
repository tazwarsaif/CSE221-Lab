input_file =  open("input6.txt","r")
output_file = open("output6.txt","w")


def findkth(arr,start,end,kth):
    q = Partition(arr,start,end)
    if q == kth:
        return arr[q]
    elif q < kth:
        return findkth(arr,q+1,end,kth)
    elif q > kth:
        return findkth(arr,start,q-1,kth)


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

l = int(input_file.readline().split(" ")[0])
arr = [int(i) for i in input_file.readline().split(" ")]
queries = int(input_file.readline().split(" ")[0])
for i in range(queries):
    output_file.write(f"{findkth(arr,0,l-1,int(input_file.readline())-1)}\n")
input_file.close()
output_file.close()


#task 6: To find the kth smallest value we need to use the partition function. Basing the index found from the partition function we 
#check the index number accordingly. If we dont find the actual index, we recursively call again the function until we finally do. That
#indexed value will be our expected output. 