class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == "]":
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                
                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop()
                    
                repeat = int(num[::-1])
                
                stack.append(repeat * string)
            else:
                stack.append(ch)
        
        return "".join(stack)
#     3[z]2[2[y]pq4[2[jk]e1[f]]]ef
#                            i
#     stack = [zzz, 2, [, yy, p, q, 4, [, jkjk, e, f, ] ]
#     string = "f"
#     num = "1"
    
#     zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef