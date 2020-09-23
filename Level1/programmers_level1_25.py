# 자연수 뒤집어 배열로 만들기

def solution1(n):
    answer = []
    
    while n != 0:
        answer.append(n % 10)
        n //= 10

    return answer



def solution2(n):
    answer = []
    
    answer = [int(i) for i in str(n)][::-1]

    return answer

print(solution2(12345))