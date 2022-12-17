# Configuration du NAT


## Cahier des charges

La mise en place du NAT permettra la communication entre internet et notre réseau. Les différents flux (entrants et sortants) devront circuler par le routeur.


## Solution proposée

Par défaut, les ditributions Debian ne sont pas configurées dans le but d'effectuer la transition des flux entre différents réseaux.
Il est cependant possible d'effectuer plusieurs manipulations permettant la communication entre deux réseaux distincts.


## Configuration du NAT

Afin de pouvoir mettre en place le NAT, il faut savoir qu'un routeur est utilisé pour faire transiter les données d'un réseau A à un réseau B.
De ce fait, le routeur doit avoir accès à ces derniers par le biais de ses interfaces.
On dit alors que le routeur à des pattes dans chaque réseau.
En instaurant le NAT, on effectue une translation de l'adresse IP locale en adresse IP routable sur internet.


Le serveur jouant le rôle doit avoir deux cartes réseaux.
Dans notre cas, la première carte sera configuré en DHCP. En effet, elle récupérera une adresse via le serveur DHCP venant du wifi d'un téléphone.

Pour se faire on se rend dans le fichier de configuration des interfaces en saisissant la commande suivante :

```
sudo nano /etc/network/interfaces

```

Enfin on y ajoute la configuration suivante : 


```
# WAN

  auto enp0s3
  iface enp0s3 inet dhcp
  
 # LAN
  auto enp0s8
  iface enp0s8 inet static
  addresse 192.169.0.1
  netmask 255.255.0.0

```
Ici on effectue un redémarrage du service networking afin de voir si les informations saisies dans le fichier de configuration sont correctes.

```

  systemctl restart networking
```

Puis on se rend dans le fichier de configuration du système afin d'y apporter la modification suivante :

```
  nano /etc/sysctl.conf
  
  
net.ipv4.ip_forward=1 # Ligne à décommenter  
```
Ici on effectue la commande suivante permettant de prendre en compte les modifications effectuées.

```
 sysctl -p /etc/sysctl.conf
```

Enfin on effectue la commande permettant de faire circuler les paquets vers l'extérieur :


```

  iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
```
