import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

def scrape_jobs():
    URL = "https://realpython.github.io/fake-jobs/"
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract job elements
    job_elements = soup.find_all("div", class_="card-content")

    jobs = []
    for job in job_elements:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        apply_link = job.find("a", text="Apply")["href"]

        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Apply Link": apply_link,
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Convert to DataFrame
    df = pd.DataFrame(jobs)

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    output_path = "data/job_listings.csv"
    df.to_csv(output_path, index=False)

    print(f"✅ {len(df)} job listings scraped successfully!")
    print(f"📁 Data saved to: {output_path}")

if __name__ == "__main__":
    scrape_jobs()
