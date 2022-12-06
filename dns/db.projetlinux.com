$TTL 1h
$ORIGIN .                                  ; base domain-name
projetlinux.com.         IN      SOA   ns.projetlinux.com. admin.projetlinux.com. (
                                2022110707 ; serial number (++ with each change)
                                12h        ; slave refresh
                                1h         ; retry if refrech failed
                                2d         ; expiry if refresh failed
                                1h         ; minimum TTL
)
                IN      NS      ns.projetlinux.com.   ; NS for this domain
		IN	NS	ns.projetlinux.com.    ; External NS
		IN	A       192.169.0.2   ; IP of domain
ns.projetlinux.com.	 IN      A       192.169.0.2   ; IP of NS
rapport.projetlinux.com.	IN	A	192.169.0.2  ; Rapport subdomain
ntp.projetlinux.com	IN	A	192.169.0.2; NTP 
