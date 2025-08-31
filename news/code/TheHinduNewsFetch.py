import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

# ========== Configuration ==========
URL = "https://www.thehindu.com/latest-news/"
EXCEL_FILE_NAME = "latest_news.xlsx"
SAVE_LOCATION = "C:\\Users\\ajayt\\OneDrive\\Desktop\\mithun"

# ========== Logging Setup ==========
LOG_FILE = "C:\\Users\\ajayt\\OneDrive\\Desktop\\mithun\\code\\news_scraper.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

EXCEL_FILE = os.path.join(SAVE_LOCATION, EXCEL_FILE_NAME)

# ========== Scraping ==========
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    logging.info("Successfully fetched the page: %s", URL)
except requests.RequestException as e:
    logging.error("Network error while fetching URL: %s", e)
    raise
except Exception as e:
    logging.error("Unexpected error while fetching page: %s", e)
    raise

news_data = []
for h3 in soup.find_all("h3", class_="title"):
    # will give:
    #   <h3 class="title">
    #       <a href="https://www.thehindu.com/opinion/open-page/in-search-of-an-identity/article69985615.ece">
    #       In search of an identity
    #       </a>
    #   </h3>
    a_tag = h3.find("a") # getting <a>...</a>
    if a_tag:
        headline = a_tag.get_text(strip=True)
        link = a_tag["href"]
        news_data.append({
            "Headline": headline,
            "Link": link,
            "Scraped_At": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

logging.info("Extracted %d news articles", len(news_data))

df = pd.DataFrame(news_data)

# ========== Saving ==========
try:
    if os.path.exists(EXCEL_FILE):
        existing_df = pd.read_excel(EXCEL_FILE)
        final_df = pd.concat([existing_df, df], ignore_index=True)
        logging.info("Appended new data to existing Excel file.")
    else:
        final_df = df
        logging.info("Created new Excel file.")
except Exception as e:
    logging.error("Error while reading/merging Excel file: %s", e)
    final_df = df

before_dedup = len(final_df)
final_df = final_df.drop_duplicates(subset=["Headline", "Link"], keep="first") # drop duplicates
after_dedup = len(final_df)
logging.info("Dropped %d duplicate rows", before_dedup - after_dedup)

try:
    writer = pd.ExcelWriter(EXCEL_FILE, engine='xlsxwriter')

    final_df.to_excel(writer, sheet_name="Sheet1", index=False)

    worksheet = writer.sheets['Sheet1']

    url_format = writer.book.add_format({"font_color": "blue", "underline": 1})

    for row_num in range(1, len(df) + 1):
        worksheet.write_url(row_num, 1, df.at[row_num - 1, "Link"], url_format) # write_url() from xlsxwriter to make it clickable
        
    writer.close()

    logging.info("Hyperlinks styled and saved successfully.")

except Exception as e:
    logging.error("Error saving Excel file: %s", e)