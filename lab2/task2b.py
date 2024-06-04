input_file =  open("input2b.txt","r")
output_file = open("output2b.txt","w")

n1 = int(input_file.readline())
lis1 = [int(i) for i in input_file.readline().split(" ")]
n2 = int(input_file.readline())
lis2 = [int(i) for i in input_file.readline().split(" ")]

mainlis = [0]*(n1+n2)

mainiterate = 0
i1 = 0
i2 = 0

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
    elif lis1[i1] <= lis2[i2]:
        mainlis[mainiterate] = lis1[i1]
        i1 += 1
    mainiterate += 1

for i in mainlis:
    output_file.write(f"{str(i)} ")

input_file.close()
output_file.close()

#task 2b: Here we initiate 2 pointers for both of the arrays and another one for
#the merged array for which we used an empty array.
#We compare the data with the iterators and change them accordingly, we insert those
#values in the empty array and find our output. Here we are doing everything in one loop.
#Therefore, timecomplexity becomes O(n).