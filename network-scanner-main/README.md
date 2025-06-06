# Yerel Ağ Cihaz Tarayıcı

Bu Python betiği, yerel ağınızdaki bağlı cihazları tarar ve IP adresleri ile cihaz adlarını (hostname) alır. ARP isteklerini kullanarak ağdaki cihazları keşfeder ve ters DNS sorguları ile cihaz adlarını çözümlemeye çalışır.

---

## Özellikler

- Yerel ağdaki tüm aktif cihazları algılar.
- Cihazların IP adreslerini ve adlarını alır.
- Bağlı cihazları kullanıcı dostu bir formatta listeler.

---

## Gereksinimler

Bu betiği çalıştırmadan önce aşağıdaki gereksinimlerin karşılandığından emin olun:

- Python 3.6 veya üstü
- Ağ paketi işleme için `scapy` kütüphanesi

`scapy` kütüphanesini yüklemek için şu komutu çalıştırabilirsiniz:
```bash
pip install scapy
```
Kullanım

  Betiği bir Python dosyası olarak kaydedin (örneğin, network_scanner.py).
  Terminal veya komut istemcisine gidin.
  Betiği çalıştırmak için şu komutu kullanın:
```python
python network_scanner.py
```
Betik çalıştıktan sonra, yerel ağınızdaki cihazların IP adresleri ve cihaz adları konsolda listelenecektir.
