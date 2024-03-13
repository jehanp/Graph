

class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return (self.items==[])
    
    def empty_and_print(self):
        while not self.is_empty():
            print(s.pop(), end=" ")
    
s = Stack()
s.push(54)
s.push(45)
s.push("+")
s.empty_and_print()
print(s.is_empty())