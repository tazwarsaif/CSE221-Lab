input= open('input1(a)_3.txt','r')
output= open('output1(a)_3.txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}
indeg = [0]*(n+1)
for i in range(n + 1):
    graph[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v = temp[0], temp[1]
    graph[u].append(v)
    indeg[v] = indeg[v]+1

color = [0]*(n+1)
qu =[]
for i in range(len(indeg)):
    if i == 0:
        pass
    elif indeg[i] == 0:
        color[i] = 1
        qu.append(i)
        
def bfs(qu,graph):
    str1 = ""
    while len(qu) != 0:
        node = qu.pop(0)
        color[node] = 1
        if indeg[node] != 0:
            temp = indeg[node]
            for j in qu:
                if node in graph[j]:
                    temp-=1
            if temp != 0:
                return "IMPOSSIBLE"
        str1 += f"{node} "
        for i in graph[node]:
            indeg[i] -= 1
            if color[i] == 0:
                qu.append(i)
                color[i] = 1
                

    return str1

def topological_sort(qu,graph):
        str2 = ""
        for i in graph.keys():
            if i == 0:
                pass
            else:
                if color[i] == 0:
                    a = bfs(qu,graph)
                    if a == "IMPOSSIBLE":
                        return a
                    str2+=a
        return str2
                        

str11 = topological_sort(qu,graph)

output.write(f"{str11}")

input.close()
output.close()
