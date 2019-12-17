from collections import deque
from heapq import heappop, heappush

def rec_dfs(G,visited,s):
  """recursive dfs (Depth First Search) code implementation

  @param G: graph G represented as a adjacency list.
  @param visited: array that representing the visited nodes.
  @param s: source node.
  """
  for v in G[s]:
    if not visited[v]:
      visited[v] = True ; rec_dfs(G,visited,prev,v)

def iter_dfs(G,s):
  """iterative dfs (Depth First Search) code implementation
  
  @param G: graph G represented as a adjacency list.
  @param s: source node.
  """
  visited = [0 for _ in range(len(G))] ; visited[s] = 1
  stack = [s]
  while len(stack)!=0:
    u = stack.pop()
    for v in G[u]:
      if not visited[v]:
        stack.append(v) ; visited[v] = 1
    visited[v] = 2

def bfs(G,s):
  """bfs (Breadth First Search) code implementation
  
  @param G: graph G represented as a adjacency list.
  @param s: source node.
  """
  visited = [0 for _ in range(len(G))] ; visited[s] = 1
  queue = deque()
  queue.append(s)
  while len(queue)!=0:
    u = popleft()
    for v in G[u]:
      if not visited:
        queue.append(v) ; visited[v] = 1
    visited[u] = 2

def dijkstra(G,s):
  """Dijkstra's algorithm to solve the SSSP problem.
  
  @param G: graph G represented as a adjacency list with weights.
  @param s: source node.

  @return dist: array which stores the minimum distances between
  the source and each node.
  """
  INF = float('inf')
  dist = [INF for _ in range(len(G))] ; dist[s] = 0
  visited = [False for _ in range(len(G))]
  prev = [None for _ in range(len(G))]
  heap = [(0, s)]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not visited[u]:
      for v,dv in G[u]:
        if d+dv<dist[v]:
          dist[v] = d+dv
          heappush(heap, (dist[v], v))
          prev[v] = u
      visited[u] = True
  return dist