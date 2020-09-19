# [1차] 비밀지도

def solution1(n, arr1, arr2):
    answer = []
    lst1, lst2 = [], []
    
    for i in range(n):  # arr1, arr2의 원소
        for j in range(n):  # 원소들을 2진수로 나타내
            lst1.append(arr1[i] % 2)
            arr1[i] //= 2
            
            lst2.append(arr2[i] % 2)
            arr2[i] //= 2
            
        arr1[i] = lst1[::-1]    # 거꾸로 2진수가 저장되어 있기 때문
        arr2[i] = lst2[::-1]
        
        lst1 = []   # 초기화
        lst2 = []
    
    arr_and = arr1[:]

    
    for i in range(n):
        for j in range(n):
            arr_and[i][j] = str(arr1[i][j] or arr2[i][j]) 
        answer.append(''.join(arr_and[i]))
        
        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('0', ' ')
    
    
def solution2(n, arr1, arr2):
    
    answer = []
    
    for i,j in zip(arr1,arr2):
        
        a12 = str(bin(i|j)[2:]) # index 2부터 시작한 이유: 0b11111이런식으로 0b가 붙기 때문
        
        a12=a12.rjust(n,'0')    # n자릿수 맞추기 위해 0으로 메꿔주기
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        
        answer.append(a12)
    

    return answer
