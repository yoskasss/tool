# Sohbet Uygulaması

Bu Python uygulaması, basit bir sohbet sunucusu ve istemcisi sağlar. Sunucu, istemcileri kabul eder ve mesajları yayar. İstemciler ise mesaj gönderir ve alır.

## Özellikler

- Sunucu, rastgele veya kullanıcının belirlediği bir oda koduyla istemcileri kabul eder.
- İstemciler, bir sunucuya bağlanarak diğer katılımcılarla sohbet edebilirler.
- Sunucu, maksimum istemci sayısını belirlemenize olanak tanır ve bu sınır aşıldığında yeni bağlantıları reddeder.
- Sunucu, sohbet odasına katılan her istemcinin bağlantısını ve mesajlarını takip eder.

## Gereksinimler

- Python 3.x

## Kullanım

### Sunucu Başlatma

1. Sunucuyu başlatmak için terminal veya komut istemcisine aşağıdaki komutu girin:
   ```bash
   python chat.py
   ```
2. Sunucu başlatıldığında, sırasıyla aşağıdaki bilgileri girmeniz istenecektir:
   - Sunucu IP adresi.
   - Sunucu port numarası.
   - Sohbet odasına izin verilen maksimum istemci sayısı.
   - Sunucuya ait bir kullanıcı adı (nickname).
   - Rastgele oluşturulmuş bir oda kodu veya kullanıcı tarafından belirlenmiş bir oda kodu.

3. Sunucu çalıştığında, oda kodunu ve diğer gerekli bilgileri istemcilerle paylaşabilirsiniz.

### İstemci Başlatma

1. İstemciyi başlatmak için terminal veya komut istemcisine aşağıdaki komutu girin:
   ```bash
   python chat.py
   ```
2. İstemci başlatıldığında, sırasıyla aşağıdaki bilgileri girmeniz istenecektir:
   - Bağlanmak istediğiniz sunucunun IP adresi.
   - Bağlanmak istediğiniz sunucunun port numarası.
   - Katılmak istediğiniz sohbet odasının 6 haneli kodu.
   - Sohbette kullanmak üzere bir kullanıcı adı (nickname).

3. Bağlantı kurulduktan sonra, mesajları yazıp gönderebilir ve diğer istemcilerden gelen mesajları görebilirsiniz.

Bu sohbet uygulaması, basit bir Python tabanlı sunucu-istemci mimarisi kullanarak temel bir iletişim platformu sağlar.
