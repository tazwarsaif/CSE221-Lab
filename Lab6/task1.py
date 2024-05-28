
input= open('input1_2.txt','r')
output= open('output1_2.txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}

for i in range(n + 1):
    graph[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v,w = temp[0], temp[1],temp[2]
    graph[u].append((v,w))
start = int(input.readline())
color = [0]*(n+1)
distance = [float('inf')]*(n+1)
qu = [start]
distance[start] = 0
color[start] = 1
print(graph)
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
            print(distance)

bfs(graph,color,qu,distance)

for i in range(1,len(distance)):
    if distance[i] == float("inf"):
        output.write(f"-1 ")
    else:
        output.write(f"{distance[i]} ")
    


input.close()
output.close()