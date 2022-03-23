from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://techwithtim.net")
print(driver.title)

#all_iframes = driver.find_elements_by_tag_name("iframe")
#print(' ')

#def close_add():
   #for iframe in all_iframes:
      #driver.switch_to.frame(iframe)
     # print("Ad Found")
      #driver.switch_to.default_content()

#print('Total Ads: ' + str(len(all_iframes)))

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()





#equasion = driver.find_element_by_xpath("//i[@class='fa fa-search']/following-sibling::span[1]")
#if equasion.
#time.sleep(5)
