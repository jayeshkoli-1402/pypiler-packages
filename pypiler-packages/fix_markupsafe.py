import os, urllib.request, json
urls = [
    "https://chaquo.com/pypi-13.1/MarkupSafe/markupsafe-3.0.3-0-cp311-cp311-android_24_arm64_v8a.whl",
    "https://chaquo.com/pypi-13.1/MarkupSafe/markupsafe-3.0.3-0-cp311-cp311-android_24_armeabi_v7a.whl"
]

os.makedirs('MarkupSafe', exist_ok=True)
for u in urls:
    try:
        urllib.request.urlretrieve(u, os.path.join('MarkupSafe', os.path.basename(u)))
        print("Downloaded", u)
    except Exception as e:
        print("Error downloading", u, e)

with open('packages.json', 'r') as f:
    data = json.load(f)

for p in data['packages']:
    if p['name'] == 'markupsafe':
        p['abis']['arm64-v8a'] = 'MarkupSafe/markupsafe-3.0.3-0-cp311-cp311-android_24_arm64_v8a.whl'
        p['abis']['armeabi-v7a'] = 'MarkupSafe/markupsafe-3.0.3-0-cp311-cp311-android_24_armeabi_v7a.whl'
        break

with open('packages.json', 'w') as f:
    json.dump(data, f, indent=2)
