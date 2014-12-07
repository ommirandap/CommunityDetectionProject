#!/bin/bash

in_file=$1
sizes_file=$2
out_file=$3

`rm -f $out_file`
`touch $out_file`

while read line
do
    `sort -R $in_file | head -$line | xargs  >> $out_file`
done < $sizes_file
