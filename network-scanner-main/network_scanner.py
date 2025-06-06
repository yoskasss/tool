import socket
from scapy.all import ARP, Ether, srp

def get_local_ips_and_hostnames():
    # Yerel ağ IP adresini ve ağ maskesini al
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network = '.'.join(local_ip.split('.')[:-1]) + '.1/24'  # CIDR formatında ağ adresi
    
    # ARP istekleri ile ağdaki cihazları bul
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        ip = received.psrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]  # IP adresinden hostname al
        except socket.herror:
            hostname = "Unknown"  # Hostname bulunamazsa "Unknown" yaz
        devices.append((ip, hostname))

    return devices

# Tüm cihazları listele
devices = get_local_ips_and_hostnames()
print("Yerel ağdaki cihazlar:")
for ip, hostname in devices:
    print(f"IP: {ip}, Hostname: {hostname}")
