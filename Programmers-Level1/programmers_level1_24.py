# 자릿수 더하기

def solution(n):
    
    n = str(n)  # int값을 바로 list로 변환해주지 못함. 문자열로 만들어서 변환할 수 있도록 처리
    num_list = list(n)  # 주어진 형식
    num_list = sum([int(num) for num in num_list])  # num_list에 있는 문자를 하나씩 빼서 정수형으로 바꿔주고 합 구하기
    
    return num_list

print(solution(123))