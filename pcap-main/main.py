from scapy.all import *
from collections import defaultdict, Counter
from scapy.layers.http import HTTPRequest, HTTPResponse

def count_tcp_packets(pcap_file):
    packets = rdpcap(pcap_file)
    tcp_count = sum(1 for packet in packets if packet.haslayer(TCP))
    return tcp_count

def filter_ip_traffic(pcap_file, target_ip):
    packets = rdpcap(pcap_file)
    filtered_packets = [packet.summary() for packet in packets if IP in packet and (packet[IP].src == target_ip or packet[IP].dst == target_ip)]
    return filtered_packets

def analyze_http_traffic(pcap_file):
    packets = rdpcap(pcap_file)
    http_traffic = []
    
    for packet in packets:
        if packet.haslayer(HTTPRequest):
            http_layer = packet[HTTPRequest]
            http_traffic.append(f"HTTP Request: {http_layer.Method.decode()} {http_layer.Host.decode()}{http_layer.Path.decode()}")
        elif packet.haslayer(HTTPResponse):
            http_layer = packet[HTTPResponse]
            http_traffic.append(f"HTTP Response: {http_layer.Status_Code.decode()} {http_layer.Protocol.decode()}")
    
    return http_traffic

def analyze_protocols(pcap_file):
    packets = rdpcap(pcap_file)
    protocol_counter = Counter()
    
    for packet in packets:
        if IP in packet:
            protocol = packet[IP].proto
            protocol_counter[protocol] += 1
            
    return protocol_counter

def detect_ddos(pcap_file, target_ip, threshold):
    packets = rdpcap(pcap_file)
    packet_count = defaultdict(int)

    for packet in packets:
        if IP in packet and packet[IP].dst == target_ip:
            packet_count[packet[IP].src] += 1

    return {ip: count for ip, count in packet_count.items() if count > threshold}

def main():
    pcap_file = input("PCAP dosyasının yolunu girin: ")
    target_ip = input("Analiz edilecek IP adresini girin: ")
    ddos_threshold = int(input("DDoS tespiti için eşik değerini girin: "))

    print("\nTCP Paket Sayısı:")
    tcp_count = count_tcp_packets(pcap_file)
    print(f"TCP Paket Sayısı: {tcp_count}")

    print("\nBelirli IP Adresine Ait Trafik:")
    filtered_packets = filter_ip_traffic(pcap_file, target_ip)
    for packet in filtered_packets:
        print(packet)

    print("\nHTTP Trafiği Analizi:")
    http_traffic = analyze_http_traffic(pcap_file)
    for http in http_traffic:
        print(http)

    print("\nEn Sık Görülen Protokoller:")
    protocol_counter = analyze_protocols(pcap_file)
    for proto, count in protocol_counter.items():
        print(f"Protokol: {proto}, Sayı: {count}")

    print("\nOlası DDoS Saldırıları:")
    ddos_attacks = detect_ddos(pcap_file, target_ip, ddos_threshold)
    for ip, count in ddos_attacks.items():
        print(f"IP: {ip}, Paket Sayısı: {count}")

if __name__ == "__main__":
    main()
