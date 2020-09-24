# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    
    for i in completion:
        if i in participant:    # 완주한 선수가 있는 경우
            participant[participant.index(i)] = ''
    
    for i in participant:   # 완주하지 못한 선수
        if i != '':
            answer = i
    
    return answer


print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))