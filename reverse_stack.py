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
        
def reverse_str(stra):
    s=Stack()
    rev_str=""
    for i in stra:
        s.push(i)
    while not s.is_empty():
        rev_str+= s.pop()
    return rev_str

input_string = "hello"
print(reverse_str(input_string))
