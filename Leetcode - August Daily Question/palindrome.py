def isPalindrome(s, left, right):
    if left < right:
        return (s[left] == s[right] and isPalindrome(s, left+1, right-1))
    return True

s = "absbaababsba"
print(isPalindrome(s, 0, len(s) - 1))