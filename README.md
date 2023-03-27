[![ci](https://github.com/IRS-projets/linux-securite/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/IRS-projets/linux-securite/actions/workflows/ci.yml)

# linux-securite
Projet de sécurité Linux

## Règles pour la contribution

Quelques règles simples pour que tout se passe proprement:

 - Les commits ne se font qu dans une branche, *aucun* commit dans le main.
 - On a une branche par module *minimum*. 
   - Si on veut modifier de facon conséquente l'état d'un module, on peut bien-sûr imbriquer une nouvelle sous-branche à la branche du module. 
 - Le merge est réalisé par celui qui a ouvert la pull request
 - On communique clairement à l'aide d'issues.
 - Si une proposition n'est pas commentée au bout de 3 jours, elle est automatiquement acceptée. 

## Sujets travaillés

### Consignes

Il faut implémenter au minimum 4 "services essentiels" et 2 "services".

Nous avons choisi les sujets les plus simples comme tâches obligatoires et d'ajouter ultérieurement d'autres projets bonus en fonction des ressources dont nous disposerons. 

### Listes

Ainsi, voici les choix sur lesquels les membres se sont accordés:

#### Services essentiels

 - [ ] Accès internet
 - [ ] Accès intranet
 - [x] SSH
 - [x] DHCP
 - [x] DNS
 - [x] NTP

#### Services

 - [ ] Partage de fichiers
 - [x] Site web
 - [ ] Base de données
 - [x] Pare-feu
 - [ ] Annuaire
 - [ ] Supervision
 - [ ] VPN
 - [x] Proxy
 - [ ] Sauvegarde
 - [ ] Conteneurisation
 - [ ] Bastion

*Les sujets optionnels n'ont pas encore été sélectionnés.*
