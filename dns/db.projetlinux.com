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
