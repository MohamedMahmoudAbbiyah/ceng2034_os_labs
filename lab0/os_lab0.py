import os
import time
from datetime import datetime

os.chdir(os.environ.get('HOME'))
os.system('mkdir os_lab_0')
os.chdir('os_lab_0')
os.system("touch 1.txt 2.txt 3.py")

for i in os.listdir():
    if os.path.isfile(i):
        print("last modified in: ", time.ctime(os.path.getmtime(i)), i)

for j in os.listdir():
    if os.path.isfile(j) and j.endswith(".txt"):
        print(j)