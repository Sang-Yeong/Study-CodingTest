# 체육복

def solution(n, lost, reserve):
    answer = 0  # 체육복을 빌리지 못한 사람의 수
    
    for i in lost:
        if i in reserve:
            reserve[reserve.index(i)] = -1
            
        elif (i-1) in reserve:
            reserve[reserve.index(i-1)] = -1
            
        elif (i+1) in reserve:
            reserve[reserve.index(i+1)] = -1
            
        else:
            answer += 1
            
    answer = n - answer
    
    return answer

print(solution(5, [1,2,3,4,5], [1,2,3,4]))