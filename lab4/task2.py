import numpy as np
input_file = open("input2.txt","r")
output_file = open("output2.txt","w")


class Node:
    def __init__(self,num):
        self.id = num
        self.color = 0
        self.vertex = []

class IDTrack:
    def __init__(self,n):
        self.ids = []
        for i in range(n+1):
            n1 = Node(i)
            self.ids.append(n1)
        

tmplis = [int(i) for i in input_file.readline().split(" ")]
n,l = tmplis
main = IDTrack(n)


for i in range(l):#[1,2]
    tempo = [int(i) for i in input_file.readline().split(" ")]
    main.ids[tempo[0]].vertex.append(main.ids[tempo[1]])
    main.ids[tempo[1]].vertex.append(main.ids[tempo[0]])

qu = []

def bfs(idtrack,qu):
    qu = [idtrack[1]]
    idtrack[1].color = 1

    while len(qu) != 0:
        m = qu.pop(0)
        output_file.write(f"{m.id} ")
        trav = m.vertex
        for i in trav:
            print(qu)
            if i.color == 0:
                qu.append(i)
                i.color = 1
    
bfs(main.ids,qu)



# tmplis = [int(i) for i in input_file.readline().split(" ")]
# n,l = tmplis
# graph = {}

# for i in range(n+1):
#     graph[i] = []

# for i in range(l):
#     tempo = [int(i) for i in input_file.readline().split(" ")]
#     if tempo[0] not in graph.keys():
#         graph[tempo[0]] = [tempo[1]]
#     else:
#         graph[tempo[0]].append(tempo[1])
#     if tempo[1] not in graph.keys():
#         graph[tempo[1]] = [tempo[0]]
#     else:
#         graph[tempo[1]].append(tempo[0])
    

# color = [0]*(n+1)
# qu = []
# print(color)

# def bfs(graph,color,qu):
#     for i in range(len(graph.keys())):
#         if i == 1:
#             qu.append(i)
#             color[i] = 1
#             break
#     while len(qu) != 0:
#         m = qu.pop(0)
#         print(m,end=" ")
#         tempo = graph[m]
#         for i in tempo: 
#             if color[i] == 0:
#                 qu.append(i)
#                 color[i] = 1

# print(graph)    
# bfs(graph,color,qu)

# output_file.write(f"{graph}")

input_file.close()
output_file.close()