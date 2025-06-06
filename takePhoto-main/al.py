import socket

# Sunucu bilgileri
HOST = 'ip'
PORT = 12345

# Socket oluştur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Sunucu başlatıldı. İstemci bekleniyor...")

    conn, addr = s.accept()

    with conn:
        print('İstemci bağlandı:', addr)
        # Gelen dosyanın adını al
        filename = conn.recv(1024).decode()
        with open(filename, 'wb') as f:
            print('Dosya alınıyor...')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print('Dosya alındı.')
