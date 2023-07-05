# Graphs are data structures which contain nodes or vertices, which are connected to each other through edges.
# Tress and Linked Lists are basically graphs having nodes and connections between the nodes.
# Graphs are primarily classified by three properties - Cyclic/Acyclic, Weighted/Unweighted/, Directed/Undirected.

# Graphs can be represented in 3 ways - Adjacency List, Adjacency Matrix, Edge List.

class Graph:
    def __init__(self):
        self.numOfNodes = 0
        self.adjacentList = {}
    
    def __str__(self):
        return str(self.__dict__)
    
    def addVertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList[node] = []
            self.numOfNodes += 1
            return
        return "Node already exists"
    
    def addEdge(self, node1, node2): # undirected graph
        if node2 not in self.adjacentList[node1]:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
            return
        return "Edge already exists"

    def showConnections(self):
        for vertex, neighbors in self.adjacentList.items():
            print(vertex, end='--->')
            print(' '.join(neighbors))

my_graph = Graph()
my_graph.addVertex('0')
my_graph.addVertex('1')
my_graph.addVertex('2')
my_graph.addVertex('3')
my_graph.addVertex('4')
my_graph.addVertex('5')
my_graph.addVertex('6')
my_graph.addEdge('3', '1')
my_graph.addEdge('3', '4')
my_graph.addEdge('4', '2') 
my_graph.addEdge('4', '5') 
my_graph.addEdge('1', '2') 
my_graph.addEdge('1', '0') 
my_graph.addEdge('0', '2') 
my_graph.addEdge('6', '5')
print(my_graph)
my_graph.showConnections()