
input= open('input2_3.txt','r')
output= open('output2_3.txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}

for i in range(n + 1):
    graph[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v,w = temp[0], temp[1],temp[2]
    graph[u].append((v,w))


al,bob = [int(i) for i in input.readline().split(' ')]
color1 = [0]*(n+1)
color2 = [0]*(n+1)
distanceA = [float('inf')]*(n+1)
distanceB = [float('inf')]*(n+1)


quA = [al]
quB = [bob]

distanceA[al] = 0
distanceB[bob] = 0

color1[al] = 1
color2[bob] = 1
both = []


def bfs(gra,colist,qu,distance):
    while len(qu)!=0:
        node = qu.pop(0)
        for i in gra[node]:
            n = i[0]
            w = i[1]
            if distance[n]>w+distance[node]:
                distance[n] = w+distance[node]
                if colist[n] == 0:
                    colist[n] = 1
                    qu.append(n)

bfs(graph,color1,quA,distanceA)
bfs(graph,color2,quB,distanceB)                     
nodeval = []
print(color1)
print(color2)
print(distanceA)
print(distanceB)
for i in range(len(color1)):
    if color2[i] == color1[i] and distanceA[i] != float("inf") and distanceB[i] != float("inf"):
        both.append(max(distanceA[i],distanceB[i]))
        nodeval.append(i)
print(both)
print(nodeval)
if len(both) == 0:
    output.write("IMPOSSIBLE")
elif len(both) == 1:
    output.write(f"Time {both[0]}\n")
    output.write(f"Node {nodeval[0]}")
else:
    min = both[0]
    idx = nodeval[0]
    for i in range(1,len(both)):
        if both[i] < min:
            min = both[i]
            idx = nodeval[i]
    output.write(f"Time {min}\n")
    output.write(f"Node {idx}")

input.close()
output.close()