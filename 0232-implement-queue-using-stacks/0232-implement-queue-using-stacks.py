# class MyQueue:

#     def __init__(self):
#         self.input = []
#         self.output = []

#     def push(self, x: int) -> None:
#         self.input.append(x)

#     def pop(self) -> int:
#         if not self.output:
#             while self.input:
#                 self.output.append(self.input.pop())
#         return self.output.pop()

#     def peek(self) -> int:
#         if not self.output:
#             while self.input:
#                 self.output.append(self.input.pop())
#         return self.output[-1]

#     def empty(self) -> bool:
#         return self.input == [] and self.output == []
    
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, val):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(val)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    def pop(self):
        return self.stack1.pop()
    
    def peek(self):
        return self.stack1[-1]
    
    def empty(self):
        return self.stack1 == []

        # p1 p2 p3 p4 po po p5
        # s1 = [4,3,2,1]
        # s2 = []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()