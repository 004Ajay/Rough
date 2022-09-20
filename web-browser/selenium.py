from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe', chrome_options=options)
driver.get("https://www.google.co.in")