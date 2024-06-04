input_file = open("input4.txt","r")
output_file = open("output4.txt","w")
n = input_file.readline()
dict1 = {}
list1 = []
def lettersort(arr):
  for i in range(len(arr)):
    letmin = i
    for j in range(i+1,len(arr)):
      if arr[letmin] > arr[j]:
        letmin = j
    temp = arr[letmin]
    arr[letmin] = arr[i]
    arr[i] = temp
for i in range(int(n)):
  temp = input_file.readline().split(" ")
  if temp[0] not in list1:
    list1.append(temp[0])
  if temp[0] not in dict1:
    dict1[temp[0]] = [temp]
  else:
    dict1[temp[0]].append(temp)
lettersort(list1)
for i in list1:
  for j in dict1[i]:
    temp = int("".join(j[-1].split(":")))
    j[-1] = temp
def sortlistime(arr):
  for i in range(len(arr)):
    tempmax = i
    for j in range(i+1,len(arr)):
      if arr[tempmax][-1] < arr[j][-1]:
        tempmax = j
    tempo = arr[tempmax]
    arr[tempmax] = arr[i]
    arr[i] = tempo

for i in list1:
  sortlistime(dict1[i])
  for j in dict1[i]:
    some = str(j[-1])
    if len(str(j[-1])) == 4:
      j[-1] = f"{some[:2]}:{some[2:]}."
    elif len(str(j[-1])) == 3:
      j[-1] = f"0{some[:1]}:{some[1:]}."
    elif len(str(j[-1])) == 2:
      j[-1] = f"00:{some}."
    elif len(some) == 1:
      j[-1] = f"00:0{some}."
    output_file.write(" ".join(j))
    output_file.write("\n")
input_file.close()
output_file.close()

'''''''''
Task 4: A dictionary is made to store the name as keys and splitted string as values.
The keys are sorted in different list. Corresponding values are iterated using the sorted key-array.
Meanwhile those splitted element's last values were replaced by actual integers from string. 
Using those numbers and index we sort all the values in a descending order in that array.
Eventually, we write the output using that list elements accordingly. 
'''