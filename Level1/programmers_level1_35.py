# 하샤드 수
def solution(x):
    answer = True
    
    lst = list(map(int, list(str(x))))
    
    if x % sum(lst):
        answer = False
        
    # n % sum([int(c) for c in str(n)]) == 0
    
    return answer

print(solution(10))