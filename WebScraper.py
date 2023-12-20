import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

page = requests.get(url)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

# ResultsContainer has all the job postings
results = soup.find(id="ResultsContainer")
# print(results.prettify())

# Div card-content holds one job listing
job_elements = results.find_all("div", class_="card-content")

# Iterate through each job element and print with two spaces
# for job in job_elements:
#    print(job, end="\n"*2)

# either full class name or just class name containing works(aka title or subtitle is 6 company
for job in job_elements:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="subtitle is-6 company")
    location = job.find("p", class_="location")
    # print(title.text.strip())
    # print(company.text.strip())
    # print(location.text.strip())
    # print()

# Narrowing the job searches by getting only developer jobs for python
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())  # only gives the title headers
# print(python_jobs)
# print(len(python_jobs)) #number of python jobs

python_job_elements = [h2_element.parent.parent.parent for h2_element in
                       python_jobs]  # get the 3rd parent (which contains all the descriptors we need)
# element for each object in python jobs

for job in python_job_elements:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
