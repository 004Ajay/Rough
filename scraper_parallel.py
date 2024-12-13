import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from tqdm.asyncio import tqdm
import json


HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

async def fetch(session, url): # fetch page contents
    async with session.get(url, header=HEADERS) as response:
        return await response.text()

async def get_phytochem_website_html(session, phytochem_link): # fetch phytochem data
    try:
        html_content = await fetch(session, phytochem_link)
        soup = BeautifulSoup(html_content, "html.parser")
        phytochem_info_table_html = phytochem_soup.find('table', class_='table table-striped').find_all('td')
        return phytochem_info_table_html
    except AttributeError:
        return None

def add_per_phytochem_details(phytochem_table):
    if not phytochem_table:
        return None
        
    per_phytochem_details_dict = {
            'IUPAC':[],
            'Canonical Smiles':[],
            'Inchi':[],
            'PubChem ID':[],
            'Smiles':[]
            }
    j = 0
    for i in phytochem_table:
        if j % 2 == 0:
            dict_key_from_soup = i.text.strip()
        else:    
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
        j+=1

    return per_phytochem_details_dict    
        
async def process_phytochemical(session, phytochem_name, phytochem_link): # process single phytochemical
    phytochem_html = await get_phytochem_website_html(session, phytochem_link)
    
    if phytochem_html:
        return phytochem_name, add_per_phytochem_details(phytochem_html)
    else:
        return phytochem_name, None

async def process_phytochemicals(phytochem_links, batch_size=40): # process all phytochemicals
    all_phytochem_info_dict = {}
    semaphore = asyncio.Semaphore(10) # limit concurrency to 10 requests
    batch_pause = 2

    async with aiohttp.ClientSession() as session:
        for batch_start in range(0, len(phytochem_links), batch_size):
            batch_links = phytochem_links[batch_start:batch_start+batch_size]
            tasks = [process_phytochemical(session, name, link) for name, link in batch_links] # change batch_links.items() to batch_links 
            results = await asyncio.gather(*tasks)
            for name, details in results:
                all_phytochem_info_dict[name] = details

            with open(f"saves/OSADHI_all_phytochem_details_after_40_{big_pause}.json", "w") as file: 
                json.dump(all_phytochem_info_dict, file, indent=4) # intermediate saving to json file, if the process breakes in between 
            await asyncio.sleep(batch_pause) # pause for server
    return all_phytochem_info_dict        


df = pd.read_csv("OSADHI_Phyto_ChemName_Links.csv")
phytochem_links = list(zip(df['Phytochemical'], df['Link'])) # change dict to list
# print(len(df['Phytochemical']))
# df.head(3)

async def main():
    results = await process_phytochemicals(phytochem_links)
    with open("saves/Phytochemicals_final.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
