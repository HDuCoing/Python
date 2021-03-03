# Python code for graph algorithms introduced in Lectures 13-15
import heapq

print("Graph algorithms")
print()

graph1 = {'0': ['1', '2'],
         '1': ['0', '3', '4'],
         '2': ['0', '4'],
         '3': ['1', '4'],
         '4': ['1', '2', '3', '5'],
         '5': ['4', '6'],
         '6': ['5']}

dag_graph = {'0': ['1', '2'],
         '1': ['3', '4'],
         '2': ['4'],
         '3': ['4'],
         '4': ['5'],
         '5': ['6'],
         '6': [],
         '7': ['6']}

dir_graph = {'0': ['1', '2'],
         '1': ['3', '4'],
         '2': ['4'],
         '3': ['4'],
         '4': ['5'],
         '5': ['6'],
         '6': ['7'],
         '7': ['6']}

graph2 = {'0': [('1', 2), ('2',4)],
         '1': [('0',1), ('3',2), ('4',7)],
         '2': [('0',6), ('4',3)],
         '3': [('1',2), ('4',1)],
         '4': [('5',1), ('6',1)],
         '5': [('4',2), ('6',3)],
         '6': [('5',3)]}

def dfs(visited, graph, vertex):
        print (vertex)
        visited.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour)
print("depth-first search order for graph1")
dfs([], graph1, '0')

print()


def bfs(visited, queue, graph, vertex):
  visited.append(vertex)
  queue.append(vertex)

  while queue != []:
    # dequeue next vertex
    next = queue.pop(0) 
    print (next, end = " ") 

    for neighbour in graph[next]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("breadth-first search order for graph1")
bfs([], [], graph1, '0')

print()
print()

# this version only works for acyclic directed graphs
# will give an incorrect result for a graph that contains a cycle
def topological_sort(graph):
    stack = []
    visited = []

    def recursive_helper(vertex):
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                recursive_helper(neighbour)
        stack.insert(0, vertex)           

    for vertex in graph:
        if vertex not in visited:
           recursive_helper(vertex)
    return stack



print("topological-sort order for dag-graph")
print(topological_sort(dag_graph))
print("topological-sort order for dir-graph (has a cycle)")
print(topological_sort(dir_graph))

# this version checks for cycles first off, using a dfs
def ts(graph):

    def cycle_check(visited, graph, vertex, cycles):
        visited.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                cycles = cycle_check(visited, graph, neighbour, False)
            else:
                cycles = True
        return cycles
                
    for vertex in graph:
        cycles = cycle_check([], graph, vertex, False)
        
        
    if cycles:
            print("cyclic input graph")
            return None
    else:
            return topological_sort(graph)
        
print("topological-sort1 order for dag-graph")
print(ts(dag_graph))
print("topological-sort1 order for dir-graph (has a cycle)")
print(ts(dir_graph))


print()

def getIndex(vertex, heap):
    i = 0
    while heap[i][1] != vertex:
        i +=1
    return i

def dijkstra(graph, start_vertex):

  seen = []
  distances = []
  predecessor = {}
  for vertex in graph:
      distances.append([float("inf"), vertex])
      predecessor[start_vertex] = ('00', 0)
  distances[0] = [0, start_vertex]
  heapq.heapify(distances)
  
  for i in range(len(graph)):
      
      next = heapq.heappop(distances)
      min_cost = next[0]
      vertex = next[1]
      seen.append(vertex)
      #expand this vertex
      for neighbour in graph[vertex]:
          if neighbour[0] not in seen:
              nInd = getIndex(neighbour[0], distances)
              if min_cost + neighbour[1] < distances[nInd][0]:
                  distances[nInd][0] = min_cost + neighbour[1]
                  predecessor[neighbour[0]] = (vertex, distances[nInd][0])
      heapq.heapify(distances)
  return(predecessor)
      

def printPath(pred, start, key): 
        if  key == start :  
            print(key, end =" ")
            return
        else:
            printPath(pred, start, pred[key][0]) 
            print(key, end =" ")
          

def printSolution(pred, start): 
    
        src = start
        print("Vertex \t\tDistance from Source\t\tPath") 
        for key in pred.keys(): 
            #print(key)
            print("\n%s --> %s \t\t%s \t\t\t\t" % (src, key, pred[key][1]), end = "")
            printPath(pred, start, key) 
            print()
  
print("output of Dijkstra's algorithm for graph2")
print()
paths = dijkstra(graph2, '0')
printSolution(paths, '0')


