import os
import time
namefile = open("external.txt", encoding="UTF-8")
names = namefile.readlines()
for name in names:
    print(name)
    os.system("sortgs.py "+name.replace(" ", "+").replace("\xa0", ""))
    time.sleep(4)