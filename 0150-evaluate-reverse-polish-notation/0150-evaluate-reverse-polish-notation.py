class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {"+": lambda x, y: x + y,"-": lambda x, y: x - y,"*": lambda x, y: x * y,"/": lambda x, y: int(x / y),}
        stack = []
        for char in tokens:
            if char in "+-*/":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(f"{operation[char](first, second)}")
            else:
                stack.append(char)
        return int(stack.pop())