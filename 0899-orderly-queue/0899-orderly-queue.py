class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            order = []
            for i in range(len(s)):
                new_string = s[i:] + s[:i]
                order.append(new_string)
            return sorted(order)[0]
        else:
            return "".join(sorted(s))