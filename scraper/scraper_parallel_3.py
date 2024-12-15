import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import json
from tqdm.asyncio import tqdm_asyncio  # For the loading meter

# Headers to mimic a browser
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

# Load CSV file and convert phytochemical names and links to a list
df = pd.read_csv("OSADHI_Phyto_ChemName_Links.csv")
phytochem_links = list(zip(df['Phytochemical'], df['Link']))  # Changed to list of tuples


async def fetch(session, url, semaphore):  # Fetch page content with semaphore limit
    async with semaphore:  # Limit concurrency
        try:
            async with session.get(url, headers=HEADERS) as response:
                if response.status == 200:  # Only process successful requests
                    return await response.text()
                else:
                    print(f"Failed to fetch {url} - Status code: {response.status}")
                    return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

async def get_phytochem_website_html(session, phytochem_link, semaphore):
    try:
        html_content = await fetch(session, phytochem_link, semaphore)
        if not html_content:
            return None  # Return None if fetch fails

        # Parse the HTML content
        phytochem_soup = BeautifulSoup(html_content, "html.parser")
        phytochem_info_table_html = phytochem_soup.find('table', class_='table table-striped')

        # Check if the table exists
        if phytochem_info_table_html:
            return phytochem_info_table_html.find_all('td')
        else:
            return None  # No table found
    except Exception as e:
        print(f"Error parsing HTML for {phytochem_link}: {e}")
        return None


def add_per_phytochem_details(phytochem_table):
    if not phytochem_table:  # Check for empty input
        return None

    # Initialize dictionary to store details
    per_phytochem_details_dict = {
        'IUPAC': [],
        'Canonical Smiles': [],
        'Inchi': [],
        'PubChem ID': [],
        'Smiles': []
    }

    # Extract table content
    j = 0
    for i in phytochem_table:
        if j % 2 == 0:  # Keys (e.g., IUPAC)
            dict_key_from_soup = i.text.strip()
        else:  # Values corresponding to keys
            if dict_key_from_soup == 'IUPAC':
                per_phytochem_details_dict['IUPAC'].append(i.text.strip())
            elif dict_key_from_soup == 'Canonical Smiles':
                per_phytochem_details_dict['Canonical Smiles'].append(i.text.strip())
            elif dict_key_from_soup == 'Inchi':
                per_phytochem_details_dict['Inchi'].append(i.text.strip())
            elif dict_key_from_soup == 'PubChem ID':
                per_phytochem_details_dict['PubChem ID'].append(i.text.strip())
            elif dict_key_from_soup == 'Smiles':
                per_phytochem_details_dict['Smiles'].append(i.text.strip())
        j += 1

    # If no data was extracted, return None
    if all(not v for v in per_phytochem_details_dict.values()):
        return None

    return per_phytochem_details_dict

async def process_phytochemical(session, phytochem_name, phytochem_link, semaphore):
    phytochem_html = await get_phytochem_website_html(session, phytochem_link, semaphore)
    if phytochem_html:
        details = add_per_phytochem_details(phytochem_html)
        if details:  # Return only if details are not empty
            return phytochem_name, details
        else:
            print(f"No data found for: {phytochem_name}")
            return phytochem_name, None
    else:
        print(f"Failed to fetch details for: {phytochem_name}")
        return phytochem_name, None


async def process_phytochemicals(phytochem_links, batch_size=40):
    all_phytochem_info_dict = {}
    semaphore = asyncio.Semaphore(10)  # Limit concurrency to 10 requests
    batch_pause = 2  # Pause duration between batches

    async with aiohttp.ClientSession() as session:
        for batch_start in range(0, len(phytochem_links), batch_size):
            batch_links = phytochem_links[batch_start:batch_start + batch_size]

            # Create tasks and use tqdm to display progress
            tasks = [
                process_phytochemical(session, name, link, semaphore) for name, link in batch_links
            ]
            results = await tqdm_asyncio.gather(*tasks, desc=f"Processing Batch {batch_start // batch_size + 1}")

            # Save results into dictionary
            for name, details in results:
                all_phytochem_info_dict[name] = details

            # Save intermediate progress
            with open(f"saves/OSADHI_all_phytochem_details_intermediate.json", "w") as file:
                json.dump(all_phytochem_info_dict, file, indent=4)

            await asyncio.sleep(batch_pause)  # Pause between batches to avoid overloading server

    return all_phytochem_info_dict

async def main():
    results = await process_phytochemicals(phytochem_links)

    # Save the final results
    with open("saves/Phytochemicals_final.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Scraping completed. Results saved!")

if __name__ == "__main__":
    asyncio.run(main())