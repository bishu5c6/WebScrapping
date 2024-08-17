from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=SI8S7XFM9KC6&qid=1723791767&sprefix=laptop%2Caps%2C217&ref=sr_pg_2")


    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    print(elems)
    for elem in elems:
        print(elem.text)

#print(elem.text) #it gives all the element in the string
#print(elem.get_attribute("outerHTML"))
    time.sleep(2)
    driver.close()