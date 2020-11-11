from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices #number of vertices 
  
    # function to add an edge to graph 
    def add_edge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topological_sort 
    def topological_sort_h(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topological_sort_h(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological_sort. It uses recursive  
    # topological_sort_h() 
    def topological_sort(self):
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topological_sort_h(i,visited,stack) 
  
        # Print contents of stack 
        print(stack)

g= Graph(8) 
g.add_edge(7, 5)
g.add_edge(5, 2)
g.add_edge(3, 0)
g.add_edge(3, 3)
g.add_edge(1, 7)
g.add_edge(7, 6)
g.add_edge(3, 4) 
g.add_edge(1, 3) 
g.add_edge(3, 0) 
g.add_edge(1, 2) 
g.add_edge(7, 0) 
g.add_edge(4, 0) 

g.topological_sort() # [1, 3, 4, 7, 6, 5, 2, 0]
