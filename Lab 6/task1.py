input = open("input1_2.txt","r")
output = open("output1_2.txt","w")

n,e = [int(i) for i in input.readline().split(" ")]
parent = []
chilnum = [1]*n

for i in range(n):
    parent.append(i)

def find_parent(arr,node):
    if arr[node] == node:
        return node
    return find_parent(arr,arr[node])

for i in range(e):
    v,u = [int(i) for i in input.readline().split(" ")]
    parent1 = find_parent(parent,v)
    parent2 = find_parent(parent,u)
    if parent1 == parent2:
        output.write(str(chilnum[parent1]))
    elif chilnum[parent1] >= chilnum[parent2]:
        parent[parent2] = parent1
        chilnum[parent1] += chilnum[parent2]
        output.write(str(chilnum[parent1]))
    else:
        parent[parent1] = parent2
        chilnum[parent2] += chilnum[parent1]
        output.write(str(chilnum[parent2]))
    output.write("\n")
    
input.close()
output.close()

