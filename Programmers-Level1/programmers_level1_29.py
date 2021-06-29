# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    
    sorted_arr = sorted(arr, reverse = True)    # 입력받은 arr은 순서가 변하면 안됨.
    pop = sorted_arr.pop()
    
    if len(sorted_arr) == 0:    # pop한 뒤, 원소가 하나도 없을 경우
        answer.append(-1)
    else:
        del arr[arr.index(pop)] # 제일 작은 원소 삭제
        answer = arr
    
    return answer


def solution2(arr):
    answer = []
    
    if len(arr) == 1:   # 원소가 하나밖에 없는 경우, 가장 작은 원소 삭제하면 하나도 남지 않게됨.
        answer.append(-1)
    else:
        arr.remove(min(arr))    # arr list원소 중 가장 작은 원소 삭제
        answer = arr
        
    return answer

print(solution2([4,3,2,1]))