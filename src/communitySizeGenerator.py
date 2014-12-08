from networkx.utils import powerlaw_sequence
import sys, math

nNodos = int(sys.argv[1])
nComunidades = int(nNodos * 0.01)
exp = float(sys.argv[2])

sequence = powerlaw_sequence(nComunidades, exponent = exp)
sequence = map(lambda x : int(math.fmod(4 + int(x), nNodos)), sequence)

for i in sequence:
	print i