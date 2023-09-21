from bs4 import BeautifulSoup
from selenium import webdriver# selenium 비동기 사이트
import time
import imageDownFun

driver = webdriver.Chrome()# Chrome 사용하겠다

# 웹 페이지 로드
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=chicken+&oquery=chicken+image&tqi=idqJSwprvTosshsevlVssssstpo-235214")


#5초 기다리기
time.sleep(5)

# 스크롤을 사이드바 밑까지 내림
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#driver=웹페이지

# 추가로 로딩되는 요소를 기다림
time.sleep(5)


html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')#img(태그) src(속성)->어느 class에 있지?


items= soup.select('.photo_bx > .thumb > a img')
print(items[0]["src"])

for item in items:
   url=item["src"]
   if  "jpg" in url or "png" in url :
        print( url )
        ret=imageDownFun.imageDown(url)
        print(ret)

driver.quit()