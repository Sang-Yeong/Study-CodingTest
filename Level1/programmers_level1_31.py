# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    location = {'L':10, 'R':12} # * == 10, 0 == 11, # == 12
    
    for i in numbers:
            
        if i == 1 or i == 4 or i == 7:  # 왼쪽 엄지 사용
            answer += 'L'
            location['L'] = i
            
        elif i == 3 or i == 6 or i == 9:    # 오른쪽 엄지 사용
            answer += 'R'
            location['R'] = i
            
        else:   # 왼쪽과 오른쪽의 거리로 판단하기
            if i == 0:  # 0의 위치를 10으로 바꾸기
                i = 11
            
            l_row = int(location['L']//3.2)
            l_col = location['L']-3*l_row
            r_row = int(location['R']//3.2)
            r_col = location['R']-3*r_row
            
            left = [abs(l_row - int(i//3.2)), abs(l_col - (i-3*int(i//3.2)))]
            right = [abs(r_row - int(i//3.2)), abs(r_col - (i-3*int(i//3.2)))]
            
            
            if sum(left) == sum(right):    # 거리 같음
                if hand == "right":
                    answer += 'R'
                    location['R'] = i
                    
                else:
                    answer += 'L'
                    location['L'] = i
                
            
            elif sum(left) < sum(right):
                answer += 'L'
                location['L'] = i

            else:
                answer += 'R'
                location['R'] = i
                        
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))