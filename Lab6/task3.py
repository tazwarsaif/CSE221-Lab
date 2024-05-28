
input= open('input3_1.txt','r')
output= open('output3_1.txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}

for i in range(n + 1):
    graph[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v,w = temp[0], temp[1],temp[2]
    graph[u].append((v,w))

paths = []
distance = []
color = [0]*(n+1)

def dfs_pathfinding(gra,srt,end,dist,paths):
    if srt == end:
        color[end] = 1
        tem = list(dist)
        paths.append(tem)
        return paths
    color[srt] = 1
    for i in graph[srt]:
        no = i[0]
        w = i[1]
        if color[no] == 0 or color[no] >= 1:
            dist.append(w)
            a = dfs_pathfinding(gra,no,end,dist,paths)
            if len(dist) > 0:
                dist.pop()
            color[no] = 2
    return paths

dfs_pathfinding(graph,1,n,distance,paths)
print(paths)
mini = float("inf")

for lis in paths:
    maxed = lis[0]
    for j in lis:
        if j>maxed:
            maxed = j
    if mini > maxed:
        mini = maxed
output.write(str(mini))


input.close()
output.close()