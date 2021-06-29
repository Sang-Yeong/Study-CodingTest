# 짝수와 홀수

def solution(num):
    answer = ''
    
    if num % 2 :
        answer = 'Odd'
    else:
        answer = 'Even'
    
    return answer