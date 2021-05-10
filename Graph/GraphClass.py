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



graph = Graph()

graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)

graph.show_connections()
