import os

def install_scapy():
    try:
        # Scapy kütüphanesini yükle
        os.system(f"{os.sys.executable} -m pip install scapy")
        print("Scapy başarıyla yüklendi.")
    except Exception as e:
        print(f"Scapy yüklenirken bir hata oluştu: {e}")

if __name__ == "__main__":
    install_scapy()
