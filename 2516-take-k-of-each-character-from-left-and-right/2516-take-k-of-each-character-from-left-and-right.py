class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        s_count = Counter(s)
        required = {character: s_count[character] - k for character in "abc"}
        if any(required[c] < 0 for c in "abc"):
            return -1
        left = 0
        n = len(s)
        have = {character: 0 for character in "abc"}
        ans = -1
        for right in range(n):
            have[s[right]] += 1
            
            while have[s[right]] > required[s[right]]:
                have[s[left]] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return -1 if ans == -1 else n - ans