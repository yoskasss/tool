import os
import sys
import subprocess
import requests
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.progress import Progress
import pyfiglet

console = Console()

def display_banner():
    """Estetik bir banner görüntüler."""
    banner = pyfiglet.figlet_format("Proxy Tester")
    console.print(f"[bold cyan]{banner}[/bold cyan]")

def install_requirements():
    """Gereksinimleri yükler."""
    console.print("[bold yellow]Gereksinimler yükleniyor...[/bold yellow]")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "gereksinimler.txt"])
        console.print("[bold green]Gereksinimler başarıyla yüklendi![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Gereksinimler yüklenirken hata oluştu: {e}[/bold red]")
        sys.exit(1)

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
            console.print(f"\n[green]Çalışan Proxy:[/green] {proxy}")  # Çalışan proxy'yi yeni satıra yaz
            with open("calis.txt", "a") as file:
                file.write(proxy + "\n")
            return proxy
    except:
        sys.stdout.write(f"\r[red]Hatalı Proxy:[/red] {proxy}   ")  # Aynı satırda kal
        sys.stdout.flush()
    return None

def filter_working_proxies(proxy_file):
    """Proxy listesinden çalışanları filtreler."""
    with open(proxy_file, "r") as file:
        proxies = file.readlines()

    with Progress(console=console) as progress:
        task = progress.add_task("[cyan]Proxy'ler test ediliyor...", total=len(proxies))

        # Paralel işlem başlatma
        with ThreadPoolExecutor(max_workers=10) as executor:
            for _ in executor.map(test_proxy, proxies):
                progress.advance(task)

def main():
    # Banner'ı göster
    display_banner()

    # Seçenekleri sun
    console.print("[bold cyan]Seçenekler:[/bold cyan]")
    console.print("[1] [yellow]Kur[/yellow] - Gereksinimleri yükle")
    console.print("[2] [yellow]Çalıştır[/yellow] - Proxy kontrolüne başla")

    choice = input("\nSeçiminizi yapın (1/2): ").strip()
    if choice == "1":
        install_requirements()
    elif choice == "2":
        console.print("[bold cyan]Proxy testi başlatılıyor...[/bold cyan]")
        while True:
            file_path = input("Proxy dosyasının yolunu girin (ör. http.txt): ").strip()
            if os.path.exists(file_path) and os.path.isfile(file_path):
                break
            console.print("[bold red]Geçersiz dosya yolu! Lütfen doğru bir dosya yolu girin.[/bold red]")

        # Çalışan proxy'leri bul ve dosyaya kaydet
        filter_working_proxies(file_path)
        console.print("\n[bold green]Çalışan proxy'ler 'calis.txt' dosyasına kaydedildi![/bold green]")
    else:
        console.print("[bold red]Geçersiz seçim![/bold red]")

if __name__ == "__main__":
    main()
