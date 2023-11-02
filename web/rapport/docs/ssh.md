---
title: SSH
description: Documentation de la configuration du SSH
---

## Cahier des charges

Nous devons rendre une machine séparée accessible en SSH.
Cette connexion doit répondre aux critères suivants:

 - Être facile d'utilisation
 - Fonctionner de façon fiable
 - Avoir un niveau de sécurité acceptable pour une entreprise
 - Disposer de ressources suffisantes pour répondre aux besoins de l'entreprise.

## Solution proposée

Nous estimons que notre solution devra aménager une dizaine d'hôtes au maximum et supporter quelques connexions simultanées sans transfert de données important (lecture / écriture / téléchargement de fichiers texte).

### Choix matériels et logiciels

Un Arduino ou une Raspberry Pi ont le meilleur rapport qualité / prix pour le niveau de charge à assumer.
De plus, ce sont des plateformes très utilisées et open-source, disposant d'une grande communauté qui rend leur maintenance plus facile et fiable.

Du côté logiciel, l'utilitaire OpenSSH répond aux besoins énoncés plus haut et dispose des mêmes avantages d'open-source et de communauté active.

Nous utiliserons donc une Raspberry Pi avec l'utilitaire openSSH pour ce projet.

### Détail des solutions implémentées

 - Installation d'un serveur SSH
 - Authentification par clés
     - Procédure pour échange de clés

## Implémentation

### Configuration SSH

Installation du serveur SSH:

```bash
apt install openssh-server
```

Configuration:

??? abstract "sshd_config"
    Modifications effectuées par rapport à la version d'origine:

     - Passage au port 2022 (pour réduire les attaques bruteforce par script)
     - Interdiction de l'IPv6 (parce qu'on en aura pas besoin pour ce projet)
     - Force un échange de clés au bout de 5 minutes (pour plus de sécurité)
     - Réduction du temps d'authentification à 1 minute (pour diminuer le risque de DOS)
     - Désactivation du login root (pour plus de sécurité)
     - Diminution de la quantité de tentatives de login à 2 par session (pour que chaque 2e échec soit logué - ceci sera utilisé par f2b)
     - Réduction de la quantité de sessions à 2 par hôte (pour limiter les tentatives de bruteforce). On autorise 2 sessions pour pouvoir garder une session de "sécurité" afin d'éviter de perdre le contrôle de la machine en cas d'erreur de configuration (SSH, firewall etc)
     - interdiction de login par mot de passe (pour plus de sécurité)
     - Désactivation de l'authentification PAM (ne sera pas utilisé pour ce projet)
     - Désactivation du forwarding SSH (pour plus de sécurité)
     - Désactivation du forwarding TCP (pour plus de sécurité)
     - Ajout des bannières (pour plus de SWAG)

    ```bash title="/etc/ssh/sshd_config" linenums="1"
    #   $OpenBSD: sshd_config,v 1.103 2018/04/09 20:41:22 tj Exp $

    # This is the sshd server system-wide configuration file.  See
    # sshd_config(5) for more information.

    # This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

    # The strategy used for options in the default sshd_config shipped with
    # OpenSSH is to specify options with their default value where
    # possible, but leave them commented.  Uncommented options override the
    # default value.

    #Include /etc/ssh/sshd_config.d/*.conf

    Port 2022
    AddressFamily inet
    #ListenAddress 0.0.0.0
    #ListenAddress ::

    #HostKey /etc/ssh/ssh_host_rsa_key
    #HostKey /etc/ssh/ssh_host_ecdsa_key
    HostKey /etc/ssh/ssh_host_ed25519_key

    # Ciphers and keying
    RekeyLimit default 5m

    # Logging
    #SyslogFacility AUTH
    #LogLevel INFO

    # Authentication:

    LoginGraceTime 1m
    PermitRootLogin no
    #StrictModes yes
    MaxAuthTries 2
    MaxSessions 2

    #PubkeyAuthentication yes

    # Expect .ssh/authorized_keys2 to be disregarded by default in future.
    #AuthorizedKeysFile .ssh/authorized_keys .ssh/authorized_keys2

    #AuthorizedPrincipalsFile none

    #AuthorizedKeysCommand none
    #AuthorizedKeysCommandUser nobody

    # For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
    #HostbasedAuthentication no
    # Change to yes if you don't trust ~/.ssh/known_hosts for
    # HostbasedAuthentication
    #IgnoreUserKnownHosts no
    # Don't read the user's ~/.rhosts and ~/.shosts files
    #IgnoreRhosts yes

    # To disable tunneled clear text passwords, change to no here!
    PasswordAuthentication no
    #PermitEmptyPasswords no

    # Change to yes to enable challenge-response passwords (beware issues with
    # some PAM modules and threads)
    ChallengeResponseAuthentication no

    # Kerberos options
    #KerberosAuthentication no
    #KerberosOrLocalPasswd yes
    #KerberosTicketCleanup yes
    #KerberosGetAFSToken no

    # GSSAPI options
    #GSSAPIAuthentication no
    #GSSAPICleanupCredentials yes
    #GSSAPIStrictAcceptorCheck yes
    #GSSAPIKeyExchange no

    # Set this to 'yes' to enable PAM authentication, account processing,
    # and session processing. If this is enabled, PAM authentication will
    # be allowed through the ChallengeResponseAuthentication and
    # PasswordAuthentication.  Depending on your PAM configuration,
    # PAM authentication via ChallengeResponseAuthentication may bypass
    # the setting of "PermitRootLogin without-password".
    # If you just want the PAM account and session checks to run without
    # PAM authentication, then enable this but set PasswordAuthentication
    # and ChallengeResponseAuthentication to 'no'.
    UsePAM no

    AllowAgentForwarding no
    AllowTcpForwarding no
    #GatewayPorts no
    X11Forwarding yes
    #X11DisplayOffset 10
    #X11UseLocalhost yes
    #PermitTTY yes
    PrintMotd yes
    #PrintLastLog yes
    #TCPKeepAlive yes
    #PermitUserEnvironment no
    #Compression delayed
    #ClientAliveInterval 0
    #ClientAliveCountMax 3
    #UseDNS no
    #PidFile /var/run/sshd.pid
    #MaxStartups 10:30:100
    #PermitTunnel no
    #ChrootDirectory none
    #VersionAddendum none

    # no default banner path
    Banner .ssh/banner

    # Allow client to pass locale environment variables
    AcceptEnv LANG LC_*

    # override default of no subsystems
    Subsystem   sftp    /usr/lib/openssh/sftp-server

    # Example of overriding settings on a per-user basis
    #Match User anoncvs
    #   X11Forwarding no
    #   AllowTcpForwarding no
    #   PermitTTY no
    #   ForceCommand cvs server
    ```

### Configuration des la banières

???abstract "MOTD"
    ```title="/etc/motd" linenums="1"
    #     #    #     #####  ####### ####### ######     ### ######   #####
    ##   ##   # #   #     #    #    #       #     #     #  #     # #     #
    # # # #  #   #  #          #    #       #     #     #  #     # #
    #  #  # #     #  #####     #    #####   ######      #  ######   #####
    #     # #######       #    #    #       #   #       #  #   #         #
    #     # #     # #     #    #    #       #    #      #  #    #  #     #
    #     # #     #  #####     #    ####### #     #    ### #     #  #####

            #####                                         #####
            #     # #####   ####  #    # #####  ######    #     #
            #       #    # #    # #    # #    # #               #
            #  #### #    # #    # #    # #    # #####      #####
            #     # #####  #    # #    # #####  #         #
            #     # #   #  #    # #    # #      #         #
             #####  #    #  ####   ####  #      ######    #######
    ```

???abstract "SSH"
    ```title="/etc/ssh/banner" linenums="1"
    Cette machine est responsable des services SSH, DNS, NTP et web.
    ```
 
## Sources

 - [OpenSSH](https://www.openssh.com/)
 - [patorjk.com](http://www.patorjk.com/software/taag/)
