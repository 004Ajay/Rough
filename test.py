import webbrowser

url = 'edge://newtab'

chrome_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s'

webbrowser.get(chrome_path).open(url)