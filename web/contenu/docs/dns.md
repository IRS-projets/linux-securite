# DNS

Nous vous proposons d'utiliser notre serveur DNS!

Pour ce faire, vous aurez besoin de paramétrer votre machine.

=== "Sur Linux"

    !!! warning "Vous aurez besoin des privilèges superutilisateur."

    Ouvrez un terminal et ajoutez la ligne suivante au début du fichier `/etc/resolv.conf`:

    ```
    nameserver 192.169.0.2
    ```

=== "Sur Windows"

    Ouvrez les paramètres et suivez le cheminement suivant:

     - Réseau et Internet
     - Paramètres réseau avancés
     - Choisissez la carte réseau que vous utilisez
     - Déroulez puis choisissez "Afficher les propriétés supplémentaires"
     - Sur la ligne "Attribution du serveur DNS", Cliquez sur "Modifier", choisissez "Manuel" puis entrez `192.169.0.2`.

A présent, vous pouvez tester le bon fonctionnement du DNS en envoyant une requête PING à [projetlinux.com](http://projetlinux.com).
