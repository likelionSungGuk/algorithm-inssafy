N = 8
p = [0] * (N+1)     #각 정점의 부모
rank = [0] * (N+1)  #각 정점의 rank(서브트리의 깊이)

def make_set(x):
    p[x] = x

#path compression 적용한 버전으로 (findset 하면서 거쳐간 정점의 부모를 대표자로 설정
def find_set(x):
    pass

#x, y가 속한 집합을 합침
#x, y의 대표를 찾음
#x, y 각각의 대표의 랭크를 비교
def union(x,y):
    pass

for i in range(1, N+1):
    make_set(i)


print(p)
print(rank)