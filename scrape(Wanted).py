from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import time


class JobScraper:
    def __init__(self, keyword):
        self.keyword = keyword
        self.jobs_parsed = []

    def scrape(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position")
            time.sleep(2)

            # 스크롤 끝까지
            prev_height = 0
            while True:
                page.keyboard.down("End")
                time.sleep(3)
                curr_height = page.evaluate("document.body.scrollHeight")
                if curr_height == prev_height:
                    break
                prev_height = curr_height

            content = page.content()
            browser.close()

        soup = BeautifulSoup(content, "html.parser")
        self.jobs_list = soup.find_all("div", class_="JobCard_container__zQcZs")

    def parse_jobs(self):
        for job in self.jobs_list:
            title_ = job.find("strong", class_="JobCard_title___kfvj")
            company_ = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu")
            career_ = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l")
            rewards_ = job.find("span", class_="JobCard_reward__oCSIQ")

            job_dir = {
                "Title": title_.text if title_ else "N/A",
                "Company": company_.text if company_ else "N/A",
                "Career": career_.text if career_ else "N/A",
                "Rewards": rewards_.text if rewards_ else "N/A"
            }
            self.jobs_parsed.append(job_dir)

    def save_to_csv(self):
        with open(f"{self.keyword}.csv", "w", newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Company", "Career", "Rewards"])
            writer.writeheader()
            writer.writerows(self.jobs_parsed)


if __name__ == "__main__":
    keywords = ["nestjs", "flutter", "java"]
    scraper = JobScraper(keywords[0])
    scraper.scrape()
    scraper.parse_jobs()
    scraper.save_to_csv()