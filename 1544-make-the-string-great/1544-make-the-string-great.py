class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        diff = ord('A') - ord('a')
        start = ord('a')
        d = {chr(start+i): chr(start+i+diff) for i in range(26)}
        
        for ch in s:
            if stack and (stack[-1] == d.get(ch, "") or d.get(stack[-1], "") == ch):
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)