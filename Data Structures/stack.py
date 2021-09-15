#Stack
#Author: Thomas S
#Date 15 Sept 2021

class Stack():
    def __init__(self):
        self.stack = []

        #Push to the stack
    def _push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    #Print Stack
    def printStack(self):
        print(self.stack)

    #Print Top of stack
    def peek(self):
        print(self.stack[-1])

    #Pop from Stack
    def _pop(self):
        self.stack.pop()

#Create objec of class Stack
myStack = Stack()

#Push elements to the stack
myStack._push("Apples")
myStack._push("Oranges")

#Print Stack
myStack.printStack()
myStack.peek()


#Push elements to the stack
myStack._push("Bananas")
myStack._push("Grapes")


#Print Stack
myStack.printStack()
myStack.peek()

#Pop from Stack
myStack._pop()
myStack.printStack()
myStack.peek()
