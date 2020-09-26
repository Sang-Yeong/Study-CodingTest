# 2016년

def solution(a, b):
    answer = ''
    
    total_day = 0
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    for i in range(a):
        if i >= 1:
            total_day += months[i-1]
        
    total_day += b - 1
    answer = days[total_day % 7]
    
    return answer

    # 한줄로 코드 완성
    # days[(sum(months[:a-1])+b-1)%7]

print(solution(5, 24))