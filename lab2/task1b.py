input_file =  open("input1b.txt","r")
output_file = open("output1b.txt","w")
temp = input_file.readline().split(" ")
l,ten = int(temp[0]),int(temp[1])
lis = [int(i) for i in input_file.readline().split(" ")]
p1,p2 = 0,l-1
flag = False
while p1<p2:
    if lis[p1] + lis[p2] == ten:
        output_file.write(f"{p1+1} {p2+1}")
        flag = True
        break
    if lis[p1] + lis[p2] > ten:
        p2 -=1
    elif lis[p1] + lis[p2] < ten:
        p1 += 2
if flag == False:
    output_file.write(f"IMPOSSIBLE")
input_file.close()
output_file.close()

#Task1b: Here we can use two pointers to avoid inner looping system.
#As the array is already sorted, to find the tentative sum
#we start one pointer from the begining of the array and 
#another one from the end of it. If each sum of 1st iterator and 
#2nd one changes, we modify our iterator accordingly. 
#Eventually if the iterators colide or start becomes bigger than
#end one we write Impossible.