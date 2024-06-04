input_file = open("input2.txt","r")
output_file = open("output2.txt","w")

l = int(input_file.readline())
arr = [int(i) for i in input_file.readline().split(" ")]

def maxVal(arr,s,e):
    if s == e:
        return arr[s]
    mid = (s+e)//2
    num1 = maxVal(arr,s,mid)
    num2 = maxVal(arr,mid+1,e)
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2

maxed = maxVal(arr,0,l-1)
output_file.write(f"{maxed}")

input_file.close()
output_file.close()

#task 2:
#Here we used a recursive fuction. The unfolding part stays on until the start 
#and end becomes the same. the function returns the number.
#While the folding process stays up, it continuously checkes for greater number and returns
#the number accordingly 