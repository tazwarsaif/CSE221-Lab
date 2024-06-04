# import numpy as np
# input_file = open("input3.txt","r")
# output_file = open("output3.txt","w")


# class Node:
#     def __init__(self,num):
#         self.id = num
#         self.color = 0
#         self.vertex = []

# class IDTrack:
#     def __init__(self,n):
#         self.ids = []
#         for i in range(n+1):
#             n = Node(i)
#             self.ids.append(n)
        

# tmplis = [int(i) for i in input_file.readline().split(" ")]
# n,l = tmplis
# main = IDTrack(n)


# for i in range(l):
#     tempo = [int(i) for i in input_file.readline().split(" ")]
#     main.ids[tempo[0]].vertex.append(main.ids[tempo[1]])
#     main.ids[tempo[1]].vertex.append(main.ids[tempo[0]])

# def dfs(graph,node):
#     node.color = 1
#     for ver in node.vertex:
#         if ver.color == 0:
#             output_file.write(f"{ver.id} ")
#             dfs(graph,ver)

# output_file.write(f"{main.ids[1].id} ")
# dfs(main.ids,main.ids[1])

# input_file.close()
# output_file.close()

input= open('input3(4).txt','r')
output= open('output3(4).txt','w')
temp= [int(i) for i in input.readline().split(' ')]
n, e= temp[0], temp[1]
graph = {}

for i in range(n + 1):
    graph[i] = []

for i in range(e):
    temp = [int(i) for i in input.readline().split(' ')]
    u,v = temp[0], temp[1]
    graph[u].append(v)
    graph[v].append(u)

color =[0]*(n+1)

def dfs(graph,node):
    color[node] = 1
    for v in graph[node]:
        if color[v] == 0:
            output.write(f"{v} ")
            dfs(graph,v)

output.write(f"{1} ")
dfs(graph,1)

input.close()
output.close()