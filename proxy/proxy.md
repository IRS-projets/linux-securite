# Proxy Squid

## Cahier des charges

Nous devons réduir l'utilisation de la bande passante on doit interdire l'accès à certains sites.
Squid prend en charge les protocoles http.

## Solution proposée

Nous estimons que notre solution devrait diminuer notre consommation de bande passante si on aura des dizaine de machines prochainement.
on a chaoisi la categorie "streming media application" le service de youtube et facebook.

 "Installation du serveur proxy" 
 `sudo apt-get install squid`

### Configurer le serveur proxy Squid:

Le fichier de configuration de Squid se trouve à /etc/squid/squid.conf  ===> `sudo vim /etc/squid/squid.conf`

Naviguez pour trouver l'option http_port. En règle générale, il est configuré pour écouter sur le port ==3128==. Ce port transporte généralement le trafic TCP.
Accédez à l'option http_access deny all. Ceci est actuellement configuré pour bloquer tout le trafic HTTP. Cela signifie qu'aucun trafic Web n'est autorisé.

### dans le fichier de conf /etc/squid/squid.conf

- remplacer deny par allow 

ligne 1416,
`http_access allow all` 


### Ajouter squid ACL et Bloquer les sites Web sur Squid Proxy :

 "squid_config"  

    - A partir "include /etc/squid/conf.d/" (ligne 1402)
    - Ajouter dans le fichier de conf

    ```bash title="/etc/squid/squid.conf" linenums="1"
    acl localnet src 10.0.2.15 (IP du serveur)
    acl liste_url dstdomain "/etc/squid/liste-sites.txt"
    http_access deny liste_url
    http_access allow localnet
    ```

### Création de la liste des sites Blacklisté : 

 "sites_blacklist"

    - dans le répertoire /etc/squid/ 
    - créer un fichier texte

    ```bash title="/etc/squid/liste-sites.txt" linenums="1"
    .facebook.com        
    .youtube.com
    ```

### Redémarrer le service: 

`sudo systemctl restart squid`

## Configurer le proxy HTTP pour fonctionner avec le navigateur Mozilla Firefox:

- Open Firefox Mozilla
- en haut > Settings
- cliquer sur Manual proxy configuration
- HTTP proxy ( Ton IP) / Port: 3128
- cliquer sur OK
