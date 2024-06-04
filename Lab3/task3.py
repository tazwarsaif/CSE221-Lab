input_file = open("input3.txt","r")
output_file = open("output3.txt","w")

def find_count(arr):
    if len(arr) <= 1:
        return arr,0
    mid = len(arr)//2
    lp,lc = find_count(arr[:mid])
    rp,rc = find_count(arr[mid:])
    sortedArr, maincount = merge(lp,rp)
    total = lc + rc + maincount
    return sortedArr,total


def merge(lis1,lis2):
    n1,n2 = len(lis1),len(lis2)
    mainlis = [0]*(n1+n2)
    mainiterate = 0
    i1 = 0
    i2 = 0
    count = 0
    while True:
        if mainiterate == len(mainlis):
            break
        if i2 >= len(lis2):
            mainlis[mainiterate] = lis1[i1]
            i1 += 1
            mainiterate += 1
            continue
        elif  i1 >= len(lis1):
            mainlis[mainiterate] = lis2[i2]
            i2 += 1
            mainiterate += 1
            continue
        elif lis1[i1] >= lis2[i2]:
            mainlis[mainiterate] = lis2[i2]
            i2 += 1
            count += len(lis1)-i1 
            #As both of the arrays are sorted, after this condition, 
            #the remaining elemnts of left array are also greater than that number too.
            #that's why we not only increase for that element on the left, 
            #we increase the count number for the rest of the 
            #array too.
        elif lis1[i1] <= lis2[i2]:
            mainlis[mainiterate] = lis1[i1]
            i1 += 1
        mainiterate += 1
    return mainlis,count
l = int(input_file.readline())
arr = [int(i) for i in input_file.readline().split(" ")]
output_file.write(f"{find_count(arr)[1]}")

output_file.close()
input_file.close()

#Task 3:
#The main topic of the task was to get the expected value using the inversion process. This process says that
#if we are comparing two numbers of two different array, if a number is greater than that number will also be
#greater for the rest of that array element too. However, we need to ensure both of the arrays are sorted.
#This task is very similar to merge sort with an extra step to track the numbers that are eventually less.