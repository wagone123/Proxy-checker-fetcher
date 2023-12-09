# Proxy Checker

Proxy Checker is a Python script that fetches proxy lists from various sources, checks their validity, and saves the working proxies to a file. It supports multi-threading for efficient checking and includes features like duplicate proxy removal.

## Features

- Fetch proxies from multiple sources.
- Check the validity of proxies using multi-threading.
- Save working proxies to a file.
- Remove duplicate proxies.

## Requirements

Make sure you have Python installed. Install the required dependencies using:

```pip install -r requirements.txt```

## Usage

Clone the repository:

```git clone https://github.com/wagone123/Proxy-checker-fetcher```

```cd proxy-checker-fetcher```

Run the script:

```python checker.py```

Follow the on-screen prompts to set the number of threats, choose a filename, and monitor the progress.

## Sources

Proxy lists are fetched from the following sources:

1. [TheSpeedX SOCKS List](https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt)
2. [ProxyScrape API](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)
3. [jetkai Proxy List](https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt)
4. [MuRongPIG Proxy Master](https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt)
5. [prxchk Proxy List](https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt)
6. [ErcinDedeoglu Proxies](https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt)
7. [officialputuid KangProxy](https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt)
8. [Anonym0usWork1221 Free-Proxies](https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt)
9. [Zaeem20 FREE_PROXIES_LIST](https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt)
10. [proxy4parsing Proxy List](https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt)
11. [ALIILAPRO Proxy](https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt)
12. [vakhov fresh-proxy-list](https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt)
13. [yuceltoluyag GoodProxy](https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt)
14. [zevtyardt Proxy List](https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt)
15. [aslisk proxyhttps](https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt)

These sources collectively contribute to a robust and diverse pool of proxies for various applications.


Feel free to add more sources to the `api_urls` list in the script.

