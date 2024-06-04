input_file=open("input5(2).txt","r")
output_file = open("output5(2).txt","w")


tmplis = [int(i) for i in input_file.readline().split(" ")]
n,l,des = tmplis
graph = {}

for i in range(n+1):
    graph[i] = []

for i in range(l):
    tempo = [int(i) for i in input_file.readline().split(" ")]
    if tempo[0] not in graph.keys():
        graph[tempo[0]] = [tempo[1]]
    else:
        graph[tempo[0]].append(tempo[1])
    if tempo[1] not in graph.keys():
        graph[tempo[1]] = [tempo[0]]
    else:
        graph[tempo[1]].append(tempo[0])
    

color = [0]*(n+1)
qu = []
quminus = [-1]*(n+1)
print(graph)
def bfs(graph,color,qu):
    for i in range(len(graph.keys())):
        if i == 1:
            qu.append(i)
            color[i] = 1
            break
    while len(qu) != 0:
        m = qu.pop(0)
        print(m,end=" ")
        tempo = graph[m]
        for i in tempo: 
            if color[i] == 0:
                qu.append(i)
                quminus[i] = m
                color[i] = 1

bfs(graph,color,qu)

lis1 = []
while quminus[des] != -1:
    lis1.append(des)
    des = quminus[des]

str1 = "1 "
for i in range(len(lis1)-1,-1,-1):
    str1 += str(lis1[i])+" "
output_file.write(f"Time: {len(lis1)}\n")
output_file.write(f"{str1}")


input_file.close()
output_file.close()