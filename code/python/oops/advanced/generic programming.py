from typing import Generic, TypeVar, List

T = TypeVar('T')                # define a type of variable -> represent for any kind of types

class Stack(Generic[T]):         # define a lass generic-> can work with any kind of types
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T):
        self.items.append(item)
        
    def pop(self) -> T:
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty!")
    
    def peek(self) -> T:
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty!")
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)
    
int_stack = Stack[int]()        # only contain int
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack.pop())          # 3
print(int_stack.peek())         # 2

str_stack = Stack[str]()        # only contain string
str_stack.push('hehe huhu heh')
str_stack.push('uh')
print(str_stack.pop())          # uh
print(str_stack.peek())         # hehe huhu heh