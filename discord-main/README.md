
# Discord Bot - Otomatik Mesaj Gönderme Uygulaması

Bu proje, Discord üzerinde belirli bir kanala otomatik mesaj göndermek için geliştirilmiş bir Python uygulamasıdır.
Kullanım Kılavuzu
# Gereksinimler

    Python 3.x
    gerekli kütübhaneler
    Mozilla Firefox tarayıcı ve GeckoDriver 

# Kurulum
Projenin klonlanması:



    git clone https://github.com/yourusername/discord-bot.git
    cd discord-bot

## Python bağımlılıklarının yüklenmesi:



    pip install -r req.txt
    
GeckoDriver'ın indirilmesi ve yolunun belirtilmesi:
GeckoDriver'ı Mozilla'nın resmi GitHub sayfasından indirin.
İndirdiğiniz dosyanın yolunu sel() fonksiyonu içinde GeckoDriver dosya yolu: sorusuna cevap olarak verin.

# Kullanım

Projeyi çalıştırmak için terminal veya komut istemcisinde aşağıdaki komutları kullanın:



    python main.py

Program çalıştırıldığında, aşağıdaki seçeneklerle karşılaşacaksınız:

    1 - token ile giriş
    2 - Şifre ile ayrıntılı bilgi alma
    3 - Spam 
    4 - Bilgileri değiştirme
    99 - Çıkış    

Seçenekleri seçerek programın işlevlerini kullanabilirsiniz.
Dikkat

    1 - token ile giriş seçeneğiyle, bir Discord bot tokeni ve bir kanal ID'si girerek botunuzun belirli bir kanala oturum açmasını ve mesaj göndermesini sağlayabilirsiniz.
    2 - Şifre ile ayrıntılı bilgi alma seçeneğiyle, Discord hesabınızın kullanıcı adı ve şifresini girerek token alabilir ve kullanıcı bilgilerinizi görebilirsiniz.
    3 - Spam seçeneğiyle, belirli bir token ve kanal ID'si kullanarak belirli bir kanala belirli aralıklarla mesaj gönderebilirsiniz.
    4 - Tokeni girilen hesabın kullanıcı adı, pp gibi bilgilerini değiştirebilirsiniz.
