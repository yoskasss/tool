# HeJo-phoneInfo

HeJo-phoneInfo, verilen bir telefon numarası hakkında çeşitli bilgileri görüntüleyen bir Python programıdır.

## Kullanım

### Gereksinimler
Bu programı çalıştırmadan önce aşağıdaki bağımlılıkları yüklemeniz gerekmektedir:
```sh
pip install -r requirements.txt
```

### Çalıştırma
1. `OPENCAGE_API_KEY` değişkenine geçerli bir OpenCage API anahtarını girin.
2. Programı çalıştırın:
```sh
python main.py
```
3. İstenilen telefon numarasını uluslararası formatta girin (örn: `+905551112233`).
4. Program, numara hakkında aşağıdaki bilgileri ekrana yazdıracaktır:
   - Coğrafi konum
   - Operatör bilgisi
   - Saat dilimi
   - Geçerlilik kontrolü
   - Ülke kodu ve formatlar
   - Koordinatlar (eğer mevcutsa)
5. Eğer koordinatlar mevcutsa, harita oluşturulacak ve `Location.html` dosyası kaydedilecektir.
6. Kullanıcıdan haritayı açmak isteyip istemediği sorulacaktır.

### Örnek Çıktı
```
Enter phone number: +905551112233
==================================================
📞 Numara Bilgileri - +905551112233
==================================================
🌍 Konum: Türkiye
📡 Operatör: Turkcell
⏰ Saat Dilimi: Europe/Istanbul
✅ Geçerli mi?: Evet
❓ Mümkün mü?: Evet
🇺🇳 Ülke Kodu: +90
📌 Uluslararası Format: +90 555 111 22 33
📞 Ulusal Format: 0555 111 22 33
--------------------------------------------------
📍 Koordinatlar: 39.9208, 32.8541
==================================================
📌 Konum haritası Location.html olarak kaydedildi.
Haritayı görmek ister misiniz? (E/H): 
```

