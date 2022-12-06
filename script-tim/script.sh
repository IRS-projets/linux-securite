#!/bin/bash

# Fichier contenant les releves
#file="/var/www/html/projetlinux.com/database"
file="/var/www/html/projetlinux.com/script/fichier"

### Recueil et conversion en % des informations
# Date au format hh:mm:ss
date=$(date +"%s")
# Processeur: 100 - taux de repos
processor=$(mpstat | awk '$12 ~ /[0-9.]+/ { print 100 - $12 }' | cut -d "," -f 1)
# Memoire disponible
memoryTotal=$(free | awk 'NR==2{ print $2}')
# Memoire utilisee
memoryUsed=$(free | awk 'NR==2{ print $3}')
# Memoire en %
memory=$((memoryUsed*100/memoryTotal))
# Disque: volume utilise
disk=$(df -t ext4 | awk 'NR==2{ print $5}' | grep -Eo '[0-9]{1,3}') 

### Ecriture du fichier
# Ligne de log
echo "${date};${processor};${memory};${disk};" >> $file
# Troncature du fichier
echo "$(tail -n 60 $file)" > $file
