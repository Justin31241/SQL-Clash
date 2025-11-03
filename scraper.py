from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup 
import time

driver = webdriver.Chrome()
driver.get("https://royaleapi.com/player/VRV9CV9QP/decks")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'img[data-card-key="hog-rider"]'))
    )

    html_content = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    hog_rider_img = soup.find('img', attrs={'data-card-key': 'hog-rider'})

    if hog_rider_img:
        image_url = hog_rider_img['src']
        alt_text = hog_rider_img['alt']
        print(f"Found! Alt: {alt_text}, URL: {image_url}")
    else:
        print("Can't find card")

except Exception as e:
    print(f"Error: {e}")
    driver.quit()