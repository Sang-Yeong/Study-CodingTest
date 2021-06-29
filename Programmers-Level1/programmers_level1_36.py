# 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    
    for i in phone_number[0:-4]:
        answer += '*'
    answer += phone_number[-4:]
       
    # "*"*(len(s)-4) + s[-4:]
    
    return answer

print(solution('01033334444'))