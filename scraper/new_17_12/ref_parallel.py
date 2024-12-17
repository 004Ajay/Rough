import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from tqdm.asyncio import tqdm_asyncio
import json

HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

df = pd.read_csv("OSADHI_Chemo_ChemName_Links.csv")
phytochem_links = list(zip(df['Phytochemical'], df['Link']))

physicochemical_properties = ['Molecular Weight', 'nRot', 'Heavy Atom Molecular Weight', 'nRig', 'Exact Molecular Weight', 'nRing', 'Solubility: LogS', 'nHRing', 'Solubility: LogP', 'No. of Aliphatic Rings', 'Acid Count', 'No. of Aromatic Rings', 'Base Count', 'No. of Aliphatic Carbocycles Rings', 'Atoms Count', 'No. of Aliphatic Hetero Cycles', 'No. of Heavy Atom', 'No. of Aromatic Carbocycles', 'nHetero', 'No. of Aromatic Hetero Cycles', 'nBridge Head', 'No. Saturated Carbocycles', 'No. of Hydrogen atom', 'No. of Saturated Hetero Cycles', 'No. of Carbon atom', 'No. of Saturated Rings', 'No. of Nitrogen atom', 'No. of Arom Atom', 'No. of Oxygen atom', 'No. of Arom Bond', 'nHA', 'APOL', 'nHD', 'BPOL']

medicinal_chemistry_properties = ['QED', 'Synth', 'Natural Product Likeliness', 'NR-PPAR-gamma']

drug_likeliness = ['Lipinski', 'Pfizer', 'GSK', 'Golden Triangle']

absorption = ['Pgp-inh', 'Pgp-sub', 'HIA', 'CACO-2']

distribution = ['MDCK', 'BBB', 'PPB', 'VDSS']

metabolism = ['FU', 'CYP1A2-inh', 'CYP1A2-sub', 'CYP2c19-inh', 'CYP2c19-sub', 'CYP2c9-inh', 'CYP2c9-sub', 'CYP2d6-inh', 'CYP2d6-sub', 'CYP3a4-inh', 'CYP3a4-sub']

excretion = ['CL', 'T12']

toxicity = ['hERG', 'Ames', 'ROA', 'SkinSen', 'Carcinogencity', 'EI', 'Respiratory', 'NR-Aromatase']

antiviral_prediction = ['Antiviral', 'Prediction']

async def fetch(session, url): # fetch page contents
    async with session.get(url, headers=HEADERS) as response:
        return await response.text()

async def get_chemo_website_html(session, phytochem_name, phytochem_link): # fetch chemo data
    try:
        html_content = await fetch(session, phytochem_link)
        phytochem_soup = BeautifulSoup(html_content, "html.parser")
        main_headers = phytochem_soup.find_all("div", class_='card-header')

        if not main_headers: # No main headers like  Physiochemical Properties, Metabolism etc
            print("No Main Headings")
            return None
        elif main_headers: # Main headers present but no content in sub-headers (Molecular Weight, nRot)
            # print("main header - yes")
            sub_headers = phytochem_soup.find_all("td") # getting table of sub-headings and values
            # sub_headers_with_values = check_sub_headers(sub_headers)

            if len(sub_header_html) == 0:
                print("Main headers okay, but no Sub-headers")
                return None # no sub headers
            else:
                # val_dict = add_details_to_dict(sub_header_html)
                return sub_header_html # val_dict
            # print(reply,"\n", sub_headers_with_values)
            # return sub_headers_with_values
    except Exception as e:
        print(f"Error parsing HTML for {phytochem_name}: {e}")
        return None

def add_details_to_dict(sub_header_bs4_html):        
    chemo_items_dict = {
        'Physiochemical Properties' : {'Molecular Weight':'', 'nRot':'', 'Heavy Atom Molecular Weight':'', 'nRig':'', 'Exact Molecular Weight':'', 'nRing':'', 'Solubility: LogS':'', 'nHRing':'', 'Solubility: LogP':'', 'No. of Aliphatic Rings':'', 'Acid Count':'', 'No. of Aromatic Rings':'', 'Base Count':'', 'No. of Aliphatic Carbocycles Rings':'', 'Atoms Count':'', 'No. of Aliphatic Hetero Cycles':'', 'No. of Heavy Atom':'', 'No. of Aromatic Carbocycles':'', 'nHetero':'', 'No. of Aromatic Hetero Cycles':'', 'nBridge Head':'', 'No. Saturated Carbocycles':'', 'No. of Hydrogen atom':'', 'No. of Saturated Hetero Cycles':'', 'No. of Carbon atom':'', 'No. of Saturated Rings':'', 'No. of Nitrogen atom':'', 'No. of Arom Atom':'', 'No. of Oxygen atom':'', 'No. of Arom Bond':'', 'nHA':'', 'APOL':'', 'nHD':'', 'BPOL':''},
        'Medicinal Chemistry Properties' : {'QED':'', 'Synth':'', 'Natural Product Likeliness':'', 'NR-PPAR-gamma':''},
        'Drug Likeliness' : {'Lipinski':'', 'Pfizer':'', 'GSK':'', 'Golden Triangle':''},
        'Absorption' : {'Pgp-inh':'', 'Pgp-sub':'', 'HIA':'', 'CACO-2':''},
        'Distribution' : {'MDCK':'', 'BBB':'', 'PPB':'', 'VDSS':''},
        'Metabolism' : {'FU':'', 'CYP1A2-inh':'', 'CYP1A2-sub':'', 'CYP2c19-inh':'', 'CYP2c19-sub':'', 'CYP2c9-inh':'', 'CYP2c9-sub':'', 'CYP2d6-inh':'', 'CYP2d6-sub':'', 'CYP3a4-inh':'', 'CYP3a4-sub':''},
        'Excretion' : {'CL':'', 'T12':''},
        'Toxicity' : {'hERG':'', 'Ames':'', 'ROA':'', 'SkinSen':'', 'Carcinogencity':'', 'EI':'', 'Respiratory':'', 'NR-Aromatase':''},
        'Antiviral Prediction' : {'Antiviral':'', 'Prediction':''}
        }
    k=0
    for i in sub_header_bs4_html:
        if k % 2 == 0: # heading
            heading = i.text.strip()
        else:          # values
            if heading in physicochemical_properties:
                chemo_items_dict['Physiochemical Properties'][heading] = str(i.text.strip())
            
            elif heading in medicinal_chemistry_properties:
                chemo_items_dict['Medicinal Chemistry Properties'][heading] = str(i.text.strip())
            
            elif heading in drug_likeliness:
                chemo_items_dict['Drug Likeliness'][heading] = str(i.text.strip())
            
            elif heading in absorption:
                chemo_items_dict['Absorption'][heading] = str(i.text.strip())
            
            elif heading in distribution:
                chemo_items_dict['Distribution'][heading] = str(i.text.strip())
            
            elif heading in metabolism:
                chemo_items_dict['Metabolism'][heading] = str(i.text.strip())
            
            elif heading in excretion:
                chemo_items_dict['Excretion'][heading] = str(i.text.strip())
            
            elif heading in toxicity:
                chemo_items_dict['Toxicity'][heading] = str(i.text.strip())
            
            elif heading in antiviral_prediction:
                chemo_items_dict['Antiviral Prediction'][heading] = str(i.text.strip())
        k+=1
    return chemo_items_dict   
        
async def process_phytochemical(session, phytochem_name, phytochem_link): # process single phytochemical
    phytochem_html = await get_chemo_website_html(session, phytochem_name, phytochem_link)
    
    if phytochem_html:
        return phytochem_name, add_details_to_dict(phytochem_html)
    else:
        return phytochem_name, None

async def process_phytochemicals(phytochem_links, batch_size=40): # process all phytochemicals
    all_phytochem_info_dict = {}
    # semaphore = asyncio.Semaphore(10) # limit concurrency to 10 requests
    batch_pause = 2 

    async with aiohttp.ClientSession() as session:
        for batch_start in range(0, len(phytochem_links), batch_size):
            batch_links = phytochem_links[batch_start:batch_start+batch_size]
            tasks = [process_phytochemical(session, name, link) for name, link in batch_links] # changed batch_links.items() to batch_links 
            results = await tqdm_asyncio.gather(*tasks, desc=f"Processing Batch {batch_start // batch_size + 1}")
            for name, details in results:
                all_phytochem_info_dict[name] = details

            with open(f"saves/OSADHI_chemo_details_intermediate.json", "w") as file: 
                json.dump(all_phytochem_info_dict, file, indent=4) # intermediate saving to json file, if the process breakes in between 
            await asyncio.sleep(batch_pause) # pause for server
    return all_phytochem_info_dict        

async def main():
    results = await process_phytochemicals(phytochem_links)
    with open("saves/Chemoinformatics_final.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    asyncio.run(main())