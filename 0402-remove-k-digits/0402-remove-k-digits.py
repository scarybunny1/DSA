class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
#         1 u 4 d 3 d 2 e 2 d 1 u 9
        
#         9                           o
#         4       o
#         3           o
#         2               o   o
#         1   o                   o
#             0   1   2   3   4   5   6
        
#         1. stack = [1,2,1,9]
#         2. stack = [0,2,0,0]
#         3. stack = [1,0]

        stack = [] #monotonically increasing stack
        for ch in num:
            while stack and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)
        n = len(stack)
        ans = "".join(stack[:n-k])
        
        #Remove leading zeroes
        zeroes = 0
        for ch in ans:
            if ch == '0':
                zeroes += 1
            else:
                break
        return "0" if ans[zeroes:] == "" else ans[zeroes:]