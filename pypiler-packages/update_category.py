import json

main_libs = {'numpy', 'pandas', 'matplotlib', 'flask', 'requests', 'pillow', 'openpyxl'}

with open('packages.json', 'r') as f:
    data = json.load(f)

for p in data['packages']:
    if p['name'] in main_libs:
        p['category'] = 'main'
    else:
        p['category'] = 'dependency'

with open('packages.json', 'w') as f:
    json.dump(data, f, indent=2)
