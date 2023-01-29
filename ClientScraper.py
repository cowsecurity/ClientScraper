#!/usr/bin/python3

import re
import requests
import os
import pyfiglet

banner = pyfiglet.figlet_format("ClientScraper")

print(banner)
print("version 1.1                  by 0xFTW")

def scrape_emails_and_phones(url):
    try:
        response = requests.get(url, timeout=10)
        html_content = response.text
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html_content)
        phone_pattern = re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b")
        phones = phone_pattern.findall(html_content)
        return emails, phones
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return [], []

def write_to_file(filename, data):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            for item in data:
                file.write("%s\n" % item)
    else:
        with open(filename, "a") as file:
            for item in data:
                file.write("%s\n" % item)

def search_google(query, num_results=10):
    try:
        response = requests.get(f"https://www.google.com/search?q={query}&num={num_results}")
        html_content = response.text
        links = re.findall(r'href="(https?://.*?)"', html_content)
        return links
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def main():
    print("ClientScraper")
    google_dork = input("Enter Google Dork: ")
    data_to_scrape = input("Enter data to scrape (emails, phones, or both): ")
    confirm = input(f"Confirm scrape {data_to_scrape}? (yes/no): ")
    if confirm.lower() != "yes":
        print("Scrape cancelled")
        return
    links = search_google(google_dork)
    count = 0
    for link in links:
        emails, phones = scrape_emails_and_phones(link)
        if data_to_scrape == "emails" or data_to_scrape == "both":
            write_to_file("emails.txt", emails)
        if data_to_scrape == "phones" or data_to_scrape == "both":
            write_to_file("phones.txt",phones)

if __name__ == "__main__":
    main()
