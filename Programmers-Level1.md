# What I learned while solving the problem.

##### level1_20. 시저 암호
- ord()와 chr()
	- ord(): 문자 --> 아스키코드
	- chr(): 아스키코드 --> 문자



##### level1_22. [1차] 비밀지도
- zip() 함수의 사용
	- zip(*iterable): 동일한 개수로 이루어진 자료형을 묶어 주는 역할

    ```python
    list(zip([1, 2, 3], [4, 5, 6]))			# [(1, 4), (2, 5), (3, 6)]
    list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))	# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
	list(zip("abc", "def"))				# [('a', 'd'), ('b', 'e'), ('c', 'f')]
    ```

- bin() 함수의 사용
	- 정수를 '0b' 가 앞에 붙은 이진 문자열로 변환
	```python
    bin(3)		#'0b11'
	bin(-10)	#'-0b1010'
    ```