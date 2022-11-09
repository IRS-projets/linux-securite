DNS

sudo apt install bind9

domaine name = projetlinux.com
ip = 192.169.0.2
subdomaine = rapport.projetlinux.com
slave server = backup.projet.com



/etc/bind/named.conf.local

zone "projetlinux.com" {
    type master;
    file "/etc/bind/db.projetlinux.com";
    // allow-transfer {bbackup.projet.com;}; // List slaves here
    // notify yes; // Notify slaves on change
};



/etc/bind/db.projetlinux.com

$TTL 1h
$ORIGIN .                                  ; base domain-name 
projetlinux.com.         IN      SOA   ns.projetlinux.com. admin.projetlinux.com. (
                                2022110701 ; serial number (++ with each change)
                                12h        ; slave refresh
                                1h         ; retry if refrech failed
                                2d         ; expiry if refresh failed
                                1h         ; minimum TTL
)
                IN      NS      ns.projetlinux.com.   ; NS for this domain
                IN      NS      ns.projetlinux.com.   ; External NS
                IN      A       192.169.0.2   ; IP of domain
ns.projetlinux.com.   IN      A       192.169.0.2   ; IP of NS
rapport.projetlinux.com IN      A       192.169.0.2  ; Rapport subdomain


verification avec dig
    sudo apt install dnsutils

    dig ns @localhost projetlinux.
    
    ce que nous affiche la commande

"
; <<>> DiG 9.16.33-Debian <<>> ns @localhost projetlinux.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51796
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 2

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 9d5bc80135ac643e01000000636983ac6b3a4c21d3b262e6 (good)
;; QUESTION SECTION:
;projetlinux.com.		IN	NS

;; ANSWER SECTION:
projetlinux.com.	3600	IN	NS	ns.projetlinux.eu.
projetlinux.com.	3600	IN	NS	ns.projetlinux.com.

;; ADDITIONAL SECTION:
ns.projetlinux.com.	3600	IN	A	192.169.0.2

;; Query time: 4 msec
;; SERVER: ::1#53(::1)
;; WHEN: Mon Nov 07 23:16:12 CET 2022
;; MSG SIZE  rcvd: 136
"