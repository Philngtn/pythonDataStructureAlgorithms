class Graph:

    def __init__(self):
        self.number_of_node = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node in self.adjacent_list:
            return print(str(node) + " is in the list")
        self.adjacent_list[node] = []
        self.number_of_node += 1

    def add_edge(self, node1, node2):
        if node1 not in self.adjacent_list:
            return print(str(node1) + " is not in the list")
        
        if node2 not in self.adjacent_list:
            return print(str(node2) + " is not in the list")
        
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
        else:
            return print(str(node2) + " is in the " + str(node1))

        self.adjacent_list[node1].sort()

        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)
        else:
            return print(str(node1) + " is in the " + str(node2))
        self.adjacent_list[node2].sort()

    def show_connections(self):
        for i in self.adjacent_list:
            print(str(i) + " --> " + str(self.adjacent_list[i]))

    def depth_first_search(self):
        # Not polluted global variable
        # Using dynamic programming
        visited = [False]*self.number_of_node
        explored = []

        # Dynamic programming
        def dfs(value):
            # Explored new node, add to the list
            explored.append(value)
            # Mark the node is visted
            visited[value] = True
            for i in self.adjacent_list[value]:
                # if the node is not visited, search at that not
                if not visited[i]:
                    dfs(i)
            return explored

        return dfs  

graph = Graph()
print("Add nodes")
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)

print("Add edges")
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,4)
graph.add_edge(0,5)
graph.add_edge(0,6)
graph.add_edge(4,3)
graph.add_edge(4,7)
graph.add_edge(7,8)
graph.add_edge(8,9)

print("Show connections")
graph.show_connections()

print("Depth First Search at value 0")
# a is now the function dfs(value)
a = graph.depth_first_search()
# DFS the graph at the a(value) 
print(a(0))