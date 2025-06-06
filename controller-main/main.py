import requests
from concurrent.futures import ThreadPoolExecutor

def test_proxy(proxy):
    """Proxy'nin çalışabilirliğini kontrol eder."""
    proxy = proxy.strip()
    try:
        response = requests.get(
            "https://www.google.com",
            proxies={"http": proxy, "https": proxy},
            timeout=5
        )
        if response.status_code == 200:
            print(f"Çalışan Proxy: {proxy}")
            with open("calis.txt", "a") as file:  # Çalışan proxy'yi dosyaya yaz
                file.write(proxy + "\n")
            return proxy
    except:
        pass
    return None

def filter_working_proxies(proxy_file):
    """Proxy listesinden çalışanları filtreler."""
    with open(proxy_file, "r") as file:
        proxies = file.readlines()

    # Paralel işlem başlatma
    with ThreadPoolExecutor(max_workers=10) as executor:  # 10 paralel işçi
        executor.map(test_proxy, proxies)

# Çalışan proxy'leri bul ve dosyaya kaydet
filter_working_proxies("http.txt")
print("Çalışan proxy'ler 'calis.txt' dosyasına kaydedildi.")
