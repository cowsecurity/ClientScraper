# Client Scraper

[![Python](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/downloads/)


A Python script to scrape email addresses and phone numbers from websites using Google Dork.

## Features
- Scrapes email addresses and phone numbers from websites.
- Accepts a Google Dork as input to search the web.
- Saves the scraped data to a text file.
- Supports user-agent rotation to avoid detection.

## Requirements
- Python 3.x
- requests
- BeautifulSoup4
- termcolor
- pyfiglet

## Installation
To install the required dependencies, run the following command:

```shell
pip install -r requirements.txt
```

## Usage

```shell
python ClientScraper.py
```

Enter the data you want to scrape (email or phone) and the Google Dork. The scraped data will be saved to a text file with a filename in the format `data_to_scrape_google_dork.txt`.

## Contribution
Feel free to open an issue or a pull request if you have any suggestions or find any bugs.

<!-- ## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->