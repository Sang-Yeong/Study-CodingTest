'''
## 1945. 간단한 소인수분해 ##

숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.

'''

T = int(input())
for test in range(T):
    num = int(input())
    exp = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    i = 0
    while i < len(exp):
        if num == 1:
            break
        if not (num % list(exp.keys())[i]):
            exp[list(exp.keys())[i]] += 1
            num //= list(exp.keys())[i]
            continue
        else:
            i += 1

    print(f'#{test + 1} {exp[2]} {exp[3]} {exp[5]} {exp[7]} {exp[11]}')