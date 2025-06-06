import subprocess

def run_command(command):
    try:
        # Komutu çalıştır
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        # Komutun çıktısını ve hatasını yazdır
        if result.stdout:
            print('Çıktı:', result.stdout)
        if result.stderr:
            print('Hata:', result.stderr)
        print('Çıkış kodu:', result.returncode)
    except subprocess.CalledProcessError as e:
        print('Komut çalıştırılırken hata oluştu:', e)
        if e.stdout:
            print('Çıktı:', e.stdout)
        if e.stderr:
            print('Hata:', e.stderr)

def install_spotify():
    print("Spotify kurulumu başlatılıyor...")
    run_command('sudo apt-get update && sudo apt-get install -y spotify-client')

def install_discord():
    print("Discord kurulumu başlatılıyor...")
    run_command('wget https://discordapp.com/api/download?platform=linux&format=deb -O discord.deb')
    run_command('sudo dpkg -i download?platform=linux')
    run_command('sudo apt-get install -f')

def install_vscode():
    print("VS Code kurulumu başlatılıyor...")
    run_command('wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -')
    run_command('sudo sh -c "echo \'deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\' > /etc/apt/sources.list.d/vscode.list"')
    run_command('sudo apt-get update')
    run_command('sudo apt-get install -y code')

def install_tor_browser():
    print("Tor Browser kurulumu başlatılıyor...")
    run_command('wget https://www.torproject.org/dist/torbrowser/12.0.3/tor-browser-linux64-12.0.3_en-US.tar.xz -O tor-browser.tar.xz')
    run_command('tar -xf tor-browser.tar.xz')
    run_command('sudo mv tor-browser_en-US /opt/tor-browser')
    run_command('echo -e "[Desktop Entry]\\nVersion=1.0\\nName=Tor Browser\\nExec=/opt/tor-browser/tor-browser\\nIcon=/opt/tor-browser/Browser/browser/chrome/icons/default/default128.png\\nTerminal=false\\nType=Application\\nCategories=Network;WebBrowser;" | sudo tee /usr/share/applications/tor-browser.desktop')
    run_command('tor')
def uninstall_spotify():
    print("Spotify kaldırma işlemi başlatılıyor...")
    run_command('sudo apt-get remove -y spotify-client')

def uninstall_discord():
    print("Discord kaldırma işlemi başlatılıyor...")
    run_command('sudo apt-get remove -y discord')

def uninstall_vscode():
    print("VS Code kaldırma işlemi başlatılıyor...")
    run_command('sudo apt-get remove -y code')

def uninstall_tor_browser():
    print("Tor Browser kaldırma işlemi başlatılıyor...")
    run_command('sudo rm -rf /opt/tor-browser')
    run_command('sudo rm /usr/share/applications/tor-browser.desktop')

def uninstall_all():
    uninstall_spotify()
    uninstall_discord()
    uninstall_vscode()
    uninstall_tor_browser()

def install_all():
    install_spotify()
    install_discord()
    install_vscode()
    install_tor_browser()

def set_keyboard_layout_to_turkish():
    print("Türkçe klavye düzeni ayarlanıyor...")
    run_command('setxkbmap tr')

def toolar():
    print("1 : HeJo-01")
    print("2 : HeJo-02")
    print("3 : ip to information")
    print("4 : Discord tooları")
    print("5 : HeJo-Trojen-Generator")
    s = input("> ")
    if s == "1":
        run_command('git clone https://github.com/HeJo-1/HeJo-01')
        print("HeJo-01 Toolu başarılı bir şekilde klonlandı \nLink :https://github.com/HeJo-1/HeJo-01 ")
    elif s == "2":
        run_command('git clone https://github.com/HeJo-1/HeJo-02-V2')
        print("HeJo-02 Toolu başarılı bir şekilde klonlandı\nLink : https://github.com/HeJo-1/HeJo-02-V2")
    elif s == "3":
        run_command('git clone https://github.com/HeJo-1/ip')
        print("ip to informatin Toolu başarılı bir şekilde klonlardı\nLink : https://github.com/HeJo-1/ip")
    elif s == "4":
        run_command('git clone https://github.com/HeJo-1/discord')
        print("Discord toolu başarılı bir şekilde klonlandı\nLink : https://github.com/HeJo-1/discord")
    elif s == "5":
        run_command('git clone https://github.com/HeJo-1/HeJo-Trojen-generator')
        print("HeJo-Trojen-Generator toolu başarılı bir şekilde klonlandı\nLink : https://github.com/HeJo-1/HeJo-Trojen-generator")
    else:
        print("Geçersiz seçim")


print('''
  |     _)                                |                            
  |      | \ \   /  _ \       _` |   _ \  __|       _` |  __ \   __ \  
  |      |  \ \ /   __/      (   |   __/  |        (   |  |   |  |   | 
 _____| _|   \_/  \___|     \__, | \___| \__|     \__,_|  .__/   .__/  
                            |___/                        _|     _|     
''')
print("1 : Spotify kur")
print("2 : Discord kur")
print("3 : VS Code kur")
print("4 : Tor Browser kur")
print("5 : Hepsini indir")
print("11 : Spotify sil")
print("12 : Discord sil")
print("13 : VS Code sil")
print("14 : Tor Browser sil")
print("15 : Hepsini sil")
print("16 : Türkçe klavye düzenini ayarla")
print("17 : Hack Toolarını kur")
a = input("> ")

if a == '1':
    install_spotify()
elif a == '2':
    install_discord()
elif a == '3':
    install_vscode()
elif a == '4':
    install_tor_browser()
elif a == '5':
    install_all()
elif a == '11':
    uninstall_spotify()
elif a == '12':
    uninstall_discord()
elif a == '13':
    uninstall_vscode()
elif a == '14':
    uninstall_tor_browser()
elif a == '15':
    uninstall_all()
elif a == '16':
    set_keyboard_layout_to_turkish()
elif a == '17':
    toolar()
else:
    print("Geçersiz giriş.")
