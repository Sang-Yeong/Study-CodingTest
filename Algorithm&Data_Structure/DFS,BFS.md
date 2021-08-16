# DFS / BFS
> 그래프를 탐색하기 위한 대표적인 알고리즘

- 탐색(search): 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
	- 그래프, 트리 등의 자료구조에서 주로 다룸

- 그래프 표현
1. 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
	- 2차원 배열에 각 노드가 연결된 형태 기록
	- 연결이 되어 있지 않은 노드끼리의 표현; Infinity
	- 모든 노드, 간선과의 관계를 저장 --> 노드의 개수가 많아질수록 메모리 낭비됨.

2. 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식
	- 2차원 리스트 이용
	- 연결된 정보만을 저장함 --> 메모리 효율적 사용 가능
	- 특정 노드 연결여부 파악에 한계 존재

```python
# row 3개인 2차원 리스트 표현
'''
[[0]*m]*n 과 같이 초기화 할 경우, 내부적으로 포함된 일부 리스트가 동일한 객체에 대한 reference로 인식되기 때문에,
계산 중 의도치 않은 결과가 나올 수 있음. 2차원 리스트를 초기화 할 때는 "Comprehension"을 이용해야 함.
'''
graph = [[] for _ in range(3)]
```


## DFS (Depth-First Search)
- 깊이 우선 탐색
- 스택 자료구조 이용
- 재귀 함수 이용하여 구현
- 시간복잡도: $$O(N)$$
1. 탐색 시작 노드를 스택에 삽입 & 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면, 그 인접노드를 스택에 넣고 방문 처리
3. 방문하지 않은 인접 노드가 없다면, 스택에서 최상단 노드 꺼냄.
(1,2,3번 반복)
	- 인접한 노드 중에서 방문하지 않은 노드가 여러개 존재할 경우, 작은 숫자부터 처리
	- 방문하지 않은 인접 노드 --> 하나씩 스택에 삽입

```python
def dfs(graph, v, visited):
	# 현재 노드 방문 처리
    visited[v] = True
    print(v, end = '')
	# graph 하나씩 방문하면서 방문 처리 여부에 따라 재귀적으로 처리
    for i in graph[v]:
    	if not visited[i]:
        	dfs(graph, i, visited)

graph = [[...], [...], ...]
visited = [False]*9
dfs(graph, 1, visited)
```


## BFS(Breadth First Search)
- 너비 우선 탐색
- 큐 자료구조 이용
- 시간복잡도: $$O(N)$$
- 실제 수행 시간은 DFS 보다 빠름.
1. 탐색 시작 노드를 큐에 삽입 & 방문 처리
2. 큐에서 노드 꺼냄 --> 해당 노드의 인접 노드 중에서 방문하지 않은 노드 **모두** 큐에 삽입
(1,2 과정 반복)


```python
from collections import deque

def bfs(graph, start, visited):
	# 탐색 시작 노드 큐에 삽입 & 방문 처리
	queue = deque([start])
    visited[start] = True
    # queue가 빌 때까지 반복
    while queue:
    	# 'queue에서 노드 꺼내고' 방문하지 않은 인접노드 확인
    	v = queue.popleft()
        print(v, end = '')
        # v에 대한 인접노드 중, 아직 방문하지 않은 노드 큐에 삽입
        for i in graph[v]:
        	if not visited[i]:
            	queue.append(i)
                visited[i] = True

graph = [[...], [...], ...]
visited = [False]*9
bfs(graph, 1, visited)
```




