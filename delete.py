import os
import shutil

first = os.path.abspath(os.path.dirname(__file__))
first = ''
second = "python1\\junk2.txt"
path = os.path.join(first, second)
print(f"path: {path}")
try:
    os.remove(path)
except Exception as error:
    print(error)
finally:
    try:
        os.rmdir('python1')
    except Exception as error:
        print(error)
        shutil.rmtree('python1')
