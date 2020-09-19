# 시저 암호

def solution(s, n):
    answer = ''
    
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in s:
        if i.isalpha(): #알파벳
            if i >= 'a' and i <= 'z':   #소문자
                answer += small[(ord(i)-ord('a')+ n) % 26]
            else:
                answer += big[(ord(i)-ord('A')+ n) % 26]
        else:
            answer += i
    return answer