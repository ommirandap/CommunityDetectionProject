import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.axes as axs
import sys, string
import math as m

file_handler = open(sys.argv[1],'r')

histArray = []

for line in file_handler:

	if line.startswith("#"):
		continue
	else:
		data = line.split("\t")
		nNodes = len(data)
		histArray.append(nNodes)
'''
n, bins, patches = plt.hist(histArray, bins=range(0, max(histArray), 10),log=True, facecolor='green', alpha=0.75, align='mid')
print n
print bins
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([0, 8000, 0, 2000])
plt.grid(True)

plt.show()
'''
sortedArray = sorted(histArray)
#print sorted(histArray)
maxH = max(histArray)
occu = range(maxH+1)

for i in range(len(occu)):
	occu[i] = 0

for i in range(len(sortedArray)):
	j = sortedArray[i]
	occu[j] = occu[j] + 1

#print occu

y = np.arange(0, len(occu), 1)
#fig = plt.loglog(y, occu)
fig = plt.plot(y, occu)
plt.axis([0, max(occu), 0, maxH])
plt.savefig('miau.png')
plt.show()