# DNS

## Cahier des charges

Nous devons proposer un NS qui traite notre nom de domaine.
Nous avons aussi besoin qu'il prenne en charge un sous-domaine pour la page du rapport.

## Solution proposée

Bind est un serveur opensource mondialement reconnu. 
Il est fiable et très simple d'utilisation, nous allons donc l'utiliser pour cette maquette. 

## Implémentation

Installation:

```
sudo apt install bind9
```

??? abstract "Configuration de la zone DNS a servir"
    ``` linenums="1" title="/etc/bind/named.conf.local"
    zone "projetlinux.com" {
        type master;
        file "/etc/bind/db.projetlinux.com";
        // allow-transfer {bbackup.projet.com;}; // List slaves here
        // notify yes; // Notify slaves on change
    };
    ```

??? abstract "Configuration des informations"
    ``` linenums="1" title="/etc/bind/db.projetlinux.com"
    $TTL 1h                                    ; Duree de vie des informations
    $ORIGIN .                                  ; On se base a la racine 
    projetlinux.com.        IN      SOA   ns.projetlinux.com. admin.projetlinux.com. (
                                    2022110701 ; Numero de serie (++ a chaque changement)
                                    12h        ; Slave refresh
                                    1h         ; Nouvel essai en cas de fail refresh
                                    2d         ; Expiration en cas de fail refresh
                                    1h         ; TTL minimum
    )
                             IN     NS      ns.projetlinux.com. ; NS for this domain
                             IN     NS      ns.projetlinux.com. ; External NS
                             IN     A       192.169.0.2         ; IP du domaine
    ns.projetlinux.com.      IN     A       192.169.0.2         ; IP du NS
    ntp.projetlinux.com.     IN     A       192.169.0.2         ; IP du NTP
    rapport.projetlinux.com. IN     A       192.169.0.2         ; Sous-domaine du rapport
    ```

Vérification avec `dig` (en local seulement, le domaine n'exisytant pas sur Internet):

```
dig @localhost projetlinux.com
```
