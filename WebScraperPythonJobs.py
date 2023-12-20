import requests
from bs4 import BeautifulSoup

url = "https://pythonjobs.github.io/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="content")

job_listings = results.find_all("section", class_="job_list")

for job in job_listings:
    title = job.find_all("h1")
    info = job.find_all("span", class_="info")
    detail = job.find_all("p", class_="detail")
    i = 0
    j = 1
    k = 2
    l = 3
    d = 0
    for t in title:
        print(t.text.strip())
        print(info[i].text.strip())
        print(info[j].text.strip())
        print(info[k].text.strip())
        print(info[l].text.strip())
        print(detail[d].text.strip())
        i += 4
        j += 4
        k += 4
        l += 4
        d += 1
        print()
