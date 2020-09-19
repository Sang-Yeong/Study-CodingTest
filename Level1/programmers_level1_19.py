# 문자열을 정수로 바꾸기

def solution(s):
    answer = 0
    
    if s[0] == '+': # s에 +부호가 붙었을 때
        answer += int(s[1:])
    elif s[0] == '-':
        answer -= int(s[1:])    # s에 -부호가 붙었을 때
    else:   # s에 부호가 없을 때 --> +
        answer += int(s)
    
    return answer