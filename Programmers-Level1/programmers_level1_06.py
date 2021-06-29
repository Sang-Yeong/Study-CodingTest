# K번째 수

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        arr = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(arr[commands[i][2]-1])
    
    return answer

    # 한줄로 표현 가능
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
    