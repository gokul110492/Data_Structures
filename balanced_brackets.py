from stack import Stack
 
def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    if p1 == '{' and p2 == '}':
        return True
    return False
def is_balanced(paren):
    s = Stack()
    n = len(paren)
    str_balanced = True
    i = 0
    while i < n and str_balanced:
        if paren[i] in '([{':
            s.push(paren[i])
        else:
            if s.is_empty():
                str_balanced = False
                break
            elif is_match(s.peek(), paren[i]):
                s.pop()
            else:
                str_balanced = False
                break
        i = i + 1
    if s.is_empty() and str_balanced:
        return True
    else:
        return False

print(is_balanced("([])"))
print(is_balanced("{}"))
print(is_balanced("{}{}"))
print(is_balanced("(({[]}))"))
print(is_balanced("(()"))
print(is_balanced("{{{)}]"))
print(is_balanced("[][]]]"))

    
