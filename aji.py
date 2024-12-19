import requests
import argparse
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def check_git_existence(url):
    # Daftar URL yang umum digunakan untuk mencari direktori .git
    git_paths = [
        ".git/",
        ".git/config",
        ".git/HEAD",
        ".git/objects/"
    ]
    
    vulnerable_paths = []  # Menyimpan jalur yang menyebabkan kerentanannya

    # Mengecek setiap jalur .git
    for path in git_paths:
        full_url = url + '/' + path
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                vulnerable_paths.append(full_url)  # Simpan URL lengkap yang rentan
        except requests.exceptions.RequestException:
            continue  # Jika ada error, lanjutkan ke jalur berikutnya

    # Output status berdasarkan hasil pemindaian
    print(f"{Fore.YELLOW}[+]Scanning Url: {url}")
    
    if vulnerable_paths:
        print(f"{Fore.RED}[+]Vulnerable")
        for path in vulnerable_paths:
            print(f"    - {path}")  # Menampilkan URL lengkap yang rentan
    else:
        print(f"{Fore.GREEN}[+]Not Vulnerable")
    
    # Menambahkan garis pemisah antar hasil
    print(f"{Fore.WHITE}{'-'*40}\n")

def scan_single_domain(domain):
    # Pastikan domain dimulai dengan http:// atau https://
    if not domain.startswith('http://') and not domain.startswith('https://'):
        domain = 'https://' + domain  # Default ke https:// jika tidak ada protocol
    check_git_existence(domain)

def scan_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
            for domain in domains:
                domain = domain.strip()
                if not domain.startswith('http://') and not domain.startswith('https://'):
                    domain = 'https://' + domain  # Default ke https:// jika tidak ada protocol
                check_git_existence(domain)
    except FileNotFoundError:
        print(f"{Fore.RED}File {file_path} not found.")

def main():
    # Setup argparse untuk menangani command-line arguments
    parser = argparse.ArgumentParser(description="Tools untuk mencari file .git di domain atau subdomain.")
    
    # Opsi -d untuk domain tunggal
    parser.add_argument('-d', '--domain', type=str, help="Domain untuk dipindai (misal: example.com atau https://example.com).")
    
    # Opsi -f untuk file yang berisi daftar domain
    parser.add_argument('-f', '--file', type=str, help="File yang berisi daftar domain atau subdomain.")
    
    # Parsing argumen
    args = parser.parse_args()

    if args.domain:
        scan_single_domain(args.domain)  # Scan domain tunggal
    elif args.file:
        scan_from_file(args.file)  # Scan domain dari file
    else:
        print(f"{Fore.RED}Harap masukkan domain dengan -d atau file dengan -f.")

if __name__ == "__main__":
    main()
