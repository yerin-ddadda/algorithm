import sys

class queue:
    def __init__(self):
        self.data = []

    def push(self, item): # enqueue
        self.data.append(item)

    def size(self):
        print(len(self.data))
    
    def pop(self): #dequeue
        if len(self.data) <= 0:
            print(-1)
        else:
            print(self.data.pop(0)) #가장 먼저 들어간거 pop
        #큐의 길이가 길어질수록 시간
    
    def front(self):
        if len(self.data) <= 0:
            print(-1)
        else:
            print(self.data[0])

    def back(self):

        if len(self.data) <= 0:
            print(-1)
        else:
            print(self.data[-1])

    def empty(self):
        if len(self.data) == 0:
            print(1)
        else:
            print(0)


q = queue()

count = 0
number = int(input())

while True:
    if count >= number:
        break
    c = sys.stdin.readline().rstrip()

    if "push" in c:
        q.push(int(c[5:]))

    elif c=="pop":
        q.pop()

    elif c== "size":
        q.size()

    elif c=="empty":
        q.empty()
    
    elif c=="front":
        q.front()

    elif c=="back":
        q.back()
    
    count +=1