# Cycles-Detector
This program is used to detect cycles in an undirected graph using matplotlib and networkx libraries in python.
It checks each node of the given graph and recursively check cycles with each unvisited neighboring node. If a 
given node has a neighbor that is connected to a visited ancestor node which is not the parent node (given node)
as this is an undirected graph, then a cycle is detected and held in the cycles array. Once all nodes are visited, we proceed
with the cycles array to draw a graph showing only the cycles found in the network. Also, an additional graph of the main given 
network is drawn to the user to show the differences between the main graph and the cycles graph. If no cycles were found in 
the network, then an empty graoh will be displayed with no cycles in it.

## How to use:
First add the rows of your graph in an excel file in csv form. The first column should contain the 
letter of the source node and the second column should contain the destination node of each edge.
Name the file as "edges" and make sure it is in csv form and put it in the same directory as your python file.
Run the python file and check the shown graphs to see the cycles found in the graph.

## Sample run:
### edges.csv file containing edges of the graph
![Screenshot 2023-07-20 021641](https://github.com/seifbassiounyy/Cycles-Detector/assets/104737465/1fd6d02b-d9e2-4e62-baf3-a3c11e5c8cf0)

### Main network graph
![Screenshot 2023-07-20 021619](https://github.com/seifbassiounyy/Cycles-Detector/assets/104737465/43642774-d343-42c2-8d7a-d5812637ed2c)

### Detected cycle graph
![Screenshot 2023-07-20 021608](https://github.com/seifbassiounyy/Cycles-Detector/assets/104737465/a7dee005-3f75-45fb-9d8e-da7476d3d078)


