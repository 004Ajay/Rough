from playwright.sync_api import sync_playwright
import pandas as pd

def extract_plant_info(links):
    # A list to store the extracted data
    extracted_data = []

    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)  # Headless mode for speed
        page = browser.new_page()

        for link in links:
            page.goto(link, timeout=60000)  # Visit each link with timeout

            # Extract required information using selectors
            try:
                plant_name = page.locator("h5").nth(0).text_content().strip()
                kingdom = page.locator("text=Kingdom:").locator("..").text_content().split(":")[1].strip()
                family = page.locator("text=Family:").locator("..").text_content().split(":")[1].strip()
                group = page.locator("text=Group:").locator("..").text_content().split(":")[1].strip()
                synonyms = page.locator("text=Synonymous names:").locator("..").text_content().split(":")[1].strip()
                iucn_category = page.locator("text=IUCN Red List category:").locator("..").text_content().split(":")[1].strip()

                # Append the extracted data as a dictionary
                extracted_data.append({
                    "Plant Name": plant_name,
                    "Kingdom": kingdom,
                    "Family": family,
                    "Group": group,
                    "Synonymous Names": synonyms,
                    "IUCN Red List Category": iucn_category,
                })

                print(f"Successfully extracted: {plant_name}")
            except Exception as e:
                msg = link.split('\\')[-1]
                print(f"Failed to extract data from {msg}: {e}")

        browser.close()

    # Save data to CSV
    df = pd.DataFrame(extracted_data)
    df.to_csv("extracted_plant_info.csv", index=False)
    print("Data saved to 'extracted_plant_info.csv'")

# List of links to scrape
links = [
    "https://cb.imsc.res.in/imppat/phytochemical/Abies%20balsamea",  # Replace with your actual links,
]

extract_plant_info(links)
