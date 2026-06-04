import os, glob, shutil
dirs = ['certifi', 'charset-normalizer', 'cycler', 'fonttools', 'idna', 'kiwisolver', 'packaging', 'pyparsing', 'blinker']
for d in dirs:
    os.makedirs(d, exist_ok=True)

# collect all wheels everywhere in root and deps_temp and move them correctly
all_wheels = glob.glob('*.whl') + glob.glob('*_dir/*.whl') + glob.glob('deps_temp/*.whl')
for d in dirs:
    for w in glob.glob(f'{d}/*.whl'):
        all_wheels.append(w)

for w in set(all_wheels):
    b = os.path.basename(w)
    target_dir = None
    if 'certifi' in b: target_dir = 'certifi'
    elif 'charset' in b: target_dir = 'charset-normalizer'
    elif 'cycler' in b: target_dir = 'cycler'
    elif 'fonttools' in b: target_dir = 'fonttools'
    elif 'idna' in b: target_dir = 'idna'
    elif 'kiwisolver' in b: target_dir = 'kiwisolver'
    elif 'packaging' in b: target_dir = 'packaging'
    elif 'pyparsing' in b: target_dir = 'pyparsing'
    elif 'blinker' in b: target_dir = 'blinker'
    
    if target_dir:
        dest = os.path.join(target_dir, b)
        if os.path.abspath(w) != os.path.abspath(dest):
            shutil.move(w, dest)
