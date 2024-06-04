input_file =  open("input4.txt","r")
output_file = open("output4.txt","w")

def sortalgo(arr):
    for i in range(len(arr)):
        temidx = i
        for j in range(i+1,len(arr)):
            if arr[j][-1] < arr[temidx][-1]:
                temidx = j
        temp = arr[i]
        arr[i] = arr[temidx]
        arr[temidx] = temp

tempo = input_file.readline().split(" ")
task,man=int(tempo[0]),int(tempo[1])
listask = []

for i in range(task):
    listask.append([int(i) for i in input_file.readline().split(" ")])

sortalgo(listask)
print(listask)
current_pairs = [[0,0]]*man
iter = 0
tc = False
n = 0
for i in range(len(listask)):
    for j in range(len(current_pairs)):
        if listask[i][0] - current_pairs[j][-1] == 0:
            tc = True
            iter += 1
            current_pairs[j] = listask[i]
            break
        elif current_pairs[j] == [0,0]:
            current_pairs[j] = listask[i]
            n += 1
            break
    if n == man:
        break
count = len(current_pairs) + iter
if tc == False:
    current_pairs = [listask[i] for i in range(man)]
print(listask)
print(current_pairs)

for i in range(len(current_pairs),len(listask)):
    temcount = 0
    temlis = []
    for k in range(len(current_pairs)):
        if listask[i][0]>=current_pairs[k][1]:
            temcount += 1
            temlis.append(k)
    if len(temlis) == 1:
        current_pairs[temlis[0]] = listask[i]
        count += 1
    elif len(temlis) == 0:
        pass
    else:
        compare = listask[i][0] - current_pairs[temlis[0]][-1] 
        idx = 0
        for j in range(1,len(temlis)):
            if listask[i][0]-current_pairs[temlis[j]][-1]   <= compare:
                compare = listask[i][0]-current_pairs[temlis[j]][-1]
                idx = j
        current_pairs[temlis[idx]] = listask[i]
        count += 1
    print(current_pairs)
output_file.write(f"{count}")

input_file.close()
output_file.close()

#Task4: Firstly, we sort all the tasks like our previous task. Then, we initialize an array
#with all the individual having their own task slot. Here we can not assign random tasks for
# all the individuals, we need to calculate the maximum one. To make a proper current pair array,
#Then we compare all the start time of list task with the current pairs end. Eventually, we get
#our maximum output.