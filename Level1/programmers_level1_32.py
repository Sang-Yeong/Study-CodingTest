# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    
    for i in range(min(n, m), 0, -1):   #최대공약수
        if n % i == 0 and m % i == 0:
            answer.append(i);
            break
    
    for i in range(max(n, m), n*m+1):   # 최소공배수
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
        
    return answer


def solution2(a, b):
    c, d = max(a, b), min(a, b)
    
    while d:    # 유클리드 호제법
        c, d = d, c % d
        
    answer = [c, int(a*b/c)]

    return answer

print(solution(3, 12))
