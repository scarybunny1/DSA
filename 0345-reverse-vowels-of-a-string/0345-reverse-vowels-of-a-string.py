class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        word = list(s)
        left, right = 0, len(word)-1

        while left < right:
            while left < right and word[left] not in vowels:
                left += 1
            
            while left < right and word[right] not in vowels:
                right -= 1
            
            if left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
        return "".join(word)