# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    
    for i in range(len(strings)):   # n번째 글자를 주어진 글자의 제일 앞에 붙이기
        strings[i] = strings[i][n] + strings[i]
        
    strings.sort()  # 그대로 sort진행
    
    for i in range(len(strings)):   # 앞에 더해준 n번째 글자를 뺀 나머지 글자를 answer에 넣기
        answer.append(strings[i][1::])

    return answer

    # 정렬시, key인자 이용
    # return sorted(strings, key=lambda x: x[n])

print(solution(['sun', 'bed', 'car'], 1))