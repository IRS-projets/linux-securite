#!/usr/bin/python

import time

# Lire une ligne
# Séparer les valeurs
# Mettre les "trous"
# Remplir les tablaux d'affichage

no_data = -1
processor = [no_data]*60
memory = [no_data]*60
disk = [no_data]*60

counter = 60
with open("fichier", 'r') as file:
    for line in reversed(list(file)):
        content = line.split(';')
        time_of_measure = content[0]
        processor_value = content[1]
        memory_value = content[2]
        disk_value = content[3]
        if line == 1:
            y = 0
            while int(time.time()) > time_of_measure+60*y:
                y += 1
                counter -= 1
        while time_of_measure < ((line-1).split(';')[0]) - 30:
            counter -= 1
        processor[counter] = processor_value
        memory[counter] = memory_value
        disk[counter] = disk_value
        counter -= 1

print(processor)
print(memory)
print(disk)
