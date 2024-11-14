# 값 입력받기(노드 수, 간선 수, 시작할 노드 번호)
n,m,v = map(int, input().split())


# 이차원 배열 선언(각 행에 대해 n+1개의 0을 포함하는 리스트를 생성하고 해당 배열을 n+1번 반복한 이차원배열 생성)
graph = [[ 0 for _ in range(n+1)] for _ in range(n+1)]


# 간선이 연결하는 두 정점의 번호 입력받고 이차원 배열에 넣어주기
for i in range(m):
    x, y =map(int, input().split())
    graph[x][y]=1
    graph[y][x]=1

print(graph)


def dps(start):
    for _ in range():
        print();

def bps(start):
    print()