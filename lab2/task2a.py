input_file =  open("input2a.txt","r")
output_file = open("output2a.txt","w")

n1 = int(input_file.readline())
lis1 = [int(i) for i in input_file.readline().split(" ")]
n2 = int(input_file.readline())
lis2 = [int(i) for i in input_file.readline().split(" ")]

lismain = lis1+lis2
lismain.sort()
output_file.write(f"{lismain}")


input_file.close()
output_file.close()

#Task2a: Here we need to sort a merged array in nlogn time complexity
#So we merge the array and use .sort() to find our result.