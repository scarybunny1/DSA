class Solution:
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    def getNextCharIndex(self, i, arr):
        while i < len(arr) and arr[i] == ' ':
            i += 1
        return i
    
    def getNextEmptyIndex(self, i, arr):
        while i < len(arr) and arr[i] != ' ':
            i += 1
        return i - 1
    
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))
        
        
        #In place algorithm
        
#         arr = list(s)
#         n = len(arr)
#         self.reverse(arr, 0, len(arr)-1)
#         left = right = 0
#         while left < n and right < n:
            
#             left = self.getNextCharIndex(left, arr)
#             right = self.getNextEmptyIndex(left, arr)
            
#             self.reverse(arr, left, right)
            
#             left = right + 2
        
#         left = right = 0
#         while right < n:
#             while right < n and arr[right] == ' ':
#                 right += 1
#             if right == n:
#                 break
#             arr[left] = arr[right]
#             right += 1
#             left += 1
        
#         return "".join(arr[:left])
        
        
        # the sky is blue
        # eulb si yks eht
        # blue is sky the