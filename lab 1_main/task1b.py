#Task 1b

input_file = open("input1b.txt","r")
output_file = open("output1b.txt","w")
n = input_file.readline()
for i in range(int(n)):
  temp = input_file.readline().split(" ")
  if temp[2] == "+":
    num = (int(temp[1])+int(temp[-1]))
  elif temp[2] == "*":
    num = (int(temp[1])*int(temp[-1]))
  elif temp[2] == "/":
    num = (int(temp[1])/int(temp[-1]))
  elif temp[2] == "-":
    num = (int(temp[1])-int(temp[-1]))
  output_file.write(f"The result of {temp[1]} {temp[2]} {temp[3].strip()} is {num}")
  output_file.write("\n")
input_file.close()
output_file.close()

'''''''''''
Task 1b: Just like the previous task, we initiate a loop after reading the first line. 
For every iteration we read lines, split the lines and according to the middle
element we do the operation for the both integers.
'''''
