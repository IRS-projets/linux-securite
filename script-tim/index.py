#!/usr/bin/python

import time

### Definitions
# No_data value
no_data = -1
# Arrays of values that will be displayed
processor = [no_data]*60
memory = [no_data]*60
disk = [no_data]*60
# Index of the measure inside the displayed arrays
index = 0
# Table that will have all the measures and timestamps
# Format timetamp;processor;memory;disk
# Timestamp is in seconds since Epoch, the rest in used %
measures = list()
# Total quantity of measures taken
measures_quantity = 0

### Copying measures to table
with open("fichier", 'r') as file:
    for line in file:
        content_txt = line.split(';')
        content_int = [int(content_txt[0]), int(content_txt[1]),int(content_txt[2]),int(content_txt[3])]
        measures.append(content_int)
        measures_quantity += 1

###  Assigning values to the display arrays
for x in range(0, measures_quantity):
    # Adding "holes" if measures where skipped
    if x > 0:
        y = 0
        while measures[x][0] > measures[x-1][0] + 60 + 60*y:
            y += 1
            index += 1
    processor[index] = measures[x][1]
    memory[index] = measures[x][2]
    disk[index] = measures[x][3]
    index += 1
