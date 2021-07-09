'''
## 1933. 간단한 N 의 약수 ##

입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

[제약사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

[입력]
입력으로 정수 N 이 주어진다.

[출력]
정수 N 의 모든 약수를 오름차순으로 출력한다.

10 ->  1 2 5 10
'''

n = int(input())
result = []
for i in range(1, n // 2 + 1):
    if not (n % i):
        result.append(i)
        result.append(n // i)

result = list(set(result))
result.sort()

for i in result:
    print(i, end=' ')