# NTP

Nous vous proposons d'utiliser notre propre serveur NTP.
Pour cela, vous allez devoir configurer votre appareil.

=== "Sur Linux"

    !!! warning "Vous avez besoin des privilèges superutilisateur."

    !!! info inline end "Vous avez besoin de l'utilitaire NTP."
        Si cet utilitaire n'est pas déjà présent sur votre machine, tapez la commande suvante pour l'installer:

        ```
        apt install ntp
        ```
    
    En tant que superutilisateur, éditez le fichier `/etc/ntp.conf` en lui ajoutant la ligne suivante (elle est ligne 18 par défaut, mais vous pouvez la mettre n'importe où):

    ```
    server ntp.projetlinux.com
    ```

    Redémarrez ensuite le service avec:

    ```
    systemctl restart ntp
    ```


=== "Sur Windows"

    !!! warning "Vous avez besoin des privilèges administrateur."

     - Ouvrez le Panneau de Configuration
     - Sélectionnez "Date et heure"
     - Ouvrez l'onglet "Temps Internet"
     - Cliquez sur "Modifer les paramètres"
     - Dans le champs, entrez `ntp.projetlinux.com`
     - Cliquez sur "Appliquer" puis "OK"

*Vous avez a présent le serveur NTP le plus fiable qui soit!*

!!! tip "Nous utilisons en vérité le serveur de l'UVSQ."
