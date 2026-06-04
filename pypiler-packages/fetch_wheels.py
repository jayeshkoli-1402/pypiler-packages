import urllib.request, re

def fetch(pkg):
    try:
        html = urllib.request.urlopen(f'https://chaquo.com/pypi-13.1/{pkg}/').read().decode()
        links = re.findall(r'href=[\'\"]([^\'\"]+cp311[^\'\"]+)[\'\"]', html)
        if links:
            print(pkg)
            for link in links:
                print('  ' + link)
    except Exception as e:
        print(f'{pkg} not found or error: {e}')

for p in ['kiwisolver', 'fonttools', 'charset-normalizer', 'charset_normalizer']:
    fetch(p)
