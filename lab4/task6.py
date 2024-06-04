import numpy as np
input_file = open("input6.txt","r")
output_file = open("output6.txt","w")

lis1 = [int(i) for i in input_file.readline().split(" ")]
r,c = lis1
matrix = np.empty((r,c),dtype=str)
maxd = 0
for i in range(r):
  str1 = input_file.readline()
  for j in range(len(str1)-1):
    matrix[i][j] = str1[j]

def dfs(row,col,matrix):
  if row < 0 or row >=len(matrix) or col < 0 or col >= len(matrix[0]):
    return 0
  if matrix[row][col] == "#":
    return 0
  total = 0
  if matrix[row][col] == "D":
    total += 1
  matrix[row][col] = "#"
  total += dfs(row+1,col,matrix)
  total += dfs(row,col+1,matrix) 
  total += dfs(row-1,col,matrix)
  total += dfs(row,col-1,matrix)
  return total

def traverse(matrix,r,c,maxd):
    for row in range(r):
        for col in range(c):
            if matrix[row][col] == ".":
                a= dfs(row,col,matrix)
                if a > maxd:
                    maxd = a
    return maxd    

output_file.write(f"{traverse(matrix,r,c,maxd)}")

input_file.close()
output_file.close()