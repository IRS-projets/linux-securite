---
title: Web
description: Documentation de la configuration du serveur web
---
 
## Cahier des charges
 
Nous devons implémenter un service web sur une machine.
Ce dernier doit répondre aux critères suivants:
 
 - Être structuré de façon à être navigable facilement
 - Avoir un sous-domaine protégé pour pouvoir accueillir des informations sensibles
 
!!! note "Sous-domaine protégé"
    La description des actions à mener est correcte mais la protection n'a pas été implémentée pour ne pas entraver la facilité d'utilisation.
 
## Solution proposée
 
### Choix matériels et logiciels
 
Notre solution devra répondre à une dizaine de connexions simultanées.
Nous allons donc installer un serveur web sur le RPi déjà utilisé.
 
Apache est un outil libre activement supporté qui répond à nos attentes et est facile d'utilisation, nous allons donc le privilégier.
 
### Détail des solutions implémentées
 
 - Installer Apache
 - Faire la configuration qui comporte un sous-réseau
 - Protéger ce sous-réseau par un mot de passe
 - Créer du contenu web à afficher
 
## Implémentation
 
### Configuration
 
Installation du serveur Apache:
 
```bash
apt install apache2
```
 
??? abstract "Modification de la configuration"
    ```bash title="/etc/apache2/sites-available/000-default.conf" linenums="1"
    <VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com
 
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/projetlinux.com/
 
        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn
 
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
 
        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
    </VirtualHost>
 
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
 
    ```
 
??? abstract "Configuration du sous-domaine"
    Le rapport contenant des données sensibles vis-à-vis de l'infrastructure du projet, nous l'isolons sur un sous-domaine protégé.
 
    ```bash title="/etc/apache2/sites-available/rapport.projetlinux.com.conf" linenums="1"
    <VirtualHost *:80>
        ServerName rapport.projetlinux.com
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/rapport.projetlinux.com/
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
 
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
    ```
 
### Protection du sous-domaine
 
#### Vérification des modules
 
Apache est un utilitaire qui s'appuie sur des modules pour beaucoup de tâches.<br>
Pour l'authentification par mot de passe, nous avons besoin des modules `authn_core_module` et `authz_core_module`.
 
Vérification des modules chargés:
 
```
apache2ctl -M
```
 
Si les modules requis ne sont pas chargés, on utilise:
 
```
a2enmod [module]
```
 
#### Création du mot de passe
 
```bash
mkdir /etc/apache2/passwd
htpasswd -c /etc/apache2/passwd/rapport standard # (1)
```
 
1. Génération du mot de passe pour l'utilisateur "standard"
 
#### Mise à jour de la configuration
 
??? abstract "Configuration du sous-domaine"
    ```bash title="/etc/apache2/sites-available/rapport.projetlinux.com.conf" linenums="1"
    <VirtualHost *:80>
        ServerName rapport.projetlinux.com
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/rapport.projetlinux.com/
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        <Directory "/var/www/html/rapport.projetlinux.com">
                AuthType Basic
                AuthName "Cet espace est sécurisé"
                AuthUserFile "/etc/apache2/passwd/rapport"
                Require user everyone
        </Directory>
    </VirtualHost>
 
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
    ```
 
Redémarrage pour que les modifications prennent lieu:
 
```
systemctl reload apache2
```
 
### Contenu
 
Nous avons décidé de peupler le domaine principal avec les modes d'emploi utiles pour utiliser notre maquette et le sous-domaine avec le rapport que vous lisez en ce moment même.
 
Nous avons généré ce contenu à l'aide de l'outil [Material](https://squidfunk.github.io/mkdocs-material/).
 
!!! tip "Code source"
    Vous pouvez voir le code source qui a servi à générer ce document sur [notre GitHub](https://github.com/IRS-projets/linux-securite).
 
## Sources
 
 - [documentation.frolov.eu](http://documentation.frolov.eu/linux/apache/) (ressource privée)
