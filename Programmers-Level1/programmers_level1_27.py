# 예산

def solution(d, budget):
    answer = 0
    
    d.sort()   # 오름차순으로 정렬
    for i in d:
        if budget-i >= 0:
            answer += 1
            budget -= i
    
    return answer



print(solution([2,2,3,3], 10))