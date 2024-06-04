import numpy as np
input_file = open("input1.txt","r")
output_file = open("output1b.txt","w")

tmplis = [int(i) for i in input_file.readline().split(" ")]
n,l = tmplis
adjlis = {}

for i in range(l+1):
    adjlis[i] = []

for i in range(l):
    tempo = [int(i) for i in input_file.readline().split(" ")]
    if tempo[0] not in adjlis.keys():
        adjlis[tempo[0]] = [(tempo[1],tempo[2])]
    else:
        adjlis[tempo[0]].append((tempo[1],tempo[2]))


output_file.write(f"{adjlis}")

input_file.close()
output_file.close()