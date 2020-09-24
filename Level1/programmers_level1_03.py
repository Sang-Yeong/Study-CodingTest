# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    
    # 바구니에 인형 넣기
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:   # 기계에 인형이 없을 때
                continue
            else:
                if len(basket) != 0 and basket[-1] == board[j][i-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
                
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))