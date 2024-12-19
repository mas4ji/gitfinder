import requests
import argparse
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Daftar header untuk menghindari pemblokiran
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
    'Connection': 'keep-alive'
}

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
            # Menggunakan headers dan timeout untuk mencegah blokir
            response = requests.get(full_url, headers=headers, timeout=10)
            if response.status_code == 200:
                vulnerable_paths.append(full_url)  # Simpan URL lengkap yang rentan
            elif response.status_code == 403:
                print(f"{Fore.YELLOW}[+] Forbidden (403): {full_url}")
            elif response.status_code == 404:
                print(f"{Fore.YELLOW}[+] Not Found (404): {full_url}")
            else:
                print(f"{Fore.YELLOW}[+] Received status {response.status_code}: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[+] Error accessing {full_url}: {str(e)}")
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
    # Logo ASCII yang lebih rapi dengan pewarnaan
    print(Fore.CYAN + r"""
     _ __     __           __      __                __           
    ____ _(_) /_   / /__  ____ _/ /__   / /_  __  ______  / /____  _____
   / __ `/ / __/  / / _ \/ __ `/ //_/  / __ \/ / / / __ \/ __/ _ \/ ___/
  / /_/ / / /_   / /  __/ /_/ / ,<    / / / / /_/ / / / / /_/  __/ /    
  \__, /_/\__/  /_/\___/\__,_/_/|_|  /_/ /_/\__,_/_/ /_/\__/\___/_/     
 /____/                                                                  
    """)

    print(Fore.YELLOW + "Commands: ")
    print(Fore.GREEN + "    -d or --domain <domain>  : Scan a single domain")
    print(Fore.GREEN + "    -f or --file <file_path>  : Scan domains from a file")
    print(Fore.WHITE + "-"*40)
    main()
