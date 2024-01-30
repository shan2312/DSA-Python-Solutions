import shutil
import glob2 as glob
with open('merged_array.py', 'wb') as outfile:
    for filename in glob.glob('*.py'):
        if filename == 'merged_array.py':
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
