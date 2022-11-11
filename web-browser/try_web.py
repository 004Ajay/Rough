import webbrowser

sites = [
'Drawkit',
'Ouch',
'Illustratious',
'Free Web illustrations',
'Humaaans',
'Absurd illustrations',
'Blush',
'StockSnap',
'Landing Stock',
'Nappy',
'Photo Creator',
'StockSnap',
'Reshot',
'Gratisography',
'Mckups',
'Placeit',
'Smartmockups',
'Mockuuups',
'PSD Repo',
'Mockup',
'Mockupmark',
"Mockup's Design",
'Pixeden',
'Noun Project',
'lonicons',
'Icons',
'Simple Icons',
'Dryicons',
'Mr.lcons',
'Pixeden',
'Iconfinder',
'Caption Icon',
]

for term in sites:
    url = f'https://www.google.com/search?q={term}'
    webbrowser.open_new_tab(url)