'''
## 2027. 대각선 출력하기 ##

#++++
+#+++
++#++
+++#+
++++#

'''

for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end='')
        else:
            print('+', end='')
    print()