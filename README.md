# 🕵️‍♂️ Job Scraper – Fake Jobs Web Scraping Project

A simple Python web scraping project that extracts job listings (title, company, location, and application link) from the [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) website.  
The scraped data is automatically saved as a CSV file for easy access and analysis.

---

## 📋 Features
- Scrapes job listings dynamically from a website.  
- Extracts **job title**, **company name**, **location**, and **apply link**.  
- Saves all data to a CSV file with timestamps.  
- Automatically creates a `data` folder if it doesn’t exist.  

---

## 🧰 Technologies Used
- **Python 3**  
- **Requests** – to fetch the HTML page.  
- **BeautifulSoup (bs4)** – to parse and extract job details.  
- **Pandas** – to organize and export data to CSV.  
- **Datetime & OS** – for timestamps and file handling.  

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lenatisha/Job-Listing-Scraper.git
   cd Job Listing Scraper
