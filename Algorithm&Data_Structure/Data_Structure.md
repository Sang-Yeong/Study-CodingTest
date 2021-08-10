#  자료구조
데이터를 표현, 관리, 처리하기 위한 구조

## Stack
- First in Last out 구조

```python
stack = []

# 삽입(5)-삽입(2)-삭제()-삽입(4)
stack.append(5) # 5
stack.append(2) # 5 2
stack.pop()     # 5
stack.append(4) # 5 4
```

## Queue
- First in First out 구조

```python
from collections import deque

queue = deque

# 삽입(5)-삽입(2)-삭제()-삽입(4)
queue.append(5) # 5
queue.append(2) # 5 2
queue.popleft() # 2
queue.append(4) # 2 4
```