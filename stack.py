class Stack():
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return "Stack is empty" if self.empty() else self.stack.pop()
    
    def peek(self):
        return "Stack is empty" if self.empty() else self.stack[-1]

    def empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)