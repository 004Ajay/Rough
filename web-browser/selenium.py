from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir= C:\Program Files\Google\Chrome\Application\chrome.exe --profile-directory=Default")
driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe', chrome_options=options)
driver.get("https://www.google.co.in")