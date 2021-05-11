import string

class Graph_undirected_weighted:

    def __init__(self):
        self.number_of_node = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node in self.adjacent_list:
            return print(str(node) + " is in the list")
        self.adjacent_list[node] = []
        self.number_of_node += 1

    def add_edge(self, node1, node2, value):
        # Checking whether node is in the list or not
        if node1 not in self.adjacent_list:
            return print(str(node1) + " is not in the list")
        if node2 not in self.adjacent_list:
            return print(str(node2) + " is not in the list")
        
        # Checking whether node A already has a connection to node B
        if node2 not in self.adjacent_list[node1]:
            # If Node A does not have that connection with other Node BB 
            self.adjacent_list[node1].append([node2,value])
        else:
            # Node A already has a connection with node B
            return print(str(node2) + " is in the " + str(node1))
        
        # Sorting the node for easy checking 
        self.adjacent_list[node1].sort()

        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append([node1,value])
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

        
    def dktra_matrix(self, value):
        visted = []
        unvisited = list(self.adjacent_list.keys())
        table =  [[0 for i in range(3)] for j in range(len(unvisited))]
        for i in unvisited:
            for j in range(3):
                if j == 0:
                    table[i][j] = i
                else:
                    table[i][j] = 0
                if j == 1:
                    if i == value:
                        table[i][j] = 0
                    else:
                        table[i][j] = float('inf')
                if j == 2:
                    table[i][j] = None

        # print(table)

        def smallest_distance_unvisited():
            smallest = float('inf') 
            for i in table:
                if i[1] < smallest and i[0] not in visted: 
                   smallest = i[1]
                   location = i[0]

            return location

        while unvisited:
            current_vertex = smallest_distance_unvisited()
            for neighbour in self.adjacent_list[current_vertex]:
                distance = table[current_vertex][1] + neighbour[1]
                if distance < table[neighbour[0]][1]:
                    table[neighbour[0]][1] = distance
                    table[neighbour[0]][2] = current_vertex
            visted.append(current_vertex)
            unvisited.remove(current_vertex)

        return table

    # Visualized the matrix with labeled node in alphabel
    def visualize_matrix(self, visualize_matrix):
        alphabet = list(map(chr,range(65, 65 + self.number_of_node)))
        for i in visualize_matrix:
            i[0] = alphabet[i[0]]
            if i[2] != None:
                i[2] = alphabet[i[2]]
        print(visualize_matrix)

    def shortest_path(self, start, end):
        table = self.dktra_matrix(start)
        shortest_path = []
        shortest_path.append(end)

        # Recursive function
        def trace_back(end):
            if end == start:
                return 0
            shortest_path.append(table[end][2])            
            trace_back(table[end][2])
        
        # Recursive function
        trace_back(end)

       
        # Convert to Alphabel for visualization
        alphabet = list(map(chr,range(65, 65 + self.number_of_node)))
        for i, value in enumerate(shortest_path):
            shortest_path[i] = alphabet[value]
            
        
        # Print the shortest path backward from START - END
        print(shortest_path[::-1])
    
        return shortest_path


graph = Graph_undirected_weighted()
# print("Add nodes")
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)


# print("Add edges")
graph.add_edge(0,1,6)
graph.add_edge(0,3,1)
graph.add_edge(1,3,2)
graph.add_edge(1,2,5)
graph.add_edge(3,4,1)
graph.add_edge(1,4,2)
graph.add_edge(2,4,5)

# print("Show connections: ")
# # graph.show_connections()

# print("Show the adjacent: ")
# # print(graph.adjacent_list)

# print("Show the Dijktra 2D Array: ")
# Array2D = graph.dktra_matrix(0)
# print(Array2D)

# print("Show the Dijktra 2D Array with labeled-alphabel: ")
# graph.visualize_matrix(Array2D)


print("Show the shortest part: ")
graph.shortest_path(0,2)
