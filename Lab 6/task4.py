input = open("input4_1.txt","r")
output = open("output4_1.txt","w")

n,t = [int(i) for i in input.readline().split(" ")]

lis1 = [int(i) for i in input.readline().split(" ")]

def find_least(arr,target):
    lis2 = [float("inf")]*(target+1)
    lis2[0] = 0
    for i in range(1,len(lis2)):
        for elem in arr:
            if elem <= i:
                lis2[i] = min(lis2[i],lis2[i-elem]+1)
    if lis2[-1] == float("inf"):
        return -1
    return lis2[-1]

least = find_least(lis1,t)
output.write(str(least))


    
input.close()
output.close()
