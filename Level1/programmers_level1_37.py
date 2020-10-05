# 행렬의 덧셈

def solution(arr1, arr2):
    answer = [[]]
    arr = []

    for a1, a2 in zip(arr1, arr2):
        for i in range(len(arr1[0])):
            arr.append(a1[i]+a2[i])
        answer.append(arr)
        arr= []
     
    answer.remove(answer[0])
    
    # answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    
    return answer

print(solution([[1],[2]], [[3],[4]]))