# Script

## Objectif

L'objectif de ce script est de faciliter le monitoring des ressources système.<br>
Il fonctionne en deux parties qui seront détaillées ci-après:

 - Log des ressources dans un fichier
     - Taux de fonction du processeur (quand il n'est pas *idle*)
     - Taux d'utilisation de la mémoire
     - Proportion du volume du disque utilisée
 - Affichage web

Ces deux parties sont indépendantes, et seule la première est écrite en BASH.

## Partie BASH

### Commandes

#### Date

Affin de loguer les différentes informations, il est important d'avoir la date des mesures.

Puisqu'on aura besoin de comparer les dates pour l'affichage des graphiques, on choisit de les stocker sous forme de secondes écoulées depuis *EPOCH*.

Ainsi, la commande pour obtenir la date sous ce format est:

```
date +"%s"
```

#### Processeur

Nous voulons obtenir le taux d'utilisation du processeur, soit la proportion du temps où il n'est pas en train d'attendre.

 - L'occupation du processeur peut être obtenue avec `mpstat`.
 - La mesure qui nous intéresse se situe en 12^e^ position, nous la récupérons avec `awk`
 - Pour obtenir la partie entière, on utilise `cut` pour prendre les valeurs avant la virgule.

La ligne de commande qui en résulte est:

```
mpstat | awk '$12 ~ /[0-9.]+/ { print 100 - $12 }' | cut -d "," -f 1
```

#### Mémoire

Utilisant `free`, on a dû faire un calcul pour obtenir le taux de mémoire utilisée en utilisant:

 - La quantité totale de mémoire
    ```
    free | awk 'NR==2{ print $2}'
    ```
 - La quantité de mémoire utilisée
    ```
    free | awk 'NR==2{ print $3}'
    ```
 - Le calcul utilisée*100/totale
    ```
    (memoryUsed*100/memoryTotal)
    ```

#### Disque

L'espace utilisé peut être trouvé en 5^e^ position dans le résultat de la commande `df -t ext4`:

```
df -t ext4 | awk 'NR==2{ print $5}' | grep -Eo '[0-9]{1,3}'
```

### Log

On utilise les commandes précédemment définies pour générer un fichier CSV de 60 lignes:

```bash title="script.sh" linenums="1"
#!/bin/bash

# Fichier contenant les releves
file="/var/www/html/projetlinux.com/script/fichier"

### Recueil et conversion en % des informations
# Date au format ssss
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
```

### Crontab

On veut faire tourner le script automatiquement chaque minute de façon a avoir 1h de logs.<br>
Pour ce faire, nous ajoutons le script dans le crontab:

```bash title="/etc/crontab/" linenums="1"
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*    *  * * *   root    /root/script.sh
```

La dernière ligne du fichier correspond au script. Les `*` signifient que le script tourne a chaque minute, de chaque heure de chaque jour.

## Partie web

### Script

La partie web consiste en un script en Python qui est lancé par Apache.

Ce scrip lit le fichier CSV précédemment généré, place ses valeurs dans différents tableaux et les place dans des endroits spécifiques d'un template HTML.
Il retourne ensuite l'HTML qui est interprété par le navigateur web du client.

Le script est construit de la façon qui suit:

 - Le fichier CSV est lu et placé dans un tableau.
 - Les valeurs de chaquaque capteur sont recopiées dans un tableau associé (processeur, mémoire et disque) en sautant une case quand la différence de temps entre les mesures est suppérieure à une minute
 - Les graphiques sont injectés dans le template HTML grâce à la fonction `Draw_Graph`.

Voici le script en entier.
Il a été réalisé entièrement à la main, sans bibliothèques.

!!! danger "Attention aux yeux"
    Nous avons manqué de temps pour le développement.
    Le script a été écrit dans la précipitation, et en partie recopié sur le premier script de Tim (voir sources).

    Nous vous prions de ne pas lire ce qui suit sans protection occulaire.

```py title="/var/www/html/projetlinux.com/script/index.py" linenums="1"
#!/usr/bin/python

import time

def Draw_Graph(values, type):
    max_height = 100
    color = ["black", "black"]
    if type == 1:
        color = ["lightblue", "blue"]
    if type == 2:
        color = ["pink", "purple"]
    if type == 3:
        color = ["lightgreen", "green"]
    for x in range(len(values)):
        value = values[x]
        if value == no_data:
            print('''<div class="no_data"></div>''')
        if value == 0:
            print('''<div class="bar" style="height: 0px; margin-top: ''' +
                  str(max_height) + '''px;"></div>''')
        if value > 0:
            height = (value/100) * max_height
            margin = max_height - height
            print('''<div class="bar" style="height:''' + str(height) + '''px; margin-top: ''' +
                  str(margin) + '''px; background: ''' + str(color[0]) + '''; border-color: ''' + str(color[1]) + '''"></div>''')

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

# "Deleting" measures that are more than an hour old
y = 0
while measures[y][0]<int(time.time())-60*60 and y < 58:
    y += 1
# Assigning values to the display arrays
for x in range(y, measures_quantity-1):
    # Adding "holes" if measures where skipped
    if x > 0:
        y = 0
        while measures[x][0] > measures[x-1][0] + 65 + 60*y:
            y += 1
            index += 1
    if index < 60:
        processor[index] = measures[x][1]
        memory[index] = measures[x][2]
        disk[index] = measures[x][3]
        index += 1
    else:
        break

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
            <button class="custom_button" onClick="window.location.reload(true)">Reload</button>
        </div>
        <div class="window_content">
            <div class="metric">
                Processor: ''' + str(processor[index-1]) + '''%
                <div class="graph">
                ''')
Draw_Graph(processor, 1)
print('''</div>
            </div>
            <div class="metric">
                Memory: ''' + str(memory[index-1]) + '''%
                <div class="graph">
                ''')
Draw_Graph(memory, 2)
print('''</div>
            </div>
            <div class="metric">
                Disk: ''' + str(disk[index-1]) + '''%
                <div class="graph">
                ''')
Draw_Graph(disk, 3)
print('''</div>
            </div>
        </div>
    </div>
</body>
''')

```

### Configuration du système

Télécharger Python 3:

```
apt install python3
```

Ajouter Python dans *PATH* pour la session qui lance le script:

```bash title="A la suite de .profile" linenums="11"
export PATH="$PATH:/usr/bin/python:/usr/bin/python3"
```

### Configuration d'Apache

Pour qu'Apache exécute le script, il faut:

 - Autoriser les scripts
 - Ajouter un handler Python
 - Charger le module CGI

Chercher et modifier la partie correspondante dans le fichier de configuration d'Apache

```html title="/etc/apache2/apache2.conf" linenums="170"
<Directory /var/www/>
        Options Indexes FollowSymLinks ExecCGI
        AddHandler cgi-script .cgi .py
        LoadModule cgi_module /usr/lib/apache2/modules/mod_cgi.so
        AllowOverride None
        Require all granted
</Directory>
```

```
systemstl reload apache2
```

## Sources

 - La structure de la page web et la fonction de génération des graphiques ont été inspirés de [sensors.frols.com](https://sensors.frols.com/draveil1).
