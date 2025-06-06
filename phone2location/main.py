import phonenumbers
import requests
from phonenumbers import geocoder, carrier, timezone
import folium
from opencage.geocoder import OpenCageGeocode
import pyfiglet
import subprocess
subprocess.call("cls", shell=True)

text = "HeJo-phoneInfo"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)

# OpenCage API Anahtarınızı buraya girin
OPENCAGE_API_KEY = input("Lütfen OpenCage API Anahtarınızı girin : ")
if OPENCAGE_API_KEY == "api":
    print("❌ Lütfen OpenCage API Anahtarınızı 'OPENCAGE_API_KEY' değişkenine girin.")
    exit()
geocoder_api = OpenCageGeocode(OPENCAGE_API_KEY)



def numara_bilgisi(numara):
    try:
        # Telefon numarasını ayrıştır
        parsed_number = phonenumbers.parse(numara, None)

        # 📍 Coğrafi Konum Bilgisi (phonenumbers)
        konum = geocoder.description_for_number(parsed_number, "tr")

        # 📡 Operatör Bilgisi
        operator = carrier.name_for_number(parsed_number, "tr")

        # ⏰ Saat Dilimi Bilgisi
        saat_dilimleri = timezone.time_zones_for_number(parsed_number)

        # ✅ Geçerlilik Kontrolleri
        gecerli_mi = phonenumbers.is_valid_number(parsed_number)
        mumkun_mu = phonenumbers.is_possible_number(parsed_number)

        # 🌍 Ülke Kodu & Formatlar
        ulke_kodu = parsed_number.country_code
        uluslararasi_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        ulusal_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

        # 🗺️ OpenCage API ile detaylı bilgi alma
        opencage_sonuc = geocoder_api.geocode(konum)

        if opencage_sonuc:
            enlem = opencage_sonuc[0]['geometry']['lat']
            boylam = opencage_sonuc[0]['geometry']['lng']
        else:
            enlem = boylam = "Bilinmiyor"

        # 📝 Bilgileri ekrana yazdır
        print("=" * 50)
        print(f"📞 Numara Bilgileri - {numara}")
        print("=" * 50)
        print(f"🌍 Konum: {konum}")
        print(f"📡 Operatör: {operator if operator else 'Bilinmiyor'}")
        print(f"⏰ Saat Dilimi: {', '.join(saat_dilimleri)}")
        print(f"✅ Geçerli mi?: {'Evet' if gecerli_mi else 'Hayır'}")
        print(f"❓ Mümkün mü?: {'Evet' if mumkun_mu else 'Hayır'}")
        print(f"🇺🇳 Ülke Kodu: +{ulke_kodu}")
        print(f"📌 Uluslararası Format: {uluslararasi_format}")
        print(f"📞 Ulusal Format: {ulusal_format}")
        print("-" * 50)
        print(f"📍 Koordinatlar: {enlem}, {boylam}")
        print("=" * 50)

        # 🌍 Harita oluşturma
        if enlem != "Bilinmiyor" and boylam != "Bilinmiyor":
            harita = folium.Map(location=[enlem, boylam], zoom_start=8)
            folium.Marker([enlem, boylam], popup=konum).add_to(harita)
            harita.save("Location.html")
            print("📌 Konum haritası Location.html olarak kaydedildi.")
            i = input("Haritayı görmek ister misiniz? (E/H): ").strip().lower()

            if i in ["e", "h"]:
                if i == "e":
                    import os
                    os.system("Location.html")
                else:
                    print("❌ Harita gösterimi iptal edildi.")
            else:
                print("❌ Lütfen sadece 'E' veya 'H' giriniz.")

        else:
            print("❌ Konum bilgisi bulunamadı, harita oluşturulamadı.")

    except Exception as e:
        print(f"❌ Hata: {e}")

# Kullanıcıdan numara al ve bilgileri getir
PHONE_NUMBER = input("Enter phone number: ")
numara_bilgisi(PHONE_NUMBER)