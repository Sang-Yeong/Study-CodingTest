# 이상한 문자 만들기

def solution(s):
    answer = ''
    
    cnt = 0
    
    for i in s:
        if i == ' ':
            cnt = 0
            answer += ' '
        else:
            cnt += 1
            if cnt % 2 == 0: #인덱스 1부터 시작-짝수번째 인덱스 --> 소문자
                answer += i.lower()
            else: 
                answer += i.upper()
            
    return answer

print(solution("try hello world"))