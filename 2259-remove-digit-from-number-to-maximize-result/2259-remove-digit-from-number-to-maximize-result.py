class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for i in range(len(number)-1, -1, -1):
            if number[i] == digit:
                max_num = max(max_num, int(number[:i]+number[i+1:]))
        return f"{max_num}"