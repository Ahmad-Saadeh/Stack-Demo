class Stack():

    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("The stack is empty")

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items)==0

    def get_stack(self):
        return self.items

mystack = Stack()
mystack.push(1); mystack.push(2); mystack.push(3)
mystack.pop();
print(mystack.get_stack())
