from scapy.all import *

def analyze_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    arp_requests = {}
    arp_responses = {}

    for packet in packets:
        if packet.haslayer(ARP):
            arp_layer = packet[ARP]
            if arp_layer.op == 1:  # ARP Request
                src_ip = arp_layer.psrc
                src_mac = arp_layer.hwsrc
                if src_ip not in arp_requests:
                    arp_requests[src_ip] = set()
                arp_requests[src_ip].add(src_mac)
            elif arp_layer.op == 2:  # ARP Response
                src_ip = arp_layer.psrc
                src_mac = arp_layer.hwsrc
                if src_ip not in arp_responses:
                    arp_responses[src_ip] = set()
                arp_responses[src_ip].add(src_mac)

    # ARP Spoofing tespiti
    print("ARP Requestlar:")
    for ip, macs in arp_requests.items():
        print(f"IP: {ip}, MAC'ler: {', '.join(macs)}")

    print("\nARP Response'lar:")
    for ip, macs in arp_responses.items():
        print(f"IP: {ip}, MAC'ler: {', '.join(macs)}")

    print("\nOlası ARP Spoofing tespitleri:")
    for ip in arp_responses.keys():
        if ip in arp_requests and len(arp_requests[ip]) > 1:
            print(f"ALERT: {ip} için farklı MAC adresleri bulundu! {arp_requests[ip]}")

# PCAP dosyasının yolunu belirtin
pcap_file = "output.pcap"
analyze_pcap(pcap_file)
