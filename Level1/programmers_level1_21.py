# 약수의 합

def solution3(n):
    answer = 0
    lst = []    # 약수를 담을 list
    
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
                
    answer += sum(lst)
    
    return answer