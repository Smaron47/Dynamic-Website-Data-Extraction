# Dynamic-Website-Data-Extraction


Project Title: Selenium Web Scraper for CES Exhibitor Gallery
Developed by: Smaron Biswas
License: MIT
Year: 2024

--------------------------------------------------------------------
OVERVIEW
--------------------------------------------------------------------
This project uses Python and Selenium WebDriver to automate the process of scraping exhibitor profile links 
from the CES (Consumer Electronics Show) Exhibitor Gallery. It mimics human-like scrolling, interacts with 
dynamic "Load More Results" buttons, and collects clickable URLs (`hrefs`) of all listed exhibitors.

The scraped links are saved to a CSV file (`hrefs_data.csv`) for further processing, analysis, or automation.

SEO Keywords:
- Selenium Web Scraping
- CES Exhibitor Gallery Scraper
- Python Automation Script
- Dynamic Website Data Extraction
- Selenium Click and Scroll Automation
- Export to CSV using Python

--------------------------------------------------------------------
FEATURES
--------------------------------------------------------------------
✅ **Automated Page Scrolling**  
✅ **Clicks on “Load More Results” Button Automatically**  
✅ **Extracts Hyperlinks Dynamically from Exhibitor Cards**  
✅ **Saves All Hrefs to a Clean CSV File**  
✅ **Handles Loading Delays Gracefully with WebDriverWait**  
✅ **Written in Pure Python, Uses Selenium Only**  
✅ **Customizable Loop Count and Scroll Depth**  
✅ **Structured and Readable Code with Logging**

--------------------------------------------------------------------
TECH STACK
--------------------------------------------------------------------
- Python 3.x
- Selenium
- Chrome WebDriver (or other supported drivers)
- CSV Module
- WebDriverWait, ActionChains, Expected Conditions

--------------------------------------------------------------------
USE CASES
--------------------------------------------------------------------
- **Lead Generation**: Collect URLs for sales and marketing outreach.
- **Event Analysis**: Scrape exhibitor data for CES 2024/2025 reports.
- **Data Aggregation**: Gather URLs for further scraping or indexing.
- **Automation Learning**: Educational example of handling dynamic websites.

--------------------------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------------------------
Your folder after running the script will look like this:

  /ces-scraper/
  ├── scraper.py              # Python script with Selenium code
  ├── hrefs_data.csv          # Output CSV with scraped exhibitor links
  └── README.md or document.txt # This documentation file

--------------------------------------------------------------------
CODE BREAKDOWN & LOGIC
--------------------------------------------------------------------

1. **Initialization**
   ```python
   driver = webdriver.Chrome()
   driver.get("https://exhibitors.ces.tech/8_0/explore/exhibitor-gallery.cfm?featured=false")
Launches Chrome browser.

Navigates to the CES Exhibitor Gallery page.

Scrolling Function


def scroll_down():
    ...
Simulates pressing PAGE_DOWN keys multiple times to trigger content loading.

Mimics user interaction to bypass lazy-loading mechanisms.

Click "Load More Results" Button

def click_load_more():
    ...
Waits until the “Load More Results” button becomes clickable.

Clicks it and waits for new content to load.

Repeats this process for each page scroll cycle.

Extracting Exhibitor Hrefs


def get_hrefs():
    ...
Looks for HTML elements with the title class and then extracts anchor tags (<a>).

Collects all exhibitor detail page URLs.

Main Loop (Scraping Logic)

for _ in range(0, 50):
    scroll_down()
    click_load_more()
    hrefs = get_hrefs()
    all_hrefs.extend(hrefs)
Repeats scroll + click + extract logic for 50 cycles.

Accumulates unique exhibitor links into all_hrefs.

Writing to CSV


with open("hrefs_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    ...
Saves the final list of URLs into a structured CSV file.


driver.quit()
Closes the browser window and ends the session.

INSTALLATION & SETUP
Install Dependencies


pip install selenium
Download WebDriver

For Chrome: https://sites.google.com/chromium.org/driver/

Place it in a known path or set it via environment variable.

Edit Script

Update this line with your correct WebDriver path:


webdriver_path = "path/to/your/webdriver"
Run the Script


python scraper.py
TROUBLESHOOTING
❌ If the script crashes:

Confirm your WebDriver version matches your Chrome version.

Make sure the website structure hasn't changed (check XPaths).

Increase WebDriverWait timeout if page loads slowly.

✅ You can also add driver.implicitly_wait(5) to wait globally.

CUSTOMIZATION IDEAS
Add user-agent spoofing for stealth.

Save additional data (e.g., company names, categories).

Implement retry logic for network interruptions.

Scrape other pages by modifying the base URL.

CONCLUSION
This Selenium scraper demonstrates dynamic content extraction from modern web applications using
scroll events, button clicks, and precise XPath targeting. It’s ideal for scraping exhibitor data
or other paginated content that requires interaction beyond static requests.

Fully customizable and adaptable for other sites with "Load More" features or infinite scroll logic.
