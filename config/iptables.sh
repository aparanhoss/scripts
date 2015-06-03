iptables -X
iptables -Z
iptables -F
iptables -t nat -X
iptables -t nat -Z
iptables -t nat -F
iptables -A FORWARD -i wlan0 -j ACCEPT
iptables -t nat -A POSTROUTING -s  10.10.10.0/24 -o eth0 -j MASQUERADE
