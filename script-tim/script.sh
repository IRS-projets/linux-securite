#!/bin/bash

# - Récupéreer les infos date, processeur, mémoire et disque
# - Les append dans un fichier de log avec la date
# - Supprimer les lignes en trop

file="/var/www/html/projetlinux.com/database"

# Recceil et conversion en % des informations
date=date +"%T"
processor=mpstat | awk '$12 ~ /[0-9.]+/ { print 100 - $12 }'
memory=free -m used*100/total
disk=df -t ext4 

# Ecriture de la ligne de log
"${date};${processor};${memory};${disk}" >> file
# Troncature du fichier
tail -n 120 file >> file
