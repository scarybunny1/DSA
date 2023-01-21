class Solution:
    def insert(self, i, s, arr, res):
        if i == len(s):
            if len(arr) == 4:
                res.append(".".join(list(arr)))
            return
        
        #add to new num
        arr.append(s[i])
        self.insert(i+1, s, arr, res)
        arr.pop()
        
        #add to prev num
        if arr:
            prev = arr.pop()
            if prev == '0':
                arr.append(prev)
                return
            new_num = prev + s[i]
            if 0 <= int(new_num) <= 255:
                arr.append(new_num)
                self.insert(i+1, s, arr, res)
                arr.pop()
            arr.append(prev)
            
        
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.insert(0, s, [], res)
        return res