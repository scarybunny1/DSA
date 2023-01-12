class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        #Check if it is at all possible to achieve desiredTotal
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        
        #Bitmasking Approach
        available = (1 << maxChoosableInteger) - 1  #If mci is 4, available will be 111
        
        return self.makeMeWin(maxChoosableInteger, available, desiredTotal, {})
    
    def makeMeWin(self, n, available, target, memo):
        if (available, target) in memo:
            return memo[(available, target)]
        for i in range(n):
            if (1 << i) & available:
                if i + 1 >= target:
                    memo[(available, target)] = True
                    return True
                if not self.makeMeWin(n, available ^ (1 << i), target - i - 1, memo):
                    memo[(available, target)] = True
                    return True
        memo[(available, target)] = False
        return False