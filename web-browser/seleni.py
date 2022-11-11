import webbrowser

sites = [
'Drawkit',
'Ouch']

for term in sites:
    url = f'https://www.google.com/search?q={term}'
    webbrowser.open_new_tab(url)