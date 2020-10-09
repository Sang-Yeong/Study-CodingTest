# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if 'Kim' == seoul[i]:
            answer += '김서방은 {}에 있다'.format(i)
    
    return answer