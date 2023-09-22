from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import imageDownFun
import os

searchInput = input("어떤 이미지를 찾을까요? ")
searchCount = int(input("몇 개의 사진을 다운받을까요? "))

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless") # Chrome 창 안보이게  

# Chrome 웹 드라이버 인스턴스 생성 (헤드리스 모드 활성화)
driver = webdriver.Chrome(options=chrome_options)

# 주어진 URL로 이동
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=apple&oquery=chicken&tqi=idz61lprvN8ssKRPlSVssssstYV-204276"
driver.get(url)

# id가 "nx_query"인 검색창을 찾아 "apple" 입력
search_box = driver.find_element(By.ID, "nx_query")
search_box.clear()  # 기존에 있던 내용 삭제

search_box.send_keys(searchInput)

# 엔터 키 입력하여 검색
search_box.send_keys(Keys.RETURN)

# 결과를 보기 위해 잠시 대기 
import time

time.sleep(5)

# 스크롤을 사이드바 밑까지 내림
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#driver=웹페이지

# 추가로 로딩되는 요소를 기다림
time.sleep(5)

# 현재 URL 출력
print("="*100)
print("driver.current_url=",driver.current_url)
print("-"*100)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
items= soup.select('.photo_bx > .thumb > a img')

for item in items:
   url=item["src"]
   if  "jpg" in url or "png" in url :
        print( url )
        ret=imageDownFun.imageDown(url)
        print(ret)
        os.system(f"start images/{ret}")
        found += 1
   if found >= searchCount:
        break

print(f"{found}/{searchCount}개의 사진을 다운받았습니다.")


# 웹 드라이버 종료
driver.quit()

#컬러 사진만 받기