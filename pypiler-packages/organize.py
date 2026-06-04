import os, glob, shutil

dirs = ['certifi', 'charset-normalizer', 'cycler', 'fonttools', 'idna', 'kiwisolver', 'packaging', 'pyparsing', 'blinker']

for d in dirs:
    os.makedirs(d, exist_ok=True)
    
    # move from _dir if exists
    if os.path.exists(d + '_dir'):
        for f in glob.glob(d + '_dir/*.whl'):
            shutil.move(f, os.path.join(d, os.path.basename(f)))
        shutil.rmtree(d + '_dir')

    # move files from root that match
    for f in glob.glob(f'{d.replace("-", "_")}*.whl') + glob.glob(f'{d}*.whl'):
        if os.path.isfile(f):
            shutil.move(f, os.path.join(d, os.path.basename(f)))

if os.path.exists('deps_temp'):
    for f in glob.glob('deps_temp/*.whl'):
        b = os.path.basename(f)
        for d in dirs:
            if b.startswith(d) or b.startswith(d.replace('-', '_')):
                shutil.move(f, os.path.join(d, b))
                break
    shutil.rmtree('deps_temp')
