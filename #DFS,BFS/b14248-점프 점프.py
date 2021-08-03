'''
문제
영우는 지금 n개의 돌이 일렬로 놓여있는 돌다리에 있다. 그리고 돌다리의 돌에는 숫자가 하나씩 적혀있다.
영우는 이 숫자가 적혀있는 만큼 왼쪽이나 오른쪽으로 점프할 수 있는데, 이때 돌다리 밖으로 나갈 수는 없다.

영우는 이 돌다리에서 자기가 방문 가능한 돌들의 개수를 알고 싶어한다.
방문 가능하다는 것은 현재위치에서 다른 돌을 적절히 밟아 해당하는 위치로 이동이 가능하다는 뜻이다.

현재 위치가 주어졌을 때, 영우가 방문 가능한 돌들의 개수를 출력하시오.

입력
첫 번째 줄에는 돌다리의 돌 개수 n이 주어진다.(1≤n≤100,000) 돌의 번호는 왼쪽부터 1번에서 n번이다.
다음 줄에는 그 위치에서 점프할 수 있는 거리 Ai가 주어진다.(1≤Ai≤100,000)

다음 줄에는 출발점 s가 주어진다.(1≤s≤n)

출력
영우가 방문 가능한 돌들의 개수를 출력하시오.

'''

import sys
sys.stdin = open('../input.txt','r')

from collections import deque

st_num = int(input())
graph = list(map(int, input().split()))
start = int(input())-1
visit = [0]*st_num

# 이동할 방향 정의(좌우)
d = [-1, 1]

def bfs(s):
    queue = deque()
    queue.append(s)
    result = 1
    visit[s] = 1

    # queue가 빌 때까지 반복
    while queue:
        s = queue.popleft()
        times = graph[s]

        # for i in [-graph[s], graph[s]]:
        #     n = s + i
        # 왼, 오 2방향으로 위치 확인
        for j in range(2):
            n = s+(d[j]*times)
            if n >= 0 and n < st_num and visit[n] == 0:
                visit[n] = 1
                result += 1
                queue.append(n)

    return result

print(bfs(start))