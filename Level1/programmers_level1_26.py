# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    
    n = str(n)
    answer = int(''.join(sorted(n,reverse = True)))
    
    return answer


print(solution(118372))