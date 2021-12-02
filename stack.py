class Stack():
    def __init__(self):
        self.items=[]

    def push(self, item):
        """ Push an element in to the stack """
        self.items.append(item)
    
    def pop(self):
        """ Delete an element and print it """
        return self.items.pop()
        
    def is_empty(self):
        """ Check if stack is empty """
        return self.items == []
        
    def peek(self):
        """ Print top elemet in the stack """
        return self.items[-1]
    
    def get_stack(self):
        """ Print all elements in the stack """
        return self.items
        
s=Stack()
print(s.is_empty())
s.push(5)
s.push(10)
s.push(2)
print(s.peek())
print(s.pop())
print(s.get_stack())