from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

# Set the path to your webdriver (e.g., chromedriver.exe)
webdriver_path = "path/to/your/webdriver"

# Initialize the webdriver (assuming you are using Chrome)
driver = webdriver.Chrome()

# Set the base URL
base_url = "https://exhibitors.ces.tech/"

# Navigate to the URL
driver.get("https://exhibitors.ces.tech/8_0/explore/exhibitor-gallery.cfm?featured=false")

# Function to get href from elements with class "bb-0"
def get_hrefs():
    try:
        # Find all elements with class "bb-0"
        elements = driver.find_elements(By.XPATH, '//*[@class="card-Title break-word f2 mb1 mt0"]')

        href_list = []
        for element in elements:
            try:
                element = element.find_element(By.XPATH, './/a[@class="bb-0"]')
                href_list.append(element.get_attribute('href'))
            except:
                pass

        return href_list

    except Exception as e:
        print(f"Error getting hrefs: {e}")
        return []

# Scroll down using ActionChains
def scroll_down():
    try:
        # Create an ActionChains object
        actions = ActionChains(driver)

        # Perform a series of actions, in this case, scroll down
        for i in range(0, 10):
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)

        # Wait for some time (adjust as needed)
        time.sleep(2)

    except Exception as e:
        print(f"Error scrolling down: {e}")

# Function to click on the "Load More Results" button
def click_load_more():
    try:
        # Wait for the "Load More Results" button to be clickable
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="btn-secondary"]'))
        )
        
        # Click the "Load More Results" button
        load_more_button.click()

        # Wait for some time (adjust as needed)
        time.sleep(8)

    except Exception as e:
        print(f"Error clicking 'Load More Results': {e}")

# List to store all hrefs
all_hrefs = []

# Scroll down, click load more, and collect hrefs three times
for _ in range(0,50):
    scroll_down()
    click_load_more()
    scroll_down()

    # Get hrefs from elements with class "bb-0"
    hrefs = get_hrefs()

    # Append the new hrefs to the list
    all_hrefs.extend(hrefs)

# Save hrefs to a CSV file
csv_file_path = "hrefs_data.csv"
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["HREF"])  # Header row

    for href in all_hrefs:
        csv_writer.writerow([href])

# Print the total number of hrefs and file path
print(f"Total number of hrefs: {len(all_hrefs)}")
print(f"Hrefs data saved to: {csv_file_path}")

# Close the webdriver
driver.quit()


