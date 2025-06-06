# Mesaj Yazma Aracı

Bu proje, Windows API kullanarak belirli bir mesajı belirtilen sıklıkta ve süre boyunca yazan basit bir GUI uygulamasıdır. Kullanıcı, mesajı, frekansı ve süresini belirleyerek otomatik mesaj yazma işlemini başlatabilir.

## Özellikler

- Mesaj girişi
- Frekans ve süre belirleme
- Mesaj yazma işlemini başlatmak için bir buton
- Mesajın her karakterinin yazılması ve enter tuşuna basılması

## Gereksinimler

- Windows işletim sistemi
- C derleyici (örneğin, GCC veya MSVC)

## Kullanım

1. Projeyi klonlayın veya indirin.
2. Projeyi bir C derleyici ile derleyin.
3. Uygulamayı çalıştırın.
4. Mesaj, frekans ve süre alanlarını doldurun:
   - **Mesaj:** Yazılacak mesaj.
   - **Frekans:** Mesajın bir saniyede kaç kez yazılacağını belirtir.
   - **Süre:** Mesajın toplamda kaç saniye yazılacağını belirtir.
5. "Başlat" butonuna tıklayın. Uygulama, 5 saniye bekledikten sonra mesajı yazmaya başlayacaktır.

## Kod Yapısı

- **typeMessage:** Mesajı belirtilen frekans ve süre boyunca yazar.
- **WindowProc:** Pencere işlemlerini yönetir, buton tıklamaları gibi olayları dinler.
- **WinMain:** Uygulamanın ana giriş noktasıdır ve pencereyi oluşturur.

## Katkıda Bulunanlar

- [NULL] - Proje sahibi

## İletişim

Herhangi bir sorun veya katkı için iletişime geçebilirsiniz.

---

**Not:** Uygulama, klavye girişlerini simüle ettiğinden, kullanırken dikkatli olun. Kullanımı kötüye kullanılmamalıdır.
