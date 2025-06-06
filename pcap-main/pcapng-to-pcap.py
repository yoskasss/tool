from scapy.all import rdpcap, wrpcap

# pcapng dosyasını oku
a = str(input("pcapng dosyasının yolunu girin : "))
pcapng_dosyasi = a
pcap_dosyasi = 'output.pcap'

# Paketleri oku
paketler = rdpcap(pcapng_dosyasi)

# Paketleri .pcap olarak yaz
wrpcap(pcap_dosyasi, paketler)

print(f"{pcapng_dosyasi} dosyası başarıyla {pcap_dosyasi} olarak kaydedildi.")
