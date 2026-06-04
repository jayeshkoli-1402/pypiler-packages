import os, urllib.request, subprocess, shutil
packages = ['cycler', 'fonttools', 'kiwisolver', 'packaging', 'pyparsing', 'charset-normalizer', 'idna', 'certifi', 'blinker']

os.makedirs('deps_temp', exist_ok=True)
os.chdir('deps_temp')
subprocess.run(['python', '-m', 'pip', 'download', 'charset-normalizer', 'fonttools', '--platform', 'any', '--only-binary', ':all:', '--no-deps'])
subprocess.run(['python', '-m', 'pip', 'download', 'cycler', 'packaging', 'pyparsing', 'idna', 'certifi', 'blinker', '--no-deps'])
os.chdir('..')

# Chaquopy kiwisolver
urls = [
    "https://chaquo.com/pypi-13.1/kiwisolver/kiwisolver-1.4.5-0-cp311-cp311-android_21_arm64_v8a.whl",
    "https://chaquo.com/pypi-13.1/kiwisolver/kiwisolver-1.4.5-0-cp311-cp311-android_21_armeabi_v7a.whl",
    "https://chaquo.com/pypi-13.1/kiwisolver/kiwisolver-1.4.5-0-cp311-cp311-android_21_x86_64.whl"
]
for u in urls:
    urllib.request.urlretrieve(u, os.path.join('deps_temp', os.path.basename(u)))

import glob
for w in glob.glob('deps_temp/*.whl'):
    b = os.path.basename(w)
    target = b.split('-')[0].replace('_', '-')
    if target == 'charset': target = 'charset-normalizer'
    os.makedirs(target, exist_ok=True)
    shutil.move(w, os.path.join(target, b))

shutil.rmtree('deps_temp')
