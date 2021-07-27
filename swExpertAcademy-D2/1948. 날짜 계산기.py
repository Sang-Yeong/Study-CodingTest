'''
## 1948. 날짜 계산기 ##

월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.

[제약 사항]
월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.
1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.

'''

T = int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test in range(T):
    date_list = list(map(int, input().split()))
    sum_date = 0

    if date_list[0] == date_list[2]:
        sum_date = date_list[3] - date_list[1] + 1

    else:
        sum_date += date_list[3]
        sum_date += days[date_list[0]] - date_list[1] + 1

        for i in range(date_list[2] - 1, date_list[0], -1):
            sum_date += days[i]

    print(f'#{test + 1} {sum_date}')