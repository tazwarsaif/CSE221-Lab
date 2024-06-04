input_file = open("input1.txt","r")
output_file = open("output1.txt","w")



def merge(a, b):    
    mainlis = [0]*(len(a)+len(b))
    mainiterate = 0
    i1 = 0
    i2 = 0

    while True:
        if mainiterate == len(mainlis):
            break
        if i2 >= len(b):
            mainlis[mainiterate] = a[i1]
            i1 += 1
            mainiterate += 1
            continue
        elif  i1 >= len(a):
            mainlis[mainiterate] = b[i2]
            i2 += 1
            mainiterate += 1
            continue
        elif a[i1] >= b[i2]:
            mainlis[mainiterate] = b[i2]
            i2 += 1
        elif a[i1] <= b[i2]:
            mainlis[mainiterate] = a[i1]
            i1 += 1
        mainiterate += 1
    return mainlis



def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])   
        a2 = mergeSort(arr[mid:])  
        return merge(a1, a2)          

l = input_file.readline()
arr = [int(i) for i in input_file.readline().split(" ")]

Sorted = mergeSort(arr)
str1 = ""

for i in Sorted:
    str1 += str(i) + " "

output_file.write(str1)

input_file.close()
output_file.close()

#Task 1:
#Here the main fucntion is mergeSort and it is used as to the divide
#and conquer part in the code. We divied the array into two different part
#then give those to another sorting function. That function returns a sorted 
#merged array. In the merge function we used 3 pointers to iterate over the three
#array based on proper condition. The whole thing is processed recusively.
