class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.key_to_freq = defaultdict(int)
        self.freq_to_key = defaultdict(OrderedDict)
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        #Get freq from the key:freq pair dictionary
        freq = self.key_to_freq[key]
        
        #Update the freq since it has been used one more time
        self.key_to_freq[key] += 1
        
        #Fetch the value from freq:{key:value} dictionary
        value = self.freq_to_key[freq][key]
        
        #Delete the key with old freq value
        del self.freq_to_key[freq][key]
        
        #Insert the key in the updated freq group
        self.freq_to_key[freq+1][key] = value
        
        #Check for change in min_freq
        if self.min_freq == freq and len(self.freq_to_key[freq]) == 0:
            self.min_freq += 1
            
        return value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.key_to_freq:
            #As it is used once more, follow the steps same as get(key)
            self.get(key)
            
            #Update the value stored in cache to the current value
            self.freq_to_key[self.key_to_freq[key]][key] = value   
        else:
            #Check for overflow
            if self.size == self.capacity:
                #Remove a key from min_freq group
                k, v = self.freq_to_key[self.min_freq].popitem(False)
                
                #Delete the key:freq pair permanently from the cache
                del self.key_to_freq[k]
                
                #Update the size of the cache
                self.size -= 1
            
            #Add the current key:value pair in cache
            self.key_to_freq[key] = 1
            self.freq_to_key[1][key] = value
            self.min_freq = 1
            
            #Update the size of the cache
            self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)