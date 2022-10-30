class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cache = {}
        n = len(creators)
        max_views = 0
        
        for i in range(n):
            if creators[i] not in cache:
                cache[creators[i]] = [views[i], ids[i], views[i]]
                max_views = max(max_views, views[i])
            else:
                creator = creators[i]
                #Update the total views
                updated_views = views[i] + cache[creator][0]
                cache[creator][0] = updated_views
                max_views = max(max_views, updated_views)
                
                #Update most viewed video if neccessary
                if views[i] > cache[creator][2]:
                    cache[creator][1] = ids[i]
                    cache[creator][2] = views[i]
                    
                #Update id if neccessary
                if views[i] == cache[creator][2]:
                    cache[creator][1] = sorted([ids[i], cache[creator][1]])[0]
                    
        res = []
        for creator, value in cache.items():
            if value[0] == max_views:
                res.append([creator, value[1]])
        return res