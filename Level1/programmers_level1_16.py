# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)): # 배열을 하나씩 돌면서 'Kim' 찾기
        if 'Kim' == seoul[i]:
            answer += '김서방은 {}에 있다'.format(i)
    
    return answer