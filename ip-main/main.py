import requests
import socket
def check(): 
    r = requests.get("https://ipinfo.io/") 
    if r.status_code == 200: 
        print("\n[+] Sunucu Çevrimiçi!\n") 
    else: 
        print("\n[!] Sunucu Çevrimdışı!\n")
        exit()
def get_device_name(ip):
    try:
        host_name = socket.gethostbyaddr(ip)
        return host_name[0]
    except socket.herror:
        return "Belirtilen IP adresi geçersiz veya cihaz adı bulunamadı."
ip = input("Lütfen hedef ip giriniz: ") 
check() 
country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text 
city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text 
region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text
device_name = get_device_name(ip)
print("İp: "+ip)
print("Ülke: "+country)
print("Şehir: "+city)
print("Bölge: "+region)
print("Posta Kodu: "+postal)
print("Zaman Dilimi: "+timezone)
print("Organizasyon: "+orgination)
print("Lokasyon: "+location)
print("Cihaz Adı: "+ device_name)
