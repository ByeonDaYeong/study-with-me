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

# ### 6. 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)
# * 다음 코드는 위의 코드에서 delete 메서드만 추가한 것이므로 해당 메서드만 확인하면 됨

# +
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == '':
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


# -

# #### 테스트를 위해 1개 노드를 만들어 봄

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# #### head 가 살아있음을 확인

linkedlist1.head

# #### head 를 지워봄(위에서 언급한 경우의 수1)

linkedlist1.delete(0)

# #### 다음 코드 실행시 아무것도 안나온다는 것은 linkedlist1.head 가 정상적으로 삭제되었음을 의미

linkedlist1.head

# #### 다시 하나의 노드를 만들어봄

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# #### 이번엔 여러 노드를 더 추가해봄

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()

# #### 노드 중에 한개를 삭제함 (위에서 언급한 경우의 수2)

linkedlist1.delete(4)

# #### 특정 노드가 삭제되었음을 알 수 있음

linkedlist1.desc()

linkedlist1.delete(9)

linkedlist1.desc()

# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습1: 위 코드에서 노드 데이터가 2인 노드 삭제해보기</font></strong>
# </div>

node_mgmt.delete(2)
node_mgmt.desc()


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습2: 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고, 테스트해보기</font></strong><br>
# 테스트: 임의로 1 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 4인 노드의 데이터 값 출력해보기
# </div>

# +
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print ('해당 값을 가진 노드가 없습니다.')
            return
        if self.head.data == data: # 경우의 수1: self.head를 삭제해야할 경우 - self.head를 바꿔줘야 함
            temp = self.head # self.head 객체를 삭제하기 위해, 임시로 temp에 담아서 객체를 삭제했음
            self.head = self.head.next # 만약 self.head 객체를 삭제하면, 이 코드가 실행이 안되기 때문!
            del temp
        else:
            node = self.head
            while node.next: # 경우의 수2: self.head가 아닌 노드를 삭제해야할 경우
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next       
                    del temp                         
                    pass                             
                else:
                    node = node.next
                    
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


# +
# 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)


# -

# ### 7. 다양한 링크드 리스트 구조 
# * 더블 링크드 리스트(Doubly linked list) 기본 구조 
#   - 이중 연결 리스트라고도 함
#   - 장점: 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능
#   <br>
# <img src="https://www.fun-coding.org/00_Images/doublelinkedlist.png" />
# (출처: wikipedia, https://en.wikipedia.org/wiki/Linked_list)

# +
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next


# -

# ### 6. 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)
# * 다음 코드는 위의 코드에서 delete 메서드만 추가한 것이므로 해당 메서드만 확인하면 됨

# +
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == '':
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


# -

# #### 테스트를 위해 1개 노드를 만들어 봄

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# #### head 가 살아있음을 확인

linkedlist1.head

# #### head 를 지워봄(위에서 언급한 경우의 수1)

linkedlist1.delete(0)

# #### 다음 코드 실행시 아무것도 안나온다는 것은 linkedlist1.head 가 정상적으로 삭제되었음을 의미

linkedlist1.head

# #### 다시 하나의 노드를 만들어봄

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# #### 이번엔 여러 노드를 더 추가해봄

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()

# #### 노드 중에 한개를 삭제함 (위에서 언급한 경우의 수2)

linkedlist1.delete(4)

# #### 특정 노드가 삭제되었음을 알 수 있음

linkedlist1.desc()

linkedlist1.delete(9)

linkedlist1.desc()

# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습1: 위 코드에서 노드 데이터가 2인 노드 삭제해보기</font></strong>
# </div>

node_mgmt.delete(2)
node_mgmt.desc()


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습2: 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고, 테스트해보기</font></strong><br>
# 테스트: 임의로 1 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 4인 노드의 데이터 값 출력해보기
# </div>

# +
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print ('해당 값을 가진 노드가 없습니다.')
            return
        if self.head.data == data: # 경우의 수1: self.head를 삭제해야할 경우 - self.head를 바꿔줘야 함
            temp = self.head # self.head 객체를 삭제하기 위해, 임시로 temp에 담아서 객체를 삭제했음
            self.head = self.head.next # 만약 self.head 객체를 삭제하면, 이 코드가 실행이 안되기 때문!
            del temp
        else:
            node = self.head
            while node.next: # 경우의 수2: self.head가 아닌 노드를 삭제해야할 경우
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next       
                    del temp                         
                    pass                             
                else:
                    node = node.next
                    
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


# +
# 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)


# -

# ### 7. 다양한 링크드 리스트 구조 
# * 더블 링크드 리스트(Doubly linked list) 기본 구조 
#   - 이중 연결 리스트라고도 함
#   - 장점: 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능
#   <br>
# <img src="https://www.fun-coding.org/00_Images/doublelinkedlist.png" />
# (출처: wikipedia, https://en.wikipedia.org/wiki/Linked_list)

# +
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
# -


