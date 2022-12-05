DHCP


Part Domain (useless ?)
domain name: projetlinux.com 
IP adress : 192.169.0.2 
subnet : 192.169.0.0 
netmask : 255.255.0.0


sudo apt install isc-dhcp-server
sudo apt install net-tools

subnet 192.169.0.0 netmask 255.255.0.0 {
}

si on passe par un routeur router:
subnet 192.169.0.0 netmask 255.255.255.0 {
  range 192.169.0.0 192.168.0.254;  # BALEK
  option routers router;
}

fichier de conf:
/etc/dhcp/dhcpd.conf


(mode root) service isc-dhcp-server restarts


# config avancée ?


Part client: 

host name : todoname (why not)
IP adress : 192.169.0.6
MAC adress : 08:00:27:49:21:01 (ma vm)
    obtenu avec ifconfig -> enp0s3 -> ether 


# L'interface réseau « loopback » (toujours requise)
auto lo
iface lo inet loopback

# Obtenir l'adresse IP de n'importe quel serveur DHCP
auto eth0
iface eth0 inet dhcp



# BIG TODO CHECK INFO + CLEAN
BIG FLEMME CAR JE SUIS UNE FLEMMARDES
