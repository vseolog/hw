f = open('/home/vseolog/Documents/PROJECTS/python/BASE_learning/26-145.txt', 'r')
N = int(f.readline())

strr = f.readline()
M, K = strr.split(' ')
M = int(M)
K = int(K)
groups = []
for str in f.readlines():
    adult, children = str.split(' ')
    adult, children = int(adult), int(children)
    groups.append([adult, children])

# groups.sort(key=lambda x: x[1])
# groups.reverse()
groups.sort(reverse=True)

wagon = [[0, 0, K * 4 + K * 2] for i in range(M)]  # [filled_coupe,filled_plazkart, freespace]
indx = 0
children=0
for i in range(N):
    if groups[i][0] <=2  and groups[i - 1][0] > 2:
        indx = 0

    if indx < M:
        wagon[indx][2] -= groups[i][0]

        children += groups[i][1]


        if groups[i][0] > 2:
            wagon[indx][0] += 1
            if wagon[indx][0] ==K:
                indx += 1

        else:
            wagon[indx][1] += 1
            if wagon[indx][1] == K:
                indx += 1
print(children)
print(wagon.index(max(wagon,key=lambda x:x[2]))+1)
