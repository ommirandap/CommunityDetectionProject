from networkx.utils import powerlaw_sequence
import sys

nNodos = int(sys.argv[1])
exp = float(sys.argv[2])
sequence = powerlaw_sequence(nNodos, exponent = exp)
sequence = map(lambda x : 4 + int(x), sequence)

for i in sequence:
	print i