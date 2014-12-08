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

graph.Defrag()

print "Graph Loaded"

modularity = 0.0
modularity_first = 0.0
modularity_second = 0.0

with open(sys.argv[3]) as communities_file:
    for line in communities_file:
        nodes = [ int(item.strip()) for item in line.split() ]

        if len(nodes) == 1:
            continue

        for node_id1 in nodes:
            for node_id2 in nodes:
                if node_id1 != node_id2:
                    modularity_first += (1.0 if graph.IsEdge(node_id1, node_id2) else 0.0) 
                    modularity_second -= (graph.GetNI(node_id1).GetDeg() * graph.GetNI(node_id2).GetDeg())

modularity = (1 / (2.0 * n_edges)) * (modularity_first + modularity_second/(2.0 * n_edges))

print modularity

modularity = 0.0

K = 0.0

nodeinfo = dict()

node = graph.BegNI()
end = graph.EndNI()

while True:

    nodeinfo[node.GetId()] = [ node.GetDeg(), 0 ]
   
    if node.Next() == end:
        break

with open(sys.argv[3]) as communities_file:
    for line in communities_file:
        if len(line.split()) == 1:
            continue
        K += 1
        for node in line.split():
            nodeinfo[int(node.strip())][1] += 1

modularity = 0

with open(sys.argv[3]) as communities_file:
    for line in communities_file:
        ids = [ int(item.strip()) for item in line.split() ]
        size = len(ids)

        if size == 1:
            continue

        nodes = snap.TIntV()
        
        for node_id in ids:
            nodes.Add(node_id)

        subgraph = snap.GetSubGraph(graph, nodes)

        node = subgraph.BegNI()
        end = subgraph.EndNI()

        acc = 0
        while True:

            global_degree = nodeinfo[node.GetId()][0]

            acc += (2.0 * node.GetDeg() - global_degree) / (1.0 * global_degree *
                    nodeinfo[node.GetId()][1])
            if node.Next() == end:
                break

        modularity += 2.0 * acc * subgraph.GetEdges() / ( size * size * (size - 1) )

modularity /= K

print modularity



