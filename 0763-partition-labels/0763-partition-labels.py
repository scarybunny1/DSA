class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(list)
        for i, ch in enumerate(s):
            if len(d[ch]) < 2:
                d[ch].append(i)
                d[ch].append(i)
            elif len(d[ch]) == 2:
                d[ch][1] = i
        
#         a b a b c b a c a d  e  f  e  g  h  i  j  h  k  l  i  j
#         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
        
#         {a:[0,8], b:[1,5], c:[4,7], d:[9,9], e:[10,12], f:[11,11], g:[13,13], h:[14,17], i:[15,20], j:[16,21], k:[18,18], l:[19,19]}
        
        stack = []
        for interval in d.values():
            if stack and stack[-1][1] > interval[0]:
                i = stack.pop()
                new_interval = [i[0], max(i[1], interval[1])]
                stack.append(new_interval)
            else:
                stack.append(interval)
        
        ans = []
        for interval in stack:
            ans.append(interval[1] - interval[0] + 1)
        
        return ans