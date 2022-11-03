# SSH

## Cahier des charges

Nous devons rendre une machine séparée accessible en SSH.
Cette connexion doit répondre aux critères suivants:

 - Être facile d'utilisation
 - Fonctionner de façon fiable
 - Avoir un niveau de sécurité acceptable pour une entreprise
 - Disposer de ressources suffisantes pour répondre aux besoins de l'entreprise.

## Solution proposée

Nous estimons que notre solution devra aménager une dixaine d'hôtes au maximum et supporter quelques connexions simultanées sans transfert de données important (lecture / écriture / téléchargement de fichiers texte).

### Choix matériels et logiciels

Un Arduino ou une Raspberry Pi ont le meilleur rapport qualité / prix pour le niveau de charge à assumer.
De plus, ce sont des plateformes très utilisées et open-source, disposant d'une grande communauté qui rend leur maintenance plus facile et fiable.

Du côté logiciel, l'utilitaire OpenSSH répond aux besoins énoncés plus haut et dispose des mêmes avantages d'open-source et de communauté active.

Nous utiliserons donc une Raspberry Pi avec l'utilitaire openSSH pour ce projet.

### Détail des solutions à implémenter

 - [ ] Configuration de base d'un RPi
 - [ ] Installation d'un serveur SSH
 - [ ] Authentification par clés
     - [ ] Procédure pour échange de clés
 - [ ] SFTP
 - [ ] Fail2Ban
 - Knocking ?
 - A compléter?

## Implémentation
