import requests
import json

def fetch_content(input_value, version):
    if version == "r1":
        url = f"https://deepseek-r1.istebutolga.workers.dev/?prompt={input_value}"
    elif version == "v3":
        url = f"https://deepv3.istebutolga.workers.dev/?prompt={input_value}"
    else:
        print("Geçersiz versiyon! 'r1' veya 'v3' kullanın.")
        return
    
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        print(data['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    while True:
        user_input = input("Lütfen bir input girin (çıkmak için 'exit' yazın): ")
        if user_input.lower() == "exit":
            print("Çıkış yapılıyor...")
            break
        
        parts = user_input.split(" ", 1)
        if len(parts) == 2 and parts[0] in ["/r1", "/v3"]:
            version = parts[0][1:]
            prompt = parts[1]
            fetch_content(prompt, version)
        else:
            print("Hatalı giriş! '/r1 <prompt>' veya '/v3 <prompt>' formatını kullanın.")
