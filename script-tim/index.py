#!/usr/bin/python

import time

### Definitions
# No_data value
no_data = -1
# Arrays of values that will be displayed
processor = [no_data]*60
memory = [no_data]*60
disk = [no_data]*60
# Counter
counter = 0
# Index of the measure inside the displayed arrays
index = 0
# Table that will have all the measures and timestamps
# Format timetamp;processor;memory;disk
# Timestamp is in seconds since Epoch, the rest in used %
measures = list(tuple())
# Total quantity of measures taken
measures_lenth = 0

### Copying measures to table
with open("fichier", 'r') as file:
    for line in file:
        content = line.split(';')
        measures[measures_lenth][0] = content[0]
        measures[measures_lenth][1] = content[1]
        measures[measures_lenth][2] = content[2]
        measures[measures_lenth][3] = content[3]
        measures_lenth += 1

### "Deleting" measures that are older than 1 hour
while measures[counter][0] < int(time.time())-60*60:
    counter +=1

### Skipping display slots until we find the oldest measure that is least than 1h old
skipped_counter = 0
while measures[counter][0] > int(time.time())-60*60+skipped_counter*60:
    index += 1
    counter += 1

###  Assigning values to the display arrays
for x in range(counter, measures_lenth):
    # Adding "holes" if measures where skipped
    if x > counter:
        y = 0
        while measures[x][0] > measures[x-1][0] + 60 + 60*y:
            y += 1
            index += 1
    processor[index] = measures[x][1]
    memory[index] = measures[x][2]
    disk[index] = measures[x][3]

print(processor)
print(memory)
print(disk)
