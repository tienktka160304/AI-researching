class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
myStack = Stack()

#push
myStack.push('A')
myStack.push('d')
myStack.push('e')
print(myStack)

#pop
print(myStack.pop())

#isEmpty
print(myStack.isEmpty())

#Peek
print(myStack.peek())

#Size
print(myStack.size())