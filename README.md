# Proxy Checker

Proxy Checker is a Python script that fetches proxy lists from various sources, checks their validity, and saves the working proxies to a file. It supports multi-threading for efficient checking and includes features like duplicate proxy removal.

## Features

- Fetch proxies from multiple sources.
- Check the validity of proxies using multi-threading.
- Save working proxies to a file.
- Remove duplicate proxies.

## Requirements

Make sure you have Python installed. Install the required dependencies using:

```bash
pip install -r requirements.txt

## Usage

Clone the repository:

```bash
git clone https://github.com/your-username/proxy-checker.git
cd proxy-checker

Run the script:

```bash
python checker.py

Follow the on-screen prompts to set the number of threats, choose a filename, and monitor the progress.

## Sources

Proxy lists are fetched from the following sources:

1. [TheSpeedX SOCKS List](https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt)
2. [ProxyScrape API](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)
3. [jetkai Proxy List](https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt)
4. [MuRongPIG Proxy Master](https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt)
5. [prxchk Proxy List](https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt)
6. [ErcinDedeoglu Proxies](https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt)

Feel free to add more sources to the `api_urls` list in the script.

