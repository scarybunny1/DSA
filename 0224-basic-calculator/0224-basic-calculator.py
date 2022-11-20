class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        stack = []
        num = 0
        res = 0
        while i < n:
            if s[i].isdigit():
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                continue
            if s[i] == '-':
                res += sign * num
                sign = -1
                num = 0
            elif s[i] == '+':
                res += sign * num
                sign = 1
                num = 0
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif s[i] == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
            i += 1
        return res + sign*num