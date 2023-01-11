class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # 2:02:30
    #---INSPECT---
        # INPUT: We are given 
        # n - the number of vertices,
        # edges - the list of edges connecting vertices
        # hasApple - a list containing Bool values for each vertex having an Apple
        
        #OUTPUT: We want the minimum time in seconds to collect all apples
        
        #EXAMPLE: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [F,F,T,F,T,T,F]
        
        #AXIOMS:
        # 1. We need to start at vertex 0 and end at vertex 0
        # 2. Walking over one edge of a tree costs 1 second
        
        #ASSUMPTIONS:
        # 1. If for vertex i, hasApple contains True, this means vertex i has an apple and needs to be visited
        
    #---STRATEGY---
        #SIMPLE SOLUTION:
        # Use DFS and go to the deepest level. Check if vertices at that level contains an apple.
        # If it does, we need to add 2 to the ans
        
        #RUNTIME ANALYSIS:
        # As we are using DFS to visited every vertex and this is a tree so each vertex will be visited once, TC will be O(n).
        
        #SPACE REQUIREMENT:
        #We need to convert the edges list into a graph, we will need an array/dictionary for storing the neighboring vertices for each vertex. i.e. in the form of adjacency list
        #We will need a visited array/set to not revisit vertices. Althoug since it is a tree, we might skip the visited set.
        # We will be using recursion for DFS so the space will be the auxiliary stack space consumed and SC will be O(n) in the worst case for a skewed tree where the height of the tree is maximum
        
        #BETTER SOLUTION:
        # This might be th ebest solution for this problem
        
        #ALL APPROACHES:
        
        #CONSIDER BEST CASE:
        #Regardless of containing apples, all the cases will take up O(n)
        
        #Let's start with the code
        tree = defaultdict(list)
        for vertex1, vertex2 in edges:
            tree[vertex1].append(vertex2)
            tree[vertex2].append(vertex1)
        return self.traverse(0, tree, -1, hasApple)
        
    def traverse(self, vertex, tree, parent, hasApple):
        seconds = 0
        #traverse
        for next_vertex in tree[vertex]:
            if next_vertex == parent:
                continue
            seconds += self.traverse(next_vertex, tree, vertex, hasApple)
            
        #check for apple in current vertex
        if vertex and (hasApple[vertex] or seconds > 0):
            seconds += 2
            
        #return the ans
        return seconds
        
        
        
        
        
        
        
        
        
        
        
        