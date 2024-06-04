#Task 1a

input_file = open("input1a.txt","r")
output_file = open("output1a.txt","w")
n = input_file.readline()
for i in range(int(n)):
  temp = int(input_file.readline())
  if temp%2 == 0:
    temstr = f"{temp} is an Even number.\n"
    output_file.write(temstr)
  elif temp%2 != 0:
    temstr = f"{temp} is an Odd number.\n"
    output_file.write(temstr)
input_file.close()
output_file.close()

'''''''''
Task 1a: The first input is the number of integers for which we need to define if its even or odd. 
We initiate a loop, read the files accordingly using proper sytax and that input number, turn it into an integer 
and eventually write it inside another output file.
'''''