import requests
from bs4 import BeautifulSoup
import openpyxl

def scrape_google_links(query_url, num_pages):
        all_links = set()

        for page in range(1, num_pages + 1):
            page_url = f"{query_url}&start={(page - 1) * 10}"
            response = requests.get(page_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                for anchor in soup.find_all('a'):
                    href = anchor.get('href')
                    if href.startswith('/url?q='):
                        link = href[7:href.find('&')]
                        all_links.add(link)

        return all_links


query = input("Arama sorgusunu girin: ")
num_pages = int(input("Araştırılacak sayfa sayısını girin: "))
url = f"https://www.google.com/search?q={query}"
links = scrape_google_links(url, num_pages)
if links:
    output_file = input("Çıktı dosya adını girin (uzantısı olmadan): ")
    output_format = input("Çıktı formatını girin (txt veya excel): ")
    if output_format == 'txt':
        with open(f"{output_file}.txt", 'w') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Linkler {output_file}.txt dosyasına kayıt edildi.\n-HeJo")
    elif output_format == 'excel':
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Links"
        for index, link in enumerate(links, start=1):
            ws.cell(row=index, column=1, value=link)
        excel_file = f"{output_file}.xlsx"
        wb.save(excel_file)
        print(f"Linkler {excel_file} dosyasına kayıt edildi.\n-HeJo")
    else:
        print("Bilinmeye fırman şunları deniyin: txt or excel.")
else:
    print("Link bulunamadı.")
