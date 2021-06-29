# 평균 구하기

def solution(arr):
    answer = 0
    
    answer += sum(arr)/len(arr)
    
    return answer


print(solution([1,2,3,4]))