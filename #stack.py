class Stack():
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            raise IndexError("Pop from an empty stack")
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.empty():
            raise IndexError("Peek from and empty stack")
        else:
            return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

stack = Stack()
stack.push(10)
stack.push(5)

print("Peek:", stack.peek())  

print("Pop:", stack.pop())    
print("Is Empty:", stack.empty())  
print("Size:", stack.size())  

print("Pop:", stack.pop())    

print("Is Empty:", stack.empty())  

try:
    print("Pop:", stack.pop())  
except IndexError as e:
    print(e)  

try:
    print("Peek:", stack.peek())  
except IndexError as e:
    print(e)  