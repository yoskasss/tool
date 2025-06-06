# Port Tarayıcı Uygulaması

Bu Go dilinde yazılmış port tarayıcı uygulaması, belirli bir IP adresi için girilen port aralığında açık ve kapalı portları kontrol eder. Açık portlar için port türünü (HTTP, HTTPS, FTP vb.) ve bağlantı süresini gösterir. Kapalı portlar da ekrana yazdırılır.

## Özellikler

- Kullanıcıdan hedef IP adresi ve port aralığı (başlangıç ve bitiş portları) alır.
- Tarama yapılan portlar için:
  - **Açık portlar**: Hangi portun açık olduğunu, türünü (örneğin, HTTP, FTP, SSH vb.) ve ne kadar sürede bağlantı sağlandığını gösterir.
  - **Kapalı portlar**: Hangi portların kapalı olduğunu gösterir.
- Port türleri, belirli port numaralarına karşılık gelen yaygın hizmet türlerini içerir (örneğin, HTTP, HTTPS, FTP vb.).
- Tarama işlemi tamamlandığında kullanıcıya sonuçlar ve bir bitiş mesajı gösterilir.

## Gereksinimler

Bu uygulama Go dilinde yazılmıştır. Go'yu yüklediğinizden emin olun.

- Go 1.12 veya daha yeni bir sürüm gereklidir.

## Kurulum

1. Go'nun yüklü olduğundan emin olun. [Go İndirme Sayfası](https://golang.org/dl/).
2. Bu depo, aşağıdaki gibi klonlanabilir:

   ```bash
   git clone https://github.com/yourusername/port-scanner.git
`
Proje dizinine girin:
```bash
cd port-scanner
```
Uygulamayı çalıştırın:

    go run main.go

Kullanım

  Uygulama çalıştırıldığında, aşağıdaki gibi kullanıcıdan bilgi alır:
      Hedef IP adresi: Tarama yapılacak IP adresini girin.
        Başlangıç portu: Taramanın başlayacağı port numarasını girin.
        Bitiş portu: Taramanın biteceği port numarasını girin.

  Program, girilen IP ve port aralığı için açık ve kapalı portları kontrol eder.

  Tarama tamamlandıktan sonra:
        Açık portlar: Hangi portların açık olduğunu, türünü ve süreyi gösterir.
        Kapalı portlar: Hangi portların kapalı olduğunu gösterir.
