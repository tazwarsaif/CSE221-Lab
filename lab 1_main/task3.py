#Task 3

input_file = open("input3.txt","r")
output_file = open("output3.txt","w")
n = int(input_file.readline())
ids = [int(i) for i in input_file.readline().split(" ")]
marks = [int(i) for i in input_file.readline().split(" ")]
dict1 = {}
def selectionSort(arr):
  for i in range(len(arr)):
    intmax = i
    for j in range(i+1,len(arr)):
      if arr[j] > arr[intmax]:
        intmax = j
    temp = arr[intmax]
    arr[intmax] = arr[i]
    arr[i] = temp
def selectionSortformin(arr):
  for i in range(len(arr)):
    intmin = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[intmin]:
        intmin = j
    temp = arr[intmin]
    arr[intmin] = arr[i]
    arr[i] = temp


for i in range(n):
  if marks[i] not in dict1:
    dict1[marks[i]] = [ids[i]]
  else:
    dict1[marks[i]].append(ids[i])
lisKey = [i for i in dict1.keys()]
selectionSort(lisKey)
for i in lisKey:
  selectionSortformin(dict1[i])
  for j in dict1[i]:
    output_file.write(f"ID: {j} Mark: {i}\n")
input_file.close()
output_file.close()

'''''''''''
Task 3: We can form a dictionary using the marks as keys. 
We sort the keys in a descending order in a different list.
Then for looping that key-list, we ascend the ids and write our output accordingly. 
'''''''''