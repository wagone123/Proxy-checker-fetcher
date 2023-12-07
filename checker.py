import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from datetime import datetime
from tqdm import tqdm
from colorama import Fore, Style  # Import colorama modules

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
        proxies = response.text.split('\n')
        proxies = {proxy.strip() for proxy in proxies if proxy.strip()}  # Use a set to remove duplicates
        return proxies
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
            for proxy in proxies:
                file.write(proxy + '\n')
        print_success(f"[save] Saved working proxies in {filename}")
    except Exception as e:
        print_error(f"[save] Error saving proxies to {filename}: {e}")

def main():
    ascii_art_filename = 'ascii_art.txt'
    try:
        with open(ascii_art_filename, 'r') as ascii_art_file:
            ascii_art_content = ascii_art_file.read()
            print(Fore.MAGENTA + ascii_art_content + Style.RESET_ALL)
    except FileNotFoundError:
        print_error(f"Error: {ascii_art_filename} not found!")

    total_proxies_fetched = 0
    api_urls = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt"  # Additional source
    ]

    all_proxies = set()
    for api_url in api_urls:
        print_info("[fetching] Getting proxies...")
        proxies_from_api = fetch_proxies(api_url)
        all_proxies.update(proxies_from_api)

    total_proxies_fetched = len(all_proxies)
    print_info(f"[fetching] Found {total_proxies_fetched} proxies in total.")

    try:
        threat_count = int(input(Fore.YELLOW + "[checking] Please enter the amount of threats to use while checking: " + Style.RESET_ALL))
    except ValueError:
        print_error("Invalid input. Please enter a valid integer.")
        return

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
    print(Fore.MAGENTA + ascii_art_content + Style.RESET_ALL)

    output_filename = input(Fore.BLUE + "[save] What should the file be named (working proxies without extension): " + Style.RESET_ALL)

    save_proxies_to_file(working_proxies, output_filename)

    input("Press any key to close ...")

if __name__ == "__main__":
    main()
