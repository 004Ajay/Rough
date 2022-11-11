from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('chrome://newtab')

print("Enter a keyword to search on wikipedia: ", end='')
keyword = input()

elem = browser.find_element_by_id('realbox')  # Find the search box
elem.send_keys(keyword + Keys.RETURN)

# do something with the opened page

browser.quit()