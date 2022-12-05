Install Squid Package on Ubuntu:   
sudo apt-get install squid

Configuring Squid Proxy Server:
1. The Squid configuration file is found at /etc/squid/squid.conf  ===> sudo vim /etc/squid/squid.conf
2. Navigate to find the http_port option. Typically, this is set to listen on Port 3128. This port usually carries TCP traffic.
3. Navigate to the http_access deny all option. This is currently configured to block all HTTP traffic. This means no web traffic is allowed.

Change this to the following:

http_access allow all


Add squid ACL et Block Websites on Squid Proxy:

# We strongly recommend the following be uncommented to protect innocent
# web applications running on the proxy server who think the only
# one who can access services on "localhost" is a local user
#http_access deny to_localhost

#
# INSERT YOUR OWN RULE(S) HERE TO ALLOW ACCESS FROM YOUR CLIENTS
#
include /etc/squid/conf.d/*

acl localnet src 10.0.2.15 (ton IP)
acl liste_url dstdomain "/etc/squid/liste-sites.txt"
http_access deny liste_url
http_access allow localnet

Création de la liste des sites Blacklisté : 

 vim "/etc/squid/liste-sites.txt" 

.facebook.com
.youtube.com



Restart the conf : 

sudo systemctl restart squid

