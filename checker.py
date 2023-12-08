import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from datetime import datetime
from tqdm import tqdm
from colorama import Fore, Style  
import time 

def print_error(message):
    """Print error messages in red."""
    print(Fore.RED + message + Style.RESET_ALL)

def print_info(message):
    """Print informational messages in cyan."""
    print(Fore.CYAN + message + Style.RESET_ALL)

def print_success(message):
    """Print success messages in green."""
    print(Fore.GREEN + message + Style.RESET_ALL)

def fetch_proxies(api_url):
    """Fetch proxies from the given API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx HTTP status codes
        time.sleep(1)  # Introduce a delay of 1 second to allow the server to respond and load content
        return {proxy.strip() for proxy in response.text.split('\n') if proxy.strip()}
    except requests.exceptions.RequestException as e:
        print_error(f"[fetching] Error fetching proxies from {api_url}: {e}")
        return set()

def check_proxy(proxy, threat_count):
    """Check the validity of a proxy by making a request to Google."""
    url = "https://www.google.com"
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return proxy, True
        elif response.status_code == 302:
            return proxy, False  # Consider 302 as not working
    except requests.exceptions.RequestException:
        pass
    return proxy, False

def save_proxies_to_file(proxies, filename):
    """Save proxies to a file."""
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    try:
        with open(filename, 'w') as file:
            for proxy, is_working in proxies:
                if is_working:
                    file.write(str(proxy) + '\n')
        print_success(f"[save] Saved working proxies in {filename}")
    except Exception as e:
        print_error(f"[save] Error saving proxies to {filename}: {e}")

def display_menu():
    print("\n"
      "                                 " + Fore.LIGHTWHITE_EX + "  ╦ ╦╔═╗╦  ╔═╗             \n"
      "                                 " + Fore.LIGHTCYAN_EX + "  ╠═╣║╣ ║  ╠═╝             \n"
      "                                 " + Fore.LIGHTCYAN_EX + "  ╩ ╩╚═╝╩═╝╩                \n"
      "             " + Fore.LIGHTCYAN_EX + "        ══╦═════════════════════════════════╦══\n"
      "             " + Fore.LIGHTCYAN_EX + "╔═════════╩═════════════════════════════════╩═════════╗\n"
      "             " + Fore.LIGHTCYAN_EX + "║ " + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTCYAN_EX + "        |" + Fore.LIGHTWHITE_EX + " Fetch and Check Proxies                  " + Fore.LIGHTCYAN_EX + "║\n"
      "             " + Fore.LIGHTCYAN_EX + "║ " + Fore.LIGHTWHITE_EX + "2" + Fore.LIGHTCYAN_EX + "        |" + Fore.LIGHTWHITE_EX + " Exit                                     " + Fore.LIGHTCYAN_EX + "║\n"
      "             " + Fore.LIGHTCYAN_EX + "╠═════════════════════════════════════════════════════╣\n"
      "             " + Fore.LIGHTCYAN_EX + "║ " + Fore.LIGHTWHITE_EX + "CREATOR" + Fore.LIGHTCYAN_EX + "  |" + Fore.LIGHTWHITE_EX + " @W_A_G_O_N_E | t.me/IgaAlts              " + Fore.LIGHTCYAN_EX + "║\n"
      "             " + Fore.LIGHTCYAN_EX + "║ " + Fore.LIGHTWHITE_EX + "YOU♥" + Fore.LIGHTCYAN_EX + "     |" + Fore.LIGHTWHITE_EX + " Please star the project :)               " + Fore.LIGHTCYAN_EX +  "║\n"
      "             " + Fore.LIGHTCYAN_EX + "║ " + Fore.LIGHTWHITE_EX + "version" + Fore.LIGHTCYAN_EX + "  |" + Fore.LIGHTWHITE_EX + " Release v1.2                             " + Fore.LIGHTCYAN_EX +  "║\n"
      "             " + Fore.LIGHTCYAN_EX + "╚═════════════════════════════════════════════════════╝\n")



def fetch_check_save_proxies():
    ascii_art_filename = 'ascii_art.txt'
    try:
        with open(ascii_art_filename, 'r') as ascii_art_file:
            ascii_art_content = ascii_art_file.read()
            print(Fore.GREEN + ascii_art_content + Style.RESET_ALL)
    except FileNotFoundError:
        print_error(f"Error: {ascii_art_filename} not found!")

    total_proxies_fetched = 0
    api_urls = [
         "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
         "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
         "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
         "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
         "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
         "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
         "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
         "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
         "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
         "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
         "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
         "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
         "https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt",
         "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
         "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt"
        

    ]

    all_proxies = set()
    for api_url in api_urls:
        print_info(f"[fetching] Getting proxies from {api_url}...")
        proxies_from_api = fetch_proxies(api_url)
        all_proxies.update(proxies_from_api)

    total_proxies_fetched = len(all_proxies)
    print_info(f"[fetching] Found {total_proxies_fetched} proxies in total. \n")

    try:
        threat_count = int(input(Fore.LIGHTCYAN_EX+"╔═══"+Fore.LIGHTCYAN_EX+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTCYAN_EX+"User"+Fore.CYAN+"]"+Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> [amount of checking threats]: " + Style.RESET_ALL))
    except ValueError:
        print_error("Invalid input. Please enter a valid integer.")
        return

    os.system('clear')
    print(Fore.GREEN + ascii_art_content + Style.RESET_ALL)
    print_info("[checking] Checking the proxies...")

    working_proxies = []
    not_working_proxies = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threat_count) as executor:
        pbar = tqdm(total=len(all_proxies), bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} {postfix}', unit=' proxies')
        for result in executor.map(lambda proxy: check_proxy(proxy, threat_count), all_proxies):
            proxy, is_working = result
            if is_working:
                working_proxies.append((proxy, is_working))
            else:
                not_working_proxies.append(result)
            pbar.set_postfix(Working=len(working_proxies), NotWorking=len(not_working_proxies))
            pbar.update(1)

        pbar.close()

    os.system('clear')
    print(Fore.GREEN + ascii_art_content + Style.RESET_ALL)

    output_filename = input(Fore.LIGHTCYAN_EX+"╔═══"+Fore.LIGHTCYAN_EX+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTCYAN_EX+"User"+Fore.CYAN+"]"+Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> [name of the file to save]: " + Style.RESET_ALL)

    save_proxies_to_file(working_proxies, output_filename)

    input("Press any key to go to menu ...")

def main_menu():
    while True:
        display_menu()
        choice = input(Fore.LIGHTCYAN_EX+"╔═══"+Fore.LIGHTCYAN_EX+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTCYAN_EX+"User"+Fore.CYAN+"]"+Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> [choose an option]: " + Style.RESET_ALL)
        if choice == "1":
            fetch_check_save_proxies()
        elif choice == "2":
            print_info("Exiting the program. Goodbye!")
            break
        else:
            print_error("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
