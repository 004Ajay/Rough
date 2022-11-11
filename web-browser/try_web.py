import webbrowser

sites1 = [
'Reshot',
'Gratisography',
'Mckups',
'Placeit',
'Smartmockups',
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

sites2 = [
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
'Mockuuups',
'PSD Repo',
'Mockup',
'Mockupmark',
]

for term in sites2:
    url = f'https://www.google.com/search?q={term}'
    webbrowser.open_new_tab(url)