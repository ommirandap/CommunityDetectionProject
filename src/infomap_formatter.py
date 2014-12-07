#!/usr/bin/python
import sys

in_file = open(sys.argv[1])
out_file = open(sys.argv[2], 'w')

comment_symbol = "#"

last_index = None
community = ""

for line in in_file:
    if line.startswith(comment_symbol):
        continue
    else:
        items = line.split()

        index = int(items[0])
        node = int(items[1])
        
        if last_index != index:
            print last_index
            if last_index != None:
                out_file.write(community.strip() + "\n")
                community = ""
            last_index = index

        community = community + str(node) + " "


out_file.write(community.strip() + "\n")

in_file.close()
out_file.close()
