def make_set(x):
    p[x] = x
    rank[x] = 0

def find_set(x):
    global p
    if x != p[x] :
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

N = 8
p = [0]*(N+1)
rank = [0]*(N+1)

for i in range(1,N+1):
    make_set(i)
union(1,3)
print(p)
print(rank)
union(2,3)
union(5,6)
union(6,8)
union(1,5)
union(6,7)
print(p)
print(rank)
find_set(4)
find_set(5)
#path compression을 하면
find_set(2)
find_set(1)
print(p)
print(rank)