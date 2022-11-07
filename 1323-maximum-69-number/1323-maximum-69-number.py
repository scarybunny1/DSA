class Solution:
    def maximum69Number (self, num: int) -> int:
        num_string = str(num)
        n = len(num_string)
        
        for i in range(n):
            if num_string[i] == '6':
                power = int(math.pow(10, n-i-1))
                num += 3*power
                break
        return num