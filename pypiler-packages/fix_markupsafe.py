import os, urllib.request, json
urls = [
    "https://chaquo.com/pypi-13.1/markupsafe/markupsafe-3.0.3-0-cp311-cp311-android_24_arm64_v8a.whl",
    "https://chaquo.com/pypi-13.1/markupsafe/markupsafe-3.0.3-0-cp311-cp311-android_24_armeabi_v7a.whl"
]

os.makedirs('MarkupSafe', exist_ok=True)
for u in urls:
    urllib.request.urlretrieve(u, os.path.join('MarkupSafe', os.path.basename(u)))
