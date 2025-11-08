from playwright.sync_api import sync_playwright
import time


def scrape_remoteok_python_jobs():
    # sync_playwright()로 동기방식 설정
    with sync_playwright() as p:
        # chromium.launch(headless==True)로 브라우저를 화면없이(백그라운드) 실행
        browser = p.chromium.launch(headless=True)
        # 새로운 페이지를 열고 해당 url로 이동
        page = browser.new_page()
        page.goto("https://remoteok.com/remote-python-jobs", wait_until="networkidle")

        # 일부 콘텐츠가 늦게 로딩될 수 있으니 로딩 대기
        time.sleep(2)

        # 검사를 통해 채용 정보가 있는 태그 추출
        jobs = page.query_selector_all("tr.job")

        # 빈 리스트 생성
        job_list = []
        for job in jobs:
            # 각 채용 정보에서 세부사항 추출, 없으면 None 반환
            title = job.query_selector("h2")  # 직무 제목
            company = job.query_selector(".companyLink h3")  # 회사 이름
            tags = job.query_selector_all(".tags .tag")  # 기술 태그
            link = job.get_attribute("data-href")  # 상세 페이지 링크

            job_data = {
                # 딕셔너리에 세부사항 저장, 오류 방지
                "title": title.inner_text().strip() if title else None,
                "company": company.inner_text().strip() if company else None,
                "tags": [tag.inner_text().strip() for tag in tags] if tags else [],
                "link": f"https://remoteok.com{link}" if link else None
            }
            # 빈 리스트에 각 채용정보의 딕셔너리 저장
            job_list.append(job_data)
        # 브라우저 종료 및 결과 반환
        browser.close()
        return job_list


# 실행 및 출력
if __name__ == "__main__":
    jobs = scrape_remoteok_python_jobs()
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} at {job['company']}")
        print(f"   Tags: {', '.join(job['tags'])}")
        print(f"   Link: {job['link']}\n")