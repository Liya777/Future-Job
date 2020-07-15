import requests
import random
from bs4 import BeautifulSoup

titles = []
locas = []
comps = []
sals = []
result = requests.get(
    "https://www.indeed.co.in/jobs?q=data+analyst&l="
)

scr = result.content
soup = BeautifulSoup(scr, 'lxml')

featured_jobs = soup.find_all('a', attrs={'data-tn-element': 'jobTitle'})
featured_locations = soup.findAll('div', attrs={'class': 'recJobLoc'})
featured_companies = soup.findAll('span', attrs={'class': 'company'})
featured_salaries = soup.findAll('span', attrs={'class': 'salary no-wrap'})

print("JOB TITLE")
for featured_job in featured_jobs:
    titles.append(featured_job.attrs['title'])

for title in titles:
    print(title)

print("LOCATION")
for location in featured_locations:
    locas.append(location.attrs['data-rc-loc'])

for loc in locas:
    print(loc)

print("COMPANY NAME")
for featured_company in featured_companies:
    comps.append(featured_company.text)

for comp in comps:
    print(comp)

print("SALARY")
for featured_salary in featured_salaries:
    sals.append(featured_salary.text)

for sal in sals:
    print(sal)
