import requests
import re
from bs4 import BeautifulSoup
from termcolor import cprint


def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def validate_input(data_to_scrape, google_dork):
    if data_to_scrape not in ['email', 'phone']:
        print("Invalid data to scrape, only 'email' and 'phone' are supported")
        return False
    if not google_dork:
        print("Google Dork is required")
        return False
    return True

def scrape_data(data_to_scrape, google_dork, limit=100):
    if not validate_input(data_to_scrape, google_dork):
        return

    search_url = f'https://www.google.com/search?q={google_dork}&num={limit}'
    soup = get_soup(search_url)
    links = [link.get('href') for link in soup.find_all("a")]
    emails = []
    phones = []

    for link in links:
        if not link.startswith('http'):
            # skip links that are not URLs
            continue
        try:
            page = requests.get(link, headers=headers)
            page_content = page.content.decode('utf-8')
        except Exception as e:
            # handle exceptions that might occur during request
            print(f'Error accessing {link}: {e}')
            continue

        if data_to_scrape == 'email':
            # scrape emails using BeautifulSoup
            page_soup = BeautifulSoup(page_content, 'html.parser')
            page_emails = page_soup.stripped_strings
            page_emails = (email for email in page_emails if '@' in email)
            emails.extend(page_emails)
        else:
            # scrape phones using regular expression
            phone_pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
            page_phones = re.findall(phone_pattern, page_content)
            phones.extend(page_phones)

    if data_to_scrape == 'email':
        return emails
    else:
        return phones
    
def save_to_file(data, data_to_scrape, google_dork):
    filename = f"{data_to_scrape}_{google_dork.replace(' ', '_')}.txt"
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")
    print(f"Scraped data saved to {filename}")
    
def print_banner():
    cprint("ClientScraper", 'red', attrs=['bold'])
    cprint(" version 1.2 by 0xFTW", 'yellow', attrs=['bold'])

if __name__ == '__main__':
    print_banner()
    data_to_scrape = input('Enter data to scrape (email or phone): ')
    google_dork = input('Enter Google Dork: ')
    result = scrape_data(data_to_scrape, google_dork)
    if result:
        save_to_file(result, data_to_scrape, google_dork)
    else:
        print("No data found")