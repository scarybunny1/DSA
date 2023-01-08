class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for k1 in "abcdefghijklmnopqrstuvwxyz":
            if c1[k1] == 0:
                continue
            for k2 in "abcdefghijklmnopqrstuvwxyz":
                if c2[k2] == 0:
                    continue
                c1[k2] += 1
                c2[k1] += 1
                c1[k1] -= 1
                c2[k2] -= 1
                if c1[k1] <= 0:
                    del c1[k1]
                if c2[k2] <= 0:
                    del c2[k2]
                count1 = count2 = 0
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c1[c] > 0:
                        count1 += 1
                    if c2[c] > 0:
                        count2 += 1
                if count1 == count2:
                    return True
                c1[k2] -= 1
                c2[k1] -= 1
                c1[k1] += 1
                c2[k2] += 1
        return False