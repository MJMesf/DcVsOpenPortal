import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

download_dir = os.getcwd()

# config Edge options
edge_options = Options()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
edge_options.add_experimental_option("prefs", prefs)

# Initialize the Edge driver 
# make sure msedgedriver is installed and in PATH
driver = webdriver.Edge(options=edge_options)

try:
    # open the main search page
    main_url = "https://search.open.canada.ca/opendata/?owner_org=aafc-aac&page=1&sort=metadata_modified+desc"
    driver.get(main_url)
    
    # opens main page and goes to download page
    # timeout after 20 seconds
    print("Main Page")
    wait = WebDriverWait(driver, 20)
    
    # waits for the first button, searched by its characters
    first_button = wait.until(
         EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Download Search Results')]"))
    )
    first_button.click()

    wait.until(EC.url_changes(main_url))
    
    # finds button with id="download-btn" and click it
    second_button = wait.until(
         EC.element_to_be_clickable((By.ID, "download-btn"))
    )
    second_button.click()
    
    #buffer for download to start
    time.sleep(10)
    
    print("CSV Downloaded in File's Directory")
    
finally:
    driver.quit()
