# HeJo-Trojen

Bu proje, hesap makinesi işlevselliği sağlayan bir GUI (Grafiksel Kullanıcı Arayüzü) uygulaması ile birlikte yüklendiği birgisayarda arka kapı açan bir virüstür 

## Hesap Makinesi Uygulaması

Hesap makinesi uygulaması, basit dört işlem (toplama, çıkarma, çarpma, bölme) fonksiyonlarını sağlar. Hesaplama işlemi için kullanıcı arayüzü (GUI) tkinter kütüphanesiyle oluşturulmuştur.

### Kullanım

Hesap makinesi uygulamasını başlatmak için, kodu çalıştırdığınızda bir hesap makinesi penceresi açılır. Bu pencerede sayıları ve işlemleri seçerek hesaplamalar yapabilirsiniz.

## Arka Kapı

Ark Kapı, istemcilere çeşitli sistem komutlarını ve dosya içeriklerini gönderir. İstemciden gelen isteklere yanıt verir.

### Kullanım

Sunucu uygulamasını başlatmak için kodu çalıştırdığınızda sunucu belirli bir bağlantı noktasında (varsayılan olarak 127.0.0.1:50002) dinlemeye başlar. İstemcilerin bağlanmasını bekler ve bağlantı kurulduğunda istemciden gelen isteklere yanıt verir.

## Nasıl Çalıştırılır

1. Kodu bir Python ortamında çalıştırın.
2. Hesap makinesi uygulaması otomatik olarak başlayacaktır. Hesap makinesi penceresi açılacaktır.
3. Sunucu uygulaması ayrı bir iş parçacığında başlayacak ve belirli bir bağlantı noktasında dinlemeye başlayacaktır.

## Gereksinimler

- Python 3.x
- tkinter kütüphanesi (genellikle Python'un standart kütüphanesinin bir parçasıdır)
- Threading kütüphanesi (standart Python kütüphanesi)
