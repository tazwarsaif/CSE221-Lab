input_file =  open("input3.txt","r")
output_file = open("output3.txt","w")

def sortalgo(arr):
    for i in range(len(arr)):
        temidx = i
        for j in range(i+1,len(arr)):
            if arr[j][-1] < arr[temidx][-1]:
                temidx = j
        temp = arr[i]
        arr[i] = arr[temidx]
        arr[temidx] = temp
n = int(input_file.readline())
lis = [None]*n
for i in range(n):
    temp = [int(i) for i in input_file.readline().split(" ")]
    lis[i] = temp

sortalgo(lis)

count = 1
tempo = lis[0]
mainlis = [tempo]
for i in range(1,len(lis)):
    time = lis[i][0]
    if time >= tempo[-1]:
        count += 1
        tempo = lis[i]
        mainlis.append(lis[i])

output_file.write(f"{count}")
output_file.write("\n")
for tup in mainlis:
    output_file.write(f"{tup[0]} {tup[1]}\n")
input_file.close()
output_file.close()

#Task 3: Firstly, we sort all the tasks using the end hour of every task in ascending order.
#We store a current pair from the task list, compare if the current pair's last elemnt
#is lesser or equal than the next task. If it is, we store the tasks and increase our count.
