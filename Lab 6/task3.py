input = open("input3_4.txt","r")
output = open("output3_4.txt","w")
n = int(input.readline())

if n <= 1:
    output.write(str(1))
else:
    w1 = 1
    w2 = 1
    w3 = 0
    for i in range(n-1):
        w3 = w1 + w2
        w1 = w2
        w2 = w3

    output.write(str(w3))

input.close()
output.close()
