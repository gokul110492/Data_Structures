from stack import Stack
def convert_int_to_bin(dec_num):
  s = Stack()
  bi = ""
  while dec_num!=0:
    r = dec_num%2
    dec_num = dec_num // 2
    s.push(r)
    
  while not s.is_empty():
    bi += str(s.pop())
  return bi
print(convert_int_to_bin(3))
