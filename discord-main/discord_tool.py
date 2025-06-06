'''
İnstagram bymer_ak
discord https://discord.gg/eAknugSZZ7 
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import requests
import asyncio
import aiohttp

def passwo():
    def get_token(username, password):
        login_url = "https://discord.com/api/v9/auth/login"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        }
        login_payload = {
            "login": username,
            "password": password,
            "undelete": False,
            "captcha_key": None,
            "login_source": None,
            "gift_code_sku_id": None,
        }


        response = requests.post(login_url, json=login_payload, headers=headers)

        if response.status_code == 200:
            token = response.json().get('token')
            print(f"Alınan token: {token}")
            return token
        else:
            print(f"Login failed: {response.status_code} - {response.text}")
            return None

    def login_and_join(token):
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        }
        

        user_info_url = "https://discord.com/api/v9/users/@me"
        response = requests.get(user_info_url, headers=headers)
        
        if response.status_code == 200:
            print("User info retrieved successfully")
            print(response.json())
        else:
            print(f"Failed to retrieve user info: {response.status_code} - {response.text}")

    username = input("Discord'a kayıtlı mail adresi: ")
    password = input("Discord şifresi: ")

    token = get_token(username, password)

    if token:
        login_and_join(token)

def degistir():
    m = str(input("Yeni ismi girin : "))
    ff = input("Yeni pp dosya yolu giriniz : ")
    tok = input("Tokeni giriniz : ")
    import discord

    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        # Get the bot's user object.
        bot = client.user
        
        # Set the bot's name and description.
        new_name = m
        
        # Change the bot's name and description.
        await bot.edit(username=new_name)
        

        # Change the bot's profile picture (avatar).
        with open(ff, "rb") as avatar_file:
            await bot.edit(avatar=avatar_file.read())

    # Run the bot with your token
    client.run(tok)

def sel():
    def login_and_join(token, gecko_driver_path):

        firefox_options = Options()
        firefox_options.set_preference("dom.webdriver.enabled", False)
        firefox_options.set_preference('useAutomationExtension', False)
        firefox_options.headless = False  
        driver = webdriver.Firefox(service=Service(gecko_driver_path), options=firefox_options)


        driver.get("https://discord.com/login")

        script = """
        function login(token) {
            setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
                location.reload();
            }, 2500);
        }
        """
        driver.execute_script(script + f'login("{token}")')

        time.sleep(5)

    gecko_driver_path = input("GeckoDriver dosya yolu: ")
    token = input("Discord tokeni: ")
    login_and_join(token, gecko_driver_path)

async def send_message(session, url, headers, message_data):
    async with session.post(url, headers=headers, json=message_data) as response:
        if response.status == 200:
            print('Message sent successfully.')
        else:
            print('An error occurred. Message could not be sent.')

async def bump_channel(token, channel_id):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }


    message_content = input("Spam içeriği: ")
    tts_option = input("TTS aktif edilsinmi (True/False): ")
    num_times_to_send = int(input("Kaç saniyede 1 mesajı göndersin: "))

    message_data = {
        'content': message_content,
        'tts': bool(tts_option)
    }

    urls = [f'https://discord.com/api/v9/channels/{channel_id}/messages'] * num_times_to_send

    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for url in urls:
            task = asyncio.ensure_future(send_message(session=session, url=url,
                                                    headers=headers,
                                                    message_data=message_data))
            tasks.append(task)

        await asyncio.gather(*tasks)

def spam():
    t = input("Tokeni giriniz: ")
    cid = input("Spam atılacak kanalın ID: ")
    token = t
    channel_id = cid

    loop = asyncio.get_event_loop()
    loop.run_until_complete(bump_channel(token=token, channel_id=channel_id))

print('''
██████████    ███                                          █████
░░███░░░░███  ░░░                                          ░░███ 
░███   ░░███ ████   █████   ██████   ██████  ████████   ███████ 
░███    ░███░░███  ███░░   ███░░███ ███░░███░░███░░███ ███░░███ 
░███    ░███ ░███ ░░█████ ░███ ░░░ ░███ ░███ ░███ ░░░ ░███ ░███ 
░███    ███  ░███ ░░░░███░███  ███░███ ░███ ░███     ░███ ░███ 
██████████   █████ ██████ ░░██████ ░░██████  █████    ░░████████
░░░░░░░░░░   ░░░░░ ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░ 
                                                                
                                                                
                                                                
███████████                   ████                              
░█░░░███░░░█                  ░░███                              
░   ░███  ░   ██████   ██████  ░███                              
    ░███     ███░░███ ███░░███ ░███                              
    ░███    ░███ ░███░███ ░███ ░███                              
    ░███    ░███ ░███░███ ░███ ░███                              
    █████   ░░██████ ░░██████  █████                             
    ░░░░░     ░░░░░░   ░░░░░░  ░░░░░    

made by Im just a girl                         
    ''')
print('''
1 - token ile giriş
2 - Şifre ile ayrıntılı bilgi alma
3 - Spam 
4 - Bilgileri değiştirme
99 - Çıkış    
    ''')


i = int(input(""))
if i == 1:
    sel()
elif i == 2:
    passwo()
elif i == 3:
    spam()
elif i ==4:
    degistir()
elif i == 99:
    exit()
else:
    print("Yanlış giriş")
