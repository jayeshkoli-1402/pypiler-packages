import json

with open('packages.json', 'r') as f:
    data = json.load(f)

new_packages = [
    {
      "name": "cycler",
      "display_name": "cycler",
      "version": "0.12.1",
      "type": "pure",
      "size_mb": 0.01,
      "description": "Composable style cycles",
      "abis": { "any": "cycler/cycler-0.12.1-py3-none-any.whl" }
    },
    {
      "name": "fonttools",
      "display_name": "fonttools",
      "version": "4.63.0",
      "type": "pure",
      "size_mb": 1.1,
      "description": "Tools to manipulate font files",
      "abis": { "any": "fonttools/fonttools-4.63.0-py3-none-any.whl" }
    },
    {
      "name": "kiwisolver",
      "display_name": "kiwisolver",
      "version": "1.4.5",
      "type": "native",
      "size_mb": 0.1,
      "description": "A fast implementation of the Cassowary constraint solver",
      "abis": {
        "arm64-v8a": "kiwisolver/kiwisolver-1.4.5-0-cp311-cp311-android_21_arm64_v8a.whl",
        "armeabi-v7a": "kiwisolver/kiwisolver-1.4.5-0-cp311-cp311-android_21_armeabi_v7a.whl",
        "x86_64": "kiwisolver/kiwisolver-1.4.5-0-cp311-cp311-android_21_x86_64.whl"
      }
    },
    {
      "name": "packaging",
      "display_name": "packaging",
      "version": "26.2",
      "type": "pure",
      "size_mb": 0.1,
      "description": "Core utilities for Python packages",
      "abis": { "any": "packaging/packaging-26.2-py3-none-any.whl" }
    },
    {
      "name": "pyparsing",
      "display_name": "pyparsing",
      "version": "3.3.2",
      "type": "pure",
      "size_mb": 0.1,
      "description": "Python parsing module",
      "abis": { "any": "pyparsing/pyparsing-3.3.2-py3-none-any.whl" }
    },
    {
      "name": "charset-normalizer",
      "display_name": "charset-normalizer",
      "version": "3.4.7",
      "type": "pure",
      "size_mb": 0.1,
      "description": "The Real First Universal Charset Detector",
      "abis": { "any": "charset-normalizer/charset_normalizer-3.4.7-py3-none-any.whl" }
    },
    {
      "name": "idna",
      "display_name": "idna",
      "version": "3.18",
      "type": "pure",
      "size_mb": 0.1,
      "description": "Internationalized Domain Names in Applications",
      "abis": { "any": "idna/idna-3.18-py3-none-any.whl" }
    },
    {
      "name": "certifi",
      "display_name": "certifi",
      "version": "2026.5.20",
      "type": "pure",
      "size_mb": 0.1,
      "description": "Python package for providing Mozilla's CA Bundle",
      "abis": { "any": "certifi/certifi-2026.5.20-py3-none-any.whl" }
    },
    {
      "name": "blinker",
      "display_name": "blinker",
      "version": "1.9.0",
      "type": "pure",
      "size_mb": 0.01,
      "description": "Fast, simple object-to-object and broadcast signaling",
      "abis": { "any": "blinker/blinker-1.9.0-py3-none-any.whl" }
    }
]

for p in new_packages:
    if not any(x['name'] == p['name'] for x in data['packages']):
        data['packages'].append(p)

with open('packages.json', 'w') as f:
    json.dump(data, f, indent=2)
