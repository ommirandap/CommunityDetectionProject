#!/usr/bin/python
import snap, sys

nodes_file = open(sys.argv[1])

graph = snap.TUNGraph.New()

for line in nodes_file:
    graph.AddNode(int(line.strip()))

nodes_file.close()

edges_file = open(sys.argv[2])
comment_symbol = "#"

n_edges = 0

for line in edges_file:
    if line.startswith(comment_symbol):
        continue
    else:
        nodes = line.split()
        graph.AddEdge(int(nodes[0].strip()), int(nodes[1].strip()))
        n_edges += 1

print "Graph Loaded"

modularity = 0
communities_file = open(sys.argv[3])

for line in communities_file:
    ids = [ int(item.strip()) for item in line.split() ]

    nodes = snap.TIntV()
    
    for node_id in ids:
        nodes.Add(node_id)

    modularity += snap.GetModularity(graph, nodes, n_edges)

print modularity
