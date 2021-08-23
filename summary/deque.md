# deque

양쪽 끝에서 삽입 / 삭제 가능(큐, 스택과 비슷)

append(val) : deque의 제일 마지막 부분에 val 값을 추가(오른쪽 끝)

appendleft(val) : deque는 양쪽 끝에서 삽입,삭제가 가능하기에, deque 시작 부분에 val 값 추가(왼쪽 끝)

extend(dest) : list와 마찬가지로 마지막 부분에 병합시켜준다

extendleft(dest) : 시작 부분에 병합시켜준다

pop() : deque 제일 마지막 부분부터 하나씩 추출 및 삭제한다(오른쪽 끝부터)

popleft() : deque 시작 부분부터 하나씩 추출 및 삭제한다(왼쪽 부터)

rotate(count) : count만큼 deque 값들을 회전, 음수면 왼쪽, 양수면 오른쪽으로 회전



```python
deq = deque([i for i in range(1, int(input())+1)])
while len(deq) > 1:
    deq.popleft()               # 제일 왼쪽값 추출 및 삭제 1
    deq.append(deq.popleft())   # 맨 끝에 값 추가          2
print(deq.pop())
#################################
#           1                   #
#           2                   #
#           3                   #
#           4                   #
#           5                   #
#           6                   #
#################################
#################################
#           3                   #
#           4                   #
#           5                   #
#           6                   #
#           2                   #
#################################
#################################
#           5                   #
#           6                   #
#           2                   #
#           4                   #
#################################
#################################
#           2                   #
#           4                   #
#           6                   #
#################################
#################################
#           6                   #
#           4                   #
#################################
#################################
#           6                   #
#################################
```

```python
List
# collections.Counter 예제 (1)
# list를 입력값으로 함
import collections
lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))
'''
결과
Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
'''
​
```

```python
Dictionary - 요소의 갯수가 많은 것 부터 출력해준다.
# collections.Counter 예제 (2)
# dictionary를 입력값으로 함
import collections
print(collections.Counter({'가': 3, '나': 2, '다': 4}))
'''
결과
Counter({'다': 4, '가': 3, '나': 2})
'''
​
```

