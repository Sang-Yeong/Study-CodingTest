'''
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다.
데스 나이트가 있는 곳이 (r, c)라면,
(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다.
데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자.
체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다.
이동할 수 없는 경우에는 -1을 출력한다.

'''
import sys
sys.stdin = open('../input.txt', 'r')

from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, +1, -2, +2, -1, +1]

n = int(input())
graph = [[0]*n for _ in range(n)]

r1, c1, r2, c2 = map(int, input().split())

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1,y1))

    while queue:
        x,y = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    if graph[x2][y2] == 0:
        graph[x2][y2] = -1

    return graph[x2][y2]


print(bfs(r1, c1, r2, c2))