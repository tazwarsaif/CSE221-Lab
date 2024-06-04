def funct(arr,ten):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == ten:
                return [i+1,j+1]
    return "IMPOSSIBLE"

input_file = open("input1a.txt","r")
output_file = open("output1a.txt","w")

tem = input_file.readline().split(" ")
l,ten = int(tem[0]),int(tem[1])

lis = [int(i) for i in input_file.readline().split(" ")]
some = funct(lis,ten)

if type(some) != list:
    output_file.write(some)
elif type(some) == list:
    output_file.write(f"{some[0]} {some[1]}")
input_file.close()
output_file.close()

#Task1a: Here we need to find the index to calculate a tentative sum.
#We built a function and checkif sum of two elements is equals to tentative sum
#eventually return our expected index as list.
#Otherwise, we return Impossible.