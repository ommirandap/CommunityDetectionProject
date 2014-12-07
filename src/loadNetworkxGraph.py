import matplotlib.pyplot as plt
import networkx as nx
import string, sys

#file_handler = open("/home/ommirandap/U/CC-MachineLearning/proyect/com-dblp.ungraph.txt",'r')
file_handler = open(sys.argv[1],'r')

graph = nx.Graph()
a = 1
for line in file_handler:
	a = a +1
	if line.startswith("#"):
		continue
	else:
		data = line.split("\t")
		graph.add_edge(data[0].strip(),data[1].strip())
	
	if a > 50:
		break

print len(graph.nodes())
print len(graph.edges())
print nx.number_connected_components(graph)
