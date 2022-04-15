import sys

class queue:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack)==0:
            return True
        return False

if __name__ =="__main__":
    s = stack()
    a = input()
    s.push(a)
    s.push(2)
    s.push(3)
    print(s.peek())