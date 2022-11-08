# Utilisation du protocole SSH

Cette partie explique en détail comment communiquer par SSH avec les machines de notre réseau.

## Echange de clés

Pour des raisons de sécurité, l'authentification par clé est obligatoire sur ce réseau.

Pour commencez, générez une paire de clés, de préférence Ed25519 .

=== "Sur Linux"
    Entrez la commande suivante dans un terminal:
    ```bash
    ssh-keygen -t ed25519
    ```

     - Si l'utilitaire vous demande un fichier de destination, laissez blanc. Il écrira automatiquement dans votre répertopire SSH utilisateur.
     - Entrez ensuite un mot de passe pour plus de sécurité.

    Une fois la paire de clés générée, donnez votre clé ==**publique**== à notre administrateur.
    Vous la trouverez sous forme de fichier `.pub` dans le répertoire `.ssh` de votre utilisateur.
    Communiquez la de préférence directement sur clé USB ou, à défaut, par mail.

=== "Sur Windows"

    !!! info "[PuTTY](https://www.putty.org/)"
        Vous aurez besoin de [télécharger le logiciel libre Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

     - Lancez PuTTYgen et sélectionnez "Ed25519".
     - Cliquez sur "Generate" et bougez phrénétiquement votre souris dans le cadre.
     - Une fois la génération terminée, communiquez à notre administrateur le contenu du premier cadre. Préférez le transfert par clé USB ou, à défaut, par mail.
     - Entrez ensuite un mod de passe pour plus de sécurité.
     - Sauvegardez ensuite vos clez ("Save * key") dans un endroit fiable.
     - Fermez PuTTYgen et ouvrez PuTTY.
     - Dans l'arborescence, allez à Connexion > SSH > Auth.
     - Dans le dernier champs, sélectionnez "Browse..." et retrouvez la clé privée précédemment sauvegardée.

## Connexion

!!! warning "Délai"
    Vous ne pourez vous connecter que quand notre administrateur aura ajouté votre clé à la machine cible.

!!! info "Machinez virtuelles"
    Si vous utilisez une machine virtuelle, il faut la passer en mode bridge.

=== "Sur Linux"
    La commande pour se connexter en SSH est la suivante:
    ```bash
    ssh [utilisateur]@[serveur] -p [port]
    ```

    Remplacez les parties entre parenthèses par ce qui suit:

     - utilisateur: le nom de l'utilisateur auquel vous vous connectez
     - serveur: le nom ou l'addresse du serveur auquel vous vous connectez
     - port: 2022 sur notre infrastructure

=== "Sur Windows"
     - Ouvrez PuTTY.
     - Entrez l'IP ou le nom cible dans le champs "host Name".
     - Entrez le port de destination dans le champs "Port" (2022 sur notre réseau).
     - Sélectionnez "Open"

    !!! tip "Sauvegarde"
        En appuyant sur "Save", vous pouvez sauvegarder ses informations de connexion pour aller plus vite la prochaine fois.
