
input= open('input1(b)_3.txt','r')
output= open('output1(b)_3.txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}

for i in range(n + 1):
    graph[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v = temp[0], temp[1]
    graph[u].append(v)

color = [0]*(n+1)
stack = []
visited = []
def dfs(node):
    color[node] = 1
    for ver in graph[node]:
        if color[ver] == 1:
            return False
        if color[ver] == 0:
            visited.append(ver)
            k = dfs(ver)
            if k == None:
                color[ver] = 2
            else:
                return k

    stack.append(node)

def topological_sort(stack):
            for i in graph.keys():
                if i == 0:
                    pass
                else:
                    if color[i] == 0:
                        a = dfs(i)
                        if a == False:
                             return a


a = topological_sort(stack)
if a == False:
    output.write("IMPOSSIBLE")
else:
    str1 = ""
    for i in stack[::-1]:
        str1 += (str(i)+" ")

    output.write(f"{str1}")

input.close()
output.close()