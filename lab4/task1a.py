import numpy as np
input_file = open("input1.txt","r")
output_file = open("output1a.txt","w")

lis1 = [int(i) for i in input_file.readline().split(" ")]
l = lis1[0]
matrix = np.zeros((l+1,l+1),dtype=int)
for i in range(lis1[1]):
  temp = [int(i) for i in input_file.readline().split(" ")]
  matrix[temp[0]][temp[1]] = temp[-1]
  
output_file.write(f"{matrix}")

input_file.close()
output_file.close()