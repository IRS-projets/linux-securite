# NTP

## Cahier des charges

Nous devons déployer un serveur NTP local.
Ce dernier doit distribuer l'heure obtenur auprès d'une source fiable et ne doit pas être modifiable par les clients.

## Solution proposée 

Le serveur NTP répond à ce beosin.
Nous allons l'implémenter sur la machine respondable du DHCP.

## Implémentation

Installation:

```
apt install ntp
```


