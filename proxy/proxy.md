# squid proxy


## Install Squid Package on Ubuntu: 
 
*udo apt-get install squid*

### Configuring Squid Proxy Server:

Le fichier de configuration de Squid se trouve à #/etc/squid/squid.conf  ===> *sudo vim /etc/squid/squid.conf*

Naviguez pour trouver l'option http_port. En règle générale, il est configuré pour écouter sur le port ==3128==. Ce port transporte généralement le trafic TCP.
Accédez à l'option http_access deny all. Ceci est actuellement configuré pour bloquer tout le trafic HTTP. Cela signifie qu'aucun trafic Web n'est autorisé.

### dans le fichier de conf /etc/squid/squid.conf

- remplacer deny par allow 

*http_access allow all*


#### Ajouter squid ACL et Bloquer les sites Web sur Squid Proxy :
 
cherchez cette ligne *include /etc/squid/conf.d/* et ajouter les 4 lignes (37- 40 en dessous) dans le fichier de conf 

# We strongly recommend the following be uncommented to protect innocent
# web applications running on the proxy server who think the only
# one who can access services on "localhost" is a local user
#http_access deny to_localhost

#
# INSERT YOUR OWN RULE(S) HERE TO ALLOW ACCESS FROM YOUR CLIENTS
#
include /etc/squid/conf.d/*
*Ajouter ces 4 ligne dans votre fichier de conf*

acl localnet src 10.0.2.15 (ton IP)
acl liste_url dstdomain "/etc/squid/liste-sites.txt"
http_access deny liste_url
http_access allow localnet

##### Création de la liste des sites Blacklisté : 

 *"/etc/squid/liste-sites.txt"* 

*.facebook.com*
*.youtube.com*



###### Restart the conf : 

*sudo systemctl restart squid*

####### Configurer le proxy HTTP pour fonctionner avec le navigateur Mozilla Firefox:

- Open Firefox Mozilla
- en haut > Settings
- cliquer sur Manual proxy configuration
- HTTP proxy ( Ton IP) / Port: 3128
- cliquer sur OK
