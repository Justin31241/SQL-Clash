from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

player_id = input("Enter Player ID Here: ")#Mine: VRV9CV9QP Ellio: QYCG8U098

options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)

driver.set_page_load_timeout(15) 

html_content = ""

try:
    print(f"Loading page for {player_id}...")
    try:
        driver.get(f"https://royaleapi.com/player/{player_id}/battles")
    except TimeoutException:
        print("Page load timed out! Stopping page load and checking for data anyway...")
        driver.execute_script("window.stop();")

    print("Checking if decks are visible...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ui.padded.grid[id^="deck_"]'))
    )
    print("Decks successfully detected.")
    html_content = driver.page_source

except Exception as e:
    print(f"Error during Selenium: {e}")

finally:
    driver.quit()

if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')
    deck_containers = soup.select('div.ui.padded.grid[id^="deck_"]')

    if not deck_containers:
        print("Can't find any decks (page might have failed to load completely).")
    else:
        print(f"Found {len(deck_containers)} decks:")
        for index, deck in enumerate(deck_containers[::2], 1):
            print(f" - Deck {index} Found (ID: {deck.get('id')})")



