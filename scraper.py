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
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ui.padded.grid[id^="deck_"]'))
    )

    html_content = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    deck_containers = soup.select('div.ui.padded.grid[id^="deck_"]')

    for deck in deck_containers:
        print(deck)
    else:
        print("Can't find deck")

except Exception as e:
    print(f"Error: {e}")
    driver.quit()