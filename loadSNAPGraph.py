import sys
import string

sys.argv[1]

#G1 = TNGraph.New()

#file_handler = open("/home/ommirandap/U/CC-MachineLearning/proyect/com-dblp.ungraph.txt",'r')
file_handler = open(sys.argv[1],'r')

for line in file_handler:

	if line.startswith("#"):
		continue
	else:
		data = line.split("\t")
		#G1.AddEdge(data[0],data[1])
		print data[0].strip()
		print data[1].strip()