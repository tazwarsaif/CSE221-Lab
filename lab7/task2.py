input = open("input2_2.txt","r")
output = open("output2_2.txt","w")

n,e = [int(i) for i in input.readline().split(" ")]
cost = [float("inf")]*(n+1)
cost[1] = 0

for i in range(e):
    u,v,c = [int(i) for i in input.readline().split(" ")]
    if cost[u] == float("inf") or cost[v] == float("inf"):
        if cost[u] == float("inf") and cost[v] == float("inf"):
            cost[u] = c
            cost[v] = c
        elif cost[u] == float("inf"):
            cost[u] = c
        elif cost[v] == float("inf"):
            cost[v] = c
    else:
        if cost[u] >= cost[v]:
            if cost[u] > c:
                cost[u] = c
        elif cost[v] > c:
            cost[v] = c
sum = 0
for i in range(1,len(cost)):
    sum += cost[i]

output.write(str(sum))
    
input.close()
output.close()
