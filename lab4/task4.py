input_file = open("input4.txt","r")
output_file = open("output4.txt","w")


class Node:
    def __init__(self,num):
        self.id = num
        self.color = 0
        self.vertex = set()

class IDTrack:
    def __init__(self,n):
        self.ids = []
        for i in range(n+1):
            n = Node(i)
            self.ids.append(n)
        

tmplis = [int(i) for i in input_file.readline().split(" ")]
n,l = tmplis
main = IDTrack(n)
print(tmplis)

lis1 = []

for i in range(l):
    tempo = [int(i) for i in input_file.readline().split(" ")]
    lis1.append([tempo[0],tempo[1]])
    main.ids[tempo[0]].vertex.add(main.ids[tempo[1]])

print(lis1)

stack = []


def dfs(graph,node):
    node.color = 1
    for ver in node.vertex:
        if ver.color == 1:
            return "Yes"
        if ver.color == 0:
            stack.append(ver)
            p = dfs(graph,ver)
            if p == None:
                a = stack.pop()
                a.color = 2
            else:
                return p


k = dfs(main.ids,main.ids[1])
if k == None:
    output_file.write("No")
else:
    output_file.write(f"{k}")



input_file.close()
output_file.close()