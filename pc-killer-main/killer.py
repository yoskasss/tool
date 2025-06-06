import os
import random

def generate_random_data(size):
    return ''.join(chr(random.randint(0, 127)) for _ in range(size))

def create_large_text_file(file_path, size_gb):
    size_bytes = size_gb * 1024 * 1024 * 1024
    with open(file_path, 'wb') as file:
        while size_bytes > 0:
            chunk_size = min(size_bytes, 100 * 1024 * 1024)  # 100MB
            data = generate_random_data(chunk_size)
            file.write(data.encode('ascii'))
            size_bytes -= len(data)

if __name__ == "__main__":
    for i in range(1000):
        file_path = f"large_file_{i}.txt"
        size_gb = 1
        create_large_text_file(file_path, size_gb)
        print(f"{file_path} dosyası oluşturuldu ve içine yaklaşık 1GB veri yazıldı.")
