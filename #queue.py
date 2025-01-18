class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        else:
            return self.queue.pop(0)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek form an empyt queue")
        else:
            return self.queue[0]
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Peek:", queue.peek())  

print("Dequeue:", queue.dequeue())  
print("Dequeue:", queue.dequeue())  

print("Is Empty:", queue.is_empty())  
print("Size:", queue.size())          

print("Dequeue:", queue.dequeue())  

print("Is Empty:", queue.is_empty())

try:
    print("Dequeue:", queue.dequeue())
except IndexError as e:
    print(e)

try:
    print("Peek:", queue.peek())
except IndexError as e:
    print(e)