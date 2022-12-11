# DHCP

## Cahier des charges:
 Le service DHCP est l'un des services qui nous a été proposé. 
 Nous l'avons choisi pour sa simplicité d'utilisation ainsi que pour le gain de temps qu'il représente.

## Solution proposée
Nous avons choisi le service nommé  'isc-dhcp-server', service qui est propablement le plus utilisé sur les différentes distributions linux.
En effet, sa configuration rapide nous permets de gagner un maximum de temps si plusieurs machines clientes venaient à faire parties du réseau.

### Installation

Dans un premier temps nous installons les paquets 'isc-dhcp-server' et 'net-tools'.
Net-tools est un paquet permettant d'effectuer des commandes en lien avec le réseau dans lequel il est installé.


`sudo apt install isc-dhcp-server`
`sudo apt install net-tools`

### Configuration DHCP

Une fois le service installé, nous nous rendons dans le fichier de configuration qui nous permet d'apporter les
modifications nécessaires au fonctionnement de ce dernier.

``` 
   sudo nano /etc/dhcp/dhcpd.conf
```
Enfin nous ajoutons dans le fichier de configuration les paramètres suivants :

  ```bash title="/etc/dhcp/dhcpd.conf" linenums="1"
    default-lease-time 86400;
    max-lease-time 172800;
    subnet 192.169.0.0 netmask 255.255.0.0 {
	  range			192.169.0.10 192.169.0.254; # Permet de definir la plage d'adresse.
	  option routers		192.169.0.1; # Permet d'indiquer aux machines clientes l'IP du routeur.
    }

   log-facility local0; # paramètre permettant une journalisation du service DHCP
  ```
Afin de vérifier que les modifications ne contiennent pas d'erreur syntaxique nous effectuons un redémarrage du service. Si ce dernier redémarre normalement cela signifie qu'il n'y pas de problème lié à l'incompréhension de la configuration par le serveur.

  `service isc-dhcp-server restart`
  
En plus de la plage d'adresse IP que nous avons défini plus haut, ici nous souhaitons mettre en place une adresse IP dite statique, qui permettra à la Raspberry (Rpi) d'avoir une adresse IP fixe.
  

  ```bash title="/etc/dhcp/dhcpd.conf" linenums="1"
    host host_name{
      hardware ethernet X:X:X:X:X:X;
      fixed-address 192.169.0.2; # Adresse IP fixe du Rpi
    }
  ```
  
Une fois de plus nous effectuons un redémarrage afin de vérifier que le fichier ne contient pas d'erreur syntaxique.
 
  
#### Configuration de l'interface DHCP

Dans le but de pouvoir attribuer des adresses IP aux machines clientes, le serveur doit connaître l'interface sur laquelle il doit agir.
De ce fait, nous nous rendons dans le fichier /etc/default/isc-dhcp-server

  ```bash title="/etc/default/isc-dhcp-server" linenums="1"
	DHCPDv4_CONF=etc/dhcp/dhcpd.conf
	INTERFACESv4 = "enp0s3"
    }
  ```
 
### L'interface réseau « loopback » (toujours requise)
auto lo
iface lo inet loopback

### Configurer de l'interface du serveur DHCP

```bash title="/etc/network/interfaces" linenums="1"
auto enp0s3
    iface enp0s3 inet static
    address 192.169.0.3
    netmask 192.169.0.0
    broadcast 192.169.255.255
  ```
