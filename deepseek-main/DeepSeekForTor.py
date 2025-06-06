import requests
import json
import socks
import socket
import subprocess
import time
from stem.control import Controller

# Tor'un yolu (Windows veya Linux için değiştirebilirsiniz)
TOR_PATH = "<TorPath>"  # Windows için


# Tor'u başlat
def start_tor():
    print("Tor servisi başlatılıyor...")
    tor_process = subprocess.Popen([TOR_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)  # Tor'un başlatılması için kısa bir bekleme süresi
    return tor_process

# Tor ağına bağlan ve yeni kimlik oluştur
def connect_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="<password>")  # Şifreyi torrc'den ayarlamalısınız
        controller.signal(2)  # Yeni IP adresi al

    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

# İçerik çekme fonksiyonu
def fetch_content(input_value, version):
    if version == "r1":
        url = f"https://deepseek-r1.istebutolga.workers.dev/?prompt={input_value}"
    elif version == "v3":
        url = f"https://deepv3.istebutolga.workers.dev/?prompt={input_value}"
    else:
        print("Geçersiz versiyon! 'r1' veya 'v3' kullanın.")
        return

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            print(data['choices'][0]['message']['content'])
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Bağlantı hatası: {e}")

if __name__ == "__main__":
    tor_process = start_tor()
    print("Tor ağına bağlanılıyor...")
    connect_tor()
    print("Tor ağına bağlanıldı!")

    while True:
        user_input = input("Lütfen bir input girin (çıkmak için 'exit' yazın): ")
        if user_input.lower() == "exit":
            print("Çıkış yapılıyor...")
            tor_process.terminate()  # Tor servisini kapat
            break
        
        parts = user_input.split(" ", 1)
        if len(parts) == 2 and parts[0] in ["/r1", "/v3"]:
            version = parts[0][1:]
            prompt = parts[1]
            fetch_content(prompt, version)
        else:
            print("Hatalı giriş! '/r1 <prompt>' veya '/v3 <prompt>' formatını kullanın.")

