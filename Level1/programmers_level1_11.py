# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    
    answer = sorted([n for n in arr if n % divisor == 0])
    
    if len(answer) == 0:
        answer = [-1]
    
    return answer

# answer = sorted([n for n in arr if n%divisor == 0]) or [-1]
print(solution([5, 9, 7, 10], 5))