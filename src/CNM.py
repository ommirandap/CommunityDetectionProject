#!/usr/bin/python
import snap, sys

nodes_file = open(sys.argv[1])

graph = snap.TUNGraph.New()

for line in nodes_file:
    graph.AddNode(int(line.strip()))

nodes_file.close()

edges_file = open(sys.argv[2])
comment_symbol = "#"
edges = 0
for line in edges_file:
    if line.startswith(comment_symbol):
        continue
    else:
        nodes = line.split()
        graph.AddEdge(int(nodes[0].strip()), int(nodes[1].strip()))
        edges += 1

communities = snap.TCnComV()

modularity = snap.CommunityCNM(graph, communities)

print modularity

