def solution(board, moves):
    answer = 0
    basket = []
    n = len(board[0])
            
    for i in moves:
        print(i,'-moves')
        for j in range(n):
            print(j,'-board')
            if board[j][i-1] == 0:
                continue
            else:
                doll = board[j][i-1]
                board[j][i-1] = 0
                print('board=',board)
                break
            
        if basket == []:
            basket.append(doll)
            
        elif basket[-1] == doll:
            basket.pop()
            answer += 1
        else:
            basket.append(doll)
        print('basket = ', basket,'\n')
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print('result = ',solution(board, moves))