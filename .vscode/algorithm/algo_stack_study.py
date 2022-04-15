import sys

class ArrayStack:
    def __init__(self):
        self.data = [] #빈스택을 초기화

    def size(self):
        print(len(self.data))

    def isEmpty(self):
        if len(self.data) == 0:
            print("1")
        else:
            print("0")

    def push(self, item):
        self.data.append(item)
    

    def pop(self):
        if len(self.data) <= 0:
            return -1
        return self.data.pop()

    def top(self):
        if len(self.data) <= 0:
            return -1
        return self.data[-1]

stk = ArrayStack() #스택 객체 생성

count = 0
number = int(input())
while True:
    if count >= number:
        break
    c = sys.stdin.readline().rstrip()

    if "push" in c:
        stk.push(int(c[5:]))
       # break
    #if c == "push":
     #   stk.push(b)
    elif c == "top":
        print(stk.top())
    elif c == "size":
        stk.size()
    elif c == "pop":
        print(stk.pop())
    elif c =="empty":
        stk.isEmpty()
    count += 1

