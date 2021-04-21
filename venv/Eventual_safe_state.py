class Solution:

    def __init__(self):
        self.visited = []

    def eventual_safe_nodes(self,graph: List[List[int]]) -> List[int]:
        # store safe nodes list
        safe_nodes = []

        # store visited status of node, 0-> not visited, 1 ->visited, 2 -> safe
        # initialize all nodes with status 0
        self.visited = [0 for _ in range(len(graph))]

        # perform dfs with each node as starting node
        for n in range(len(graph)):
            # function returns true if node is safe
            if self.dfs(graph,n):
                safe_nodes.append(n)

        return safe_nodes

    def dfs(self,graph,node):
        # check status of node. If it has been visited, check if it is safe
        if self.visited[node] != 0:
            return self.visited[node] == 2

        # mark node as visited
        self.visited[node] = 1

        # visit the nodes neighbours and mark as unsafe if not safe.
        for neighbour in graph[node]:
            if not self.dfs(graph,neighbour):
                return False

        # mark node as safe if all its neighbours return true
        self.visited[node] = 2
        return True

