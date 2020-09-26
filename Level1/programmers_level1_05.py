# 모의고사

def solution(answers):
    answer = []
    
    stu1 = '12345'
    stu2 = '21232425'
    stu3 = '3311224455'
    
    dic = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == int(stu1[i % 5]):
            dic[1] += 1
        if answers[i] == int(stu2[i % 8]):
            dic[2] += 1
        if answers[i] == int(stu3[i % 10]):
            dic[3] += 1
    
    
    max_value = max(dic.values())
    for k in dic.keys():
        if dic[k] == max_value:
            answer.append(k)
    
    return answer


print(solution([1,3,2,4,2]))