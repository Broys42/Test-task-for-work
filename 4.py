t = int(input())
pairs = []

def checkBeautyNumber(number):
    stroke = str(number)
    numbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in stroke:
        if int(i) in numbersList:
            numbersList.remove(int(i))
        else:
            return False

    return True

for i in range(t):
    edges = [int(x) for x in input().split() if int(x) >= 1 and int(x) <= 1000000000]
    pairs.append((edges[0], edges[1]))

for i in pairs:
    count = 0
    for j in range(i[0], i[len(i) - 1] + 1):
        if checkBeautyNumber(j):
            count += 1

    print(count)
