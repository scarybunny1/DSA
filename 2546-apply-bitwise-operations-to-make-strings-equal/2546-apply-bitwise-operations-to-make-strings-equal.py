class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True
        if s.count('0') == len(s) or target.count('0') == len(target):
            return False
        return True