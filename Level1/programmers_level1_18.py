# 수박수박수박수박수?

def solution(n):
    answer = ''
    
    for i in range(1, n+1): # 홀수번째는 '수', 짝수번째는 '박' 반복
        if i % 2:
            answer += '수'
        else:
            answer += '박'
    
    return answer