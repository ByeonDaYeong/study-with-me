# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## 대표적인 데이터 구조4: 큐 (Queue)
#
# ### 1. 큐 구조
# * 줄을 서는 행위와 유사
# * 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
#   - 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
#   - FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대
#   
# <img src="https://www.fun-coding.org/00_Images/queue.png" />
# * 출처: http://www.stoimen.com/blog/2012/06/05/computer-algorithms-stack-and-queue-data-structure/
#
# > 엑셀로 이해해보기

# ### 2. 알아둘 용어
# * Enqueue: 큐에 데이터를 넣는 기능
# * Dequeue: 큐에서 데이터를 꺼내는 기능
# * <font color='#BF360C'>Visualgo 사이트에서 시연해보며 이해하기 (enqueue/dequeue 만 클릭해보며): https://visualgo.net/en/list

# ### 3. 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
# * **queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공**
# * <font color='#BF360C'>프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용</font>
#   - Queue(): 가장 일반적인 큐 자료 구조
#   - LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
#   - PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
#   
# > 일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음

# #### 3.1. Queue()로 큐 만들기 (가장 일반적인 큐, FIFO(First-In, First-Out))

# +
import queue

data_queue = queue.Queue()
# -

data_queue.put("funcoding")
data_queue.put(1)

data_queue.qsize()

data_queue.get()

data_queue.qsize()

data_queue.get()

# #### 3.2. LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))

import queue
data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)

data_queue.qsize()

data_queue.get()

# #### 3.3. PriorityQueue()로 큐 만들기

# +
import queue

data_queue = queue.PriorityQueue()
# -

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))
# 우선 순위가 높은 것부터 가져옴 

data_queue.qsize()

data_queue.get()

data_queue.get()

# ### 참고: 어디에 큐가 많이 쓰일까?
# - 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조)
#
# > 큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점이 없음), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음

# ### 4. 프로그래밍 연습 

# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습1: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기</font></strong>
# </div>

# +
queue_list = list()

def enqueue(data):
    queue_list.append(data)
    
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


# -

for index in range(10):
    enqueue(index)


len(queue_list)

dequeue()

# ### 쉬어가기: https://youtu.be/u6RoU-SDpYE
