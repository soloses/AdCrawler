import os
import requests
from colorama import init, Fore

init()

def print_ascii():
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⡀⠀⠀⢀⣀⣈⣳⣤⣤⣤⣤⣤⣤⣄⡀⠉⠳⣄⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⢠⣙⣶⡷⠶⠙⠁⣤⣿⡿⣻⣽⡏⠑⠪⣿⣿⠦⣤⠗⢢⡀⠀⠀⠀")
    print("⢶⣾⣟⢙⠀⠀⠀⠀⣰⡯⣗⢓⢷⣿⣷⣦⣰⣿⣽⣏⠛⢦⠀⠘⡦⡀⠀")
    print("⠀⠀⠛⢦⣲⡀⠀⠀⡿⠁⠉⠁⢾⣿⣟⣿⣿⣿⣿⡿⡄⠰⣧⡀⠱⠵⡀")
    print("⠀⠀⠀⠈⠙⠟⣆⠀⢷⠀⠀⠀⠸⣿⣷⡃⠀⠉⢙⣷⠃⠀⠈⠛⣖⠋⠀")
    print("⠀⠀⠀⢢⡘⠛⠛⠻⢎⣷⣄⣀⣀⠀⠀⠀⣀⣔⡯⠃⠀⠀⠀⠀⠹⡆⠀")
    print("⠀⠀⠀⠀⠈⠑⠒⠤⣄⡀⠈⠋⠫⠍⠯⠟⡍⡁⡀⣤⣤⡦⠶⠒⠀⠁⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠒⠒⠂⠀⠀⠀⠀⠈⠉⠳⠀⠀⠀⠀⠀")
    print("Admin Crawler v1 by solos")
    print("  solos@tutamail.com\n")

def find_admin_panel(url, wordlist_file):
    print("Crawling the website...")

    # Load wordlist from file
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().splitlines()

    for keyword in wordlist:
        admin_url = url + keyword
        response = requests.get(admin_url)
        if response.status_code == 200:
            print(Fore.GREEN + f"[+] Admin panel found: {admin_url}")
            return
        else:
            print(Fore.RED + f"[-] {admin_url} not found")

    print(Fore.RED + "[-] No admin panel found.")

def main():
    print_ascii()

    url = input("Enter the URL of the website: ")

    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    if not url.endswith('/'):
        url += '/'

    # Get the path to the wordlist file in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    wordlist_file = os.path.join(script_dir, 'wordlist.txt')

    find_admin_panel(url, wordlist_file)

if __name__ == "__main__":
    main()
