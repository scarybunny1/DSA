class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split()
        prev = arr[0][-1]
        for i in range(1, len(arr)):
            if prev != arr[i][0]:
                return False
            prev = arr[i][-1]
        return prev == arr[0][0]