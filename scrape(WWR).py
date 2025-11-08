import requests
from bs4 import BeautifulSoup
import re

url = "https://weworkremotely.com/remote-full-time-jobs?page=1"
all_jobs = []


def scrape_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]
    
    for job in jobs:
        
        try:
            title = job.find("h3", class_="new-listing__header__title").text
            company = job.find("p", class_="new-listing__company-name").text
            location_tag = job.find("p", class_="new-listing__company-headquarters")
            location = location_tag.text if location_tag else "N/A"
            application = job.find("a", class_="listing-link--unlocked").get("href")
        
            # application = job.find("a")["href"]
            # ㄴ 클래스가 없을 때 사용 가능.

            # application = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
            # ㄴ 해당 클래스명을 가진 div 태그의 다음 태그에서 href를 추출하는 태그
        
            if application is None:
                application = "There's no link"
            else:
                application = f"https://weworkremotely.com{application}"
            
            job_dir = {
                "title": title,
                "company": company,
                "location": location,
                "application": application
            }
        
            all_jobs.append(job_dir)
        
        except AttributeError:
            pass


def all_pages(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, "html.parser")
    pages = soup.find("span", class_="last").find('a').get("href")
    last_page_number = int(re.search(r'page=(\d+)', pages).group(1))
    return last_page_number


for page in range(all_pages(url)):
    scrape_pages(f"https://weworkremotely.com/remote-full-time-jobs?page={page+1}")
    
print(len(all_jobs))