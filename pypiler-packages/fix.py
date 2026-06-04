import os, shutil
for f in ['certifi', 'charset-normalizer', 'cycler', 'fonttools', 'idna', 'kiwisolver', 'packaging', 'pyparsing']:
    if os.path.isfile(f):
        os.remove(f)
    if os.path.isdir(f + '_dir'):
        os.rename(f + '_dir', f)

if os.path.isdir('deps_temp'):
    if not os.path.isdir('kiwisolver'):
        os.mkdir('kiwisolver')
    for whl in os.listdir('deps_temp'):
        shutil.move(os.path.join('deps_temp', whl), os.path.join('kiwisolver', whl))
    os.rmdir('deps_temp')
