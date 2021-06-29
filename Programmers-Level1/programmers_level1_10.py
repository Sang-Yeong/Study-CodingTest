# 같은 숫자는 싫어
def solution(arr):
    answer = []
    
    for i in arr:
        if [i] != answer[-1:]:
            answer.append(i)
    
    return answer


print(solution([1,1,3,3,0,1,1]	))