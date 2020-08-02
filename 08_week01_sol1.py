# 8월 1주차 문제풀이 - 1. 완주하지 못한 선수

def solution(participant, completion):
    
    dic = {}
    for i in participant:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
            
    print(dic)
    
    for key in dic.keys():
        if key in completion:
            dic[key] -= 1
            
    print(dic)
            
    for key, val in dic.items():
        if val >= 1:
            answer = key
    return answer


participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant, completion))