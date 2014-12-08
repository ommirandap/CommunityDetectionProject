#!/usr/bin/python
import sys

in_file = open(sys.argv[1])

comment_symbol = "#"

last_index = None
community = ""

for line in in_file:
    if line.startswith(comment_symbol):
        continue
    else:

        items = line.split()

        index = int(items[0][0:items[0].index(":")])
        node = int(items[3])
        
        if last_index != index:
            if last_index != None:
                print community.strip() 
                community = ""
            last_index = index

        community = community + str(node) + " "


print community.strip()

in_file.close()
