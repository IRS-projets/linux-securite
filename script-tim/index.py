#!/usr/bin/python

#import time

def Draw_Graph(values, type):
    max_height = 100
    if type == "processor":
        color = ["lightblue", "blue"]
    if type == "memory":
        color = ["pink", "purple"]
    if type == "disk":
        color = ["lightgreen", "green"]
    for x in range(60):
        value = values[x]
        if value == no_data:
            print('''div class="no_data"></div>''')
        if value == 0:
            print('''<div class="bar" style="height: 0px; margin-top: ''' +
                  max_height + '''px;">''')
        if value > 0:
            height = (index/100) * max_height
            margin = max_height - height
            print('''<div class="bar" style="height:''' + str(height) + '''px; margin-top: ''' +
                  str(margin) + '''px; background: ''' + str(color[0]) + '''; border-color: ''' + str(color[1]) + '''">''')

# Definitions
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

# Copying measures to table
with open("fichier", 'r') as file:
    for line in file:
        content_txt = line.split(';')
        content_int = [int(content_txt[0]), int(content_txt[1]),
                       int(content_txt[2]), int(content_txt[3])]
        measures.append(content_int)
        measures_quantity += 1

# Assigning values to the display arrays
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

print("Content-type: text/html\n\n")
print('''
<!DOCTYPE html>

<head>
    <title>
        Performances
    </title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <div class="winwow">
        <div class="window_header">
            <button class="custom_button">Reload</button>
        </div>
        <div class="window_content">
            <div class="metric">
                Processor: X%
                <div class="graph">
                ''' + Draw_Graph(processor, "processor") + '''</div>
            </div>
            <div class="metric">
                Memory: X%
                <div class="graph">
                ''' + Draw_Graph(memory, "memory") + '''</div>
            </div>
            <div class="metric">
                Disk: X%
                <div class="graph">
                ''' + Draw_Graph(disk, "disk") + '''</div>
            </div>
        </div>
    </div>
</body>
''')
