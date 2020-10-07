def solution(s):
    s = s.lower()
    dic = {'p':0, 'y':0}
    
    for i in s:
        if i in dic:
            dic[i] += 1
            
    return dic['p'] == dic['y']
