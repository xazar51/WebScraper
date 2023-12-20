import requests
from bs4 import BeautifulSoup

url = "https://remote.co/remote-jobs/developer"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

all_jobs = soup.find("div", class_="card bg-white m-0")

job_listing_titles = all_jobs.find_all("span", class_="font-weight-bold larger")

job_listing_companies = all_jobs.find_all("p", class_="m-0 text-secondary")

job_listing_urls = all_jobs.find_all("a", class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")

for i, (job_title, job_company, job_url) in enumerate(zip(job_listing_titles,job_listing_companies,job_listing_urls)):
    print(job_title.text)
    print(job_company.text.strip())
    print(url + job_url.get('href'))
    print("\n")


#print(job_listings)
