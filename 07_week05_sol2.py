# 7월 5주차 문제풀이 - 2. 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    n = len(board[0])
            
    for i in moves:
        for j in range(n):
            if board[j][i-1] == 0:
                continue
            else:
                doll = board[j][i-1]
                board[j][i-1] = 0
                break
            
        if basket == []:
            basket.append(doll)
            
        elif basket[-1] == doll:
            basket.pop()
            answer += 1
        else:
            basket.append(doll)
            
    return answer