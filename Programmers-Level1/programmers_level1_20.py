# 시저 암호

def solution(s, n):
    answer = ''
    
    for i in s:
        if i.isalpha(): #알파벳
            if i >= 'a' and i <= 'z':   #소문자
                answer += chr(ord('a') + ((ord(i)-ord('a')+n) % 26))
            else:
                answer += chr(ord('A') + ((ord(i)-ord('A')+n) % 26))
        else:
            answer += i
    return answer


print(solution("AAbs d", 1))