~~~
# Chapter 03. Sequential Logic Design(순차 논리 회로)
~~~

> ## 1. Introduction (소개)
>
> 1. 순차회로의 출력은 현재의 입력과 과거의 입력 값에 의존한다. == 메모리를 가지고 있다.
> 
> 2. Some definitions:
> 	1) State(상태)
> 	2) Latches
> 	3) Flip - flops
> 	4) Synchronous sequential circuits
> 	
> 3. Sequential Circuits
> 
> 4. State Elements (상태 요소)
> 	1) Bistable circuit
> 	2) SR Latch
> 	3) D Latch
> 	4) D Flip-flop


> ## 2. Latches and Flip-Flops (래치와 플립플롭)
>
>> ### 1) Bistable circuit
>> - bi(2개) + stable(안정적인)
>> - Two outputs: Q, Q
>> - No inputs
>> *![2-1-1](이미지링크)
>> - Consider the two possible cases:
	Q = 0: then Q = 1 and Q = 0 (consistent)
	Q = 1: then Q = 0 and Q = 1 (consistent)
>> - input이 없으면 메모리로서의 의미가 X --> NOT gate 대신 NOR gate사용하여 입력값을 받을 수 있게 바꾼다.


>> ### 2) SR Latch
>> - Set + Reset Latch
>> - Definitions
	Set: Make the output 1
	Reset: Make the output 0
>> *![2-2-1](이미지링크)
>> - Consider the four possible cases:
	(1) S = 1, R = 0
	(2) S = 0, R = 1
	(3) S = 0, R = 0
	(4) S = 1, R = 1











> ## 3. Synchronous Logic Design (동기식 회로 설계)
> ## 4. Finite State Machines (유한 상태 기계)
> ## 5. Timing of Sequential Logic (순차회로의 타이밍)
> ## 6. Parallelism (병렬성)





