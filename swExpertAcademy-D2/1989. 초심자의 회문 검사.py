'''
## 1989. 초심자의 회문 검사 ##

"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

'''

T = int(input())
for test in range(T):
    s = list(input())
    s_t = s[::-1]

    if s == s_t:
        print(f'#{test+1} 1')
    else:
        print(f'#{test+1} 0')