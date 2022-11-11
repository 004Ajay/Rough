import webbrowser

url = 'https://docs.python.org/'
url2 = 'google'

# Open URL in a new tab, if a browser window is already open.
#webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
path = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
chrome = webbrowser.get(path)
chrome.open_new('chrome://newtab')