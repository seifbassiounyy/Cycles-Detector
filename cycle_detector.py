import networkx as nxx
import matplotlib.pyplot as plt1
import csv


class CyclesFinder: #class of cycles detector
    def __init__(self):
        self.csv_data = ""              #string to hold input data in csv file
        self.parent = {}                #hash map to hold parent of each node
        self.visited = []               #array to hold visited nodes
        self.cycles = []                #array to hold cycles found in network
        self.nodes = []                 #array to hold nodes in network
        self.g1 = nxx.Graph()           #graph of given network
        self.g2 = nxx.Graph()           #graph of cycles in the given network
        self.read_csv()                 #function to read csv file
        self.construct_main_graph()     #function to construct main graph from input data
        self.find_cycles()              #function to find cycles in the network
        self.construct_cycles_graph()   #function to construct graph of cycles in network
        self.plot_graphs()              #function to plot graph of cycles in network

    def read_csv(self):
        n_rows = 0  #variable to hold number of rows in csv file
        with open("./edges.csv", 'r') as file:  #open csv file
            csvreader = csv.reader(file, delimiter=',')     #read csv file
            for row in csvreader:   #loop on rows and add each edge's nodes to csv_data variable separated with ','
                n_rows += 1     #increment number of rows in each loop
                self.csv_data = self.csv_data + row[0] + ',' + row[1] + ','
        self.csv_data = str(n_rows) + ',' + self.csv_data   #concatenate the number of rows to the beginning of the data string

    def construct_main_graph(self):
        first_line = self.csv_data.split(",")   #split the data upon ',' to get both nodes of each edge
        n = int(first_line[0])      #get the number of rows(edges) to know how many loops to iterate
        ctr = 1     #index variable for each node in each edge
        for i in range(1, n + 1):
            node1 = first_line[ctr]     #get source node of each edge
            ctr = ctr + 1
            node2 = first_line[ctr]     #get destination node of each edge
            ctr = ctr + 1
            self.g1.add_edge(node1, node2)  #add edge to graph
        pos = nxx.circular_layout(self.g1)  #draw graph
        nxx.draw(self.g1, pos, with_labels=True)    #add labels of nodes to the graph
        self.nodes = self.g1.nodes()    #get graph nodes

    def find_cycles(self):
        for node in self.nodes:
            self.parent[node] = node    #set the parent of each node as itself initially

        for node in self.nodes:
            if node not in self.visited:
                self.check(node)    #check cycles starting from each unvisited node in the graph

    def check(self, given_node):
        self.visited.append(given_node)     #append given_node to visited array
        neighbors = self.g1.neighbors(given_node)   #get neighbors of given_node
        for neighbor in neighbors:  #iterate over each neighbor of given node
            if neighbor not in self.visited:    #if neighbor is not visited
                self.parent[neighbor] = given_node  #set this node's parent as the given node
                self.check(neighbor)    #check cycles starting from neighbor node
            elif neighbor in self.visited and neighbor != self.parent[given_node] and self.parent[given_node] != given_node:
                #if neighbor node is visited and not the parent of the given node as this is undirected graph and it is not
                #the same node to avoid self loops
                temp = ""
                temp = temp + str(neighbor) #add the symbol of this neighbor node to a string
                x = given_node  #starting from given node
                while x != neighbor and self.parent[x] != x:    #keep backtracking through parent node until reaching rhe same neighbor node or a node without parent
                    temp = temp + str(x)
                    x = self.parent[x]
                self.cycles.append(temp)    #add this cycle to the cycles array

    def construct_cycles_graph(self):
        for i in self.cycles:
            for j in range(0, len(i)):
                if j != len(i) - 1:
                    node1 = i[j]    #get the first node in the edge
                    node2 = i[j + 1]    #get the second node in the edge
                    self.g2.add_edge(node1, node2)  #add edge to cycles graph
                else:   #if the last node in the string
                    node1 = i[0]    #construct an edge between the first and last node in the cycle to complete the cycle
                    node2 = i[len(i) - 1]
                    self.g2.add_edge(node1, node2)

    def plot_graphs(self):
        plt1.figure(1)  #plot the main network graph
        plt1.figure(2)  #plot the cycles graph
        pos = nxx.circular_layout(self.g2)
        nxx.draw(self.g2, pos, with_labels=True)
        plt1.show()


if __name__ == '__main__':
    cycles_finder = CyclesFinder()
