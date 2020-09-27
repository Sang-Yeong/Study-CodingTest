# 정수 제곱근 판별

import math

def solution(n):
    answer = 0
    
    if math.sqrt(n) == int(math.sqrt(n)):   # sqrt()는 float로 반환 --> 만약 제곱수라면 int로 형변환해도 결과가 같게 나옴.
        answer += (int(math.sqrt(n)) + 1)**2
    else:
        answer += -1
    
    return answer


print(solution(121))
