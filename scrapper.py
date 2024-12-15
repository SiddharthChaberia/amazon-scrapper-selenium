from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
element='laptops'
page=0
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={element}&page={i}&qid=1734255390&sprefix=lapto%2Caps%2C263&ref=sr_pg_{i}")
    elems=driver.find_elements(By.CLASS_NAME,'puis-card-container')
    print(f"{len(elems)} element found on page {i}")
    for elem in elems:
        d=elem.get_attribute("outerHTML")
        with open(f'data/{element}_{page}.html', 'w', encoding='utf-8') as f:
            f.write(d)
            page+=1

    time.sleep(2)
driver.close()