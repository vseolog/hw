import math
try:
    a = int(input('Enter the number 1: '))
    b = int(input('Enter the number 2: '))
except:
    print('Wrong input format!')
    a = int(input('Enter the number 1: '))
    b = int(input('Enter the number 2: '))

if a>b:
    c=a
    d=b
    a=d
    b=c
for i in range(a-1,b+1):
    if i == 0:
        continue
    div = []
    count = 0
    for j in range(1, math.ceil(i**0.5) + 2):
        if i % j == 0:
            count+=1
            if i % (i//j) == 0 and i//j not in div:
                div.append(i//j)

            if j not in div:
                div.append(j)
    if len(div) == 4:
        div.sort()
        div.reverse()
        print('Number', i,', divisors: ',div[0],div[1],div[2],div[3])
