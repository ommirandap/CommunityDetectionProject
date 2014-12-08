import matplotlib.pyplot as plt
import networkx as nx
import string, sys

#file_handler = open("/home/ommirandap/U/CC-MachineLearning/proyect/com-dblp.ungraph.txt",'r')
graphFile = open(sys.argv[1],'r')

graph = nx.Graph()

print "Loading Graph"
for line in graphFile:
	
	if line.startswith("#"):
		continue
	else:
		data = line.split("\t")
		graph.add_edge(data[0].strip(),data[1].strip())

print "Graph Loaded"

communityFile = open(sys.argv[2],'r')

communities = []
print "Loading Communities"
for line in communityFile:

	if line.startswith("#"):
		continue
	else:
		community = line.split("\t")
		community = map(lambda x: int(x.strip()), community)
		communities.append(community)

print "Communities Loaded"

subgraph1 = nx.subgraph(graph, communities[10])

print subgraph1.edges()

nx.draw_spring(subgraph1)
plt.show()