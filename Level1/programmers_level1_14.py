# 두 정수 사이의 합

def solution(a, b):
    
    if a > b:
        a,b = b,a
        
    lst = [n for n in range(a, b+1)]
    return sum(lst)