from collections import deque


def islandCoverter(M):
    if M is None or M == [[]]:
        return 0
    islands = 0
    r = len(M[0])
    c = len(M)
    for i in range(0, c):
        for j in range(0, r):
            if M[i][j] == 1:
                islands += 1
                find_parts_of_island(M, i, j, r, c)
    return islands


def find_parts_of_island(M, i, j, r, c):
    q = deque()
    q.append([i, j])
    while len(q) != 0:
        i = q.pop()
        x = i[0]
        y = i[1]
        print(x,y)
        if M[x][y] == 1:
            M[x][y] = 2
            appendif(q, r, c, x, y + 1)
            appendif(q, r, c, x + 1, y)
            appendif(q, r, c, x, y - 1)
            appendif(q, r, c, x - 1, y)


def appendif(q, r, c, x, y):
    if 0 < x < c and 0 < y < r:
        q.append([x, y])


print(islandCoverter(None))
print(islandCoverter([[]]))
M = [[1, 0, 1], [1, 1, 1]]
print(islandCoverter(M))
print(M)
