# Dosya.co Brute Force Tool

## 🔨 Araç Hakkında
Bu Python tabanlı tool, **dosya.co** üzerindeki şifreli dosyaların doğru şifresini bulmak için brute force (kaba kuvvet) yöntemi kullanır. Kullanıcıdan bir dosya.co linki ve bir wordlist (metin dosyası) alarak, şifre denemeleri yapar ve doğru şifreyi bulduğunda bunu ekranda gösterir.

---

## 🔗 Özellikler
- Dosya.co sitelerinde form alanı bulur ve şifre denemesi yapar.
- Yanlış şifre denemelerinde "Şifre yanlış" mesajı verir.
- Doğru şifre bulunduğunda denemeyi durdurur ve sonucu ekranda gösterir.
- Estetik ve renkli terminal çıktısı sunar (colorama kullanılarak).

---

## 📝 Sistem Gereksinimleri
Toolun çalışması için aşağıdaki bileşenlerin yüklenmiş olması gerekmektedir:

1. **Python 3.x** (3.7 veya daha yeni bir sürüm)
2. Gerekli Python kütüphaneleri:
   - `requests`
   - `bs4` (BeautifulSoup)
   - `colorama`

Kurulum yapmak için terminalde şu komutu çalıştırabilirsiniz:
```bash
pip install requests beautifulsoup4 colorama
```

---

## ⚡ Kullanım

### 1. Adım: Script'i Çalıştırma
Terminal veya komut satırı üzerinden script'i çalıştırın:
```bash
python main.py
```

### 2. Adım: Gerekli Bilgileri Girme
Script, şu bilgileri girmenizi ister:
- **Dosya.co linki**: Hedef dosyanın URL'si.
- **Wordlist dosyası**: Denenecek şifrelerin bulunduğu bir metin dosyası (her satırda bir şifre).

#### Örnek:
```plaintext
Dosya.co linkini giriniz: https://dosya.co/example
Wordlist dosyasını giriniz (.txt): passwords.txt
```


https://github.com/user-attachments/assets/dad273b4-d8fb-4f4f-a93e-535a87b20db9



### 3. Adım: Şifre Denemeleri
Tool, wordlist dosyasındaki her şifreyi sırayla dener. Doğru şifre bulunduğunda denemeyi durdurur ve sonucu gösterir.

#### Çıktı Örneği:
```plaintext
Şifre: 123 | Sonuç: Şifre yanlış
Şifre: 456 | Sonuç: Şifre yanlış
Şifre: 789 | Yanıt:

<Valid Response Detected>
Doğru şifre bulundu: 789
```

---


## 📢 Uyarı
Bu tool eğitim ve test amaçlı geliştirilmiştir. **Yetkisiz sistemlere brute force veya benzeri yöntemlerle erişim denemek yasalara aykırıdır.** Sadece kendi sistemlerinizde veya izin aldığınız durumlarda kullanın. Kullanımdan doğabilecek sorumluluk tamamen kullanıcıya aittir.

