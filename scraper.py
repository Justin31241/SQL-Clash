from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup 
import time

player_id = input("Enter Player ID Here: ") #Mine: VRV9CV9QP Ellio: QYCG8U098

driver = webdriver.Chrome()
driver.get(f"https://royaleapi.com/player/{player_id}/decks")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ui.padded.grid[id^="deck_"]')) 
        #The id^ means it checks for the element STARTING with deck_ | just id would check for literal
    )

    html_content = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    print(soup.select('div.ui.padded.grid[id^="games"]'))
    deck_containers = soup.select('div.ui.padded.grid[id^="deck_"]')
    

    for deck in deck_containers:
        print('Deck Found')
    else:
        print("Can't find deck")

except Exception as e:
    print(f"Error: {e}")
    driver.quit()


    