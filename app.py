#!/usr/bin/python
import sys
file = open("text.txt","r");
input = [];
location = 0;
for line in file:
    input.append(line);
for str in input:
    sys.stdout.write(str);
sys.stdout.write("\n");