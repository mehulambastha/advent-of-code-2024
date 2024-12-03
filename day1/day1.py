with open('./input.txt', 'r') as f:
    data = f.readlines()

coord1 = []
coord2 = []

for line in data[0:1000]:
    lineData = line.split("   ")
    coord1.append(int(lineData[0]))
    coord2.append(int(lineData[1][0:5]))

coord1.sort()
coord2.sort()


def day1question1(coord1, coord2):
    sum = 0
    for x in range(0, 1000):
        sum += abs(coord1[x] - coord2[x])

    print("sum: ", sum)
    return sum


def day1Ques2(coor1: list, coor2: list) -> int:
    similarity_score = 0

    for num in coor1:
        count = coor2.count(num)
        similarity_score += (num * count)

    return similarity_score


print(day1Ques2(coord1, coord2))
