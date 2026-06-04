import urllib.request, re
try:
    html = urllib.request.urlopen('https://chaquo.com/pypi-13.1/markupsafe/').read().decode()
    links = re.findall(r'href=[\'\"]([^\'\"]+cp311[^\'\"]+)[\'\"]', html)
    for link in links:
        print('  ' + link)
except Exception as e:
    print(f'Error: {e}')
