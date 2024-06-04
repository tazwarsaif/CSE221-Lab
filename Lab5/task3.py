import heapq as hq
input= open('input3_2.txt','r')
output= open('output3_2.txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}
transpose = {}

for i in range(n + 1):
    graph[i] = []
    transpose[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v = temp[0], temp[1]
    graph[u].append(v)
    transpose[v].append(u)

color = [0]*(n+1)
colorafter = [0]*(n+1)
stack = []
endlis = []

def dfs(gra,node,stacked,colorlis):
    colorlis[node] = 1
    for ver in gra[node]:
        if colorlis[ver] == 0:
            k = dfs(gra,ver,stacked,colorlis)
            colorlis[ver] = 2

    stacked.append(node)

def funct(gra,stack,colorlis):
    for i in gra.keys():
        if i == 0:
            pass
        else:
            if colorlis[i] == 0:
                a = dfs(gra,i,stack,colorlis)

def another(gra,stacked):
    for i in stacked:
        if colorafter[i] == 0:
            a = dfs(gra,i,endlis,colorafter)
            hq.heapify(endlis)
            for j in range(len(endlis)):
                temp = hq.heappop(endlis)
                output.write(f"{temp} ")
            output.write(f"\n")
            


a = funct(graph,stack,color)
k = another(transpose,stack[::-1])


input.close()
output.close()