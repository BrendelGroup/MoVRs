#!/usr/bin/bash
file=$1
fold=$2
suffix=$3

total_lines=$(wc -l <${file})
((lines_per_file=(total_lines+fold-1)/fold))

split -d --lines=$lines_per_file $file $suffix"." # use numeric suffix

echo "Total lines = $total_lines"
echo "Lines per file = $lines_per_file"
wc -l $suffix"."*
