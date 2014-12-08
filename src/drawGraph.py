#!/usr/bin/python
import sys, math
import networkx as nx
import matplotlib.pyplot as plt

nodes_file = open(sys.argv[1])

graph = nx.Graph()

for line in nodes_file:
    graph.add_node(int(line.strip()))

nodes_file.close()

edges_file = open(sys.argv[2])
comment_symbol = "#"

for line in edges_file:
    if line.startswith(comment_symbol):
        continue
    else:
        nodes = line.split()
        graph.add_edge(int(nodes[0].strip()), int(nodes[1].strip()))

print "Graph Loaded"

'''
print "Drawing spring"

nx.draw_spring(graph)
plt.savefig("spring-sin-k.png")
#plt.show()
'''

grados = graph.degree()
meanDegree = 0
for i in grados:
    meanDegree = meanDegree + grados[i]

meanDegree = int((meanDegree/1539)*0.7)

grafito = nx.watts_strogatz_graph(1539, meanDegree, 0.5)
nx.draw_spring(grafito)
plt.savefig("watts_strogatz_graph2.png")
plt.show()

print "Drawing shell"
#nx.draw_shell(graph)
#plt.savefig("shell.png")
print "Drawing circular"
#nx.draw_circular(graph)
#plt.savefig("circular.png")
print "Drawing random"
#nx.draw_random(graph)
#plt.savefig("random.png")