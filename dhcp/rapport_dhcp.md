# DHCP

## Cahier des charges:
  A faire

## Solution proposée

### Installation
`sudo apt install isc-dhcp-server`
`sudo apt install net-tools`

###

  ```bash title="/etc/dhcp/dhcpd.conf" linenums="1"
    default-lease-time 86400;
    max-lease-time 172800;
    subnet 192.169.0.0 netmask 255.255.0.0 {
	  range			192.169.0.3 192.169.0.254;
	  option routers		192.169.0.2;
    } 

   log-facility local0;
  ```

Il faut redémarrer le service pour que les modifications soient prises en compte
en mode super utilisateur :
  `service isc-dhcp-server restarts`


### Partie Client

  - Si on veut définir un client avec une adresse statique
  - On connait l'adresse MAC avec `ip a`
  
  ```bash title="/etc/dhcp/dhcpd.conf" linenums="1"
    host host_name{
      hardware ethernet X:X:X:X:X:X;
      fixed-address Y:Y:Y:Y;
    }
  ```


### L'interface réseau « loopback » (toujours requise)
auto lo
iface lo inet loopback

### Configurer interface du pc de Chris
  - Le pc de Chris sert de passerelle 

```bash title="/etc/network/interfaces" linenums="1"
  auto enp0s3
    iface enp0s3 inet static
    address 192.169.0.1
    netmask 192.169.0.0
    broadcast 192.169.255.255
  ```
