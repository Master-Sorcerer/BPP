import os
import re
from pathlib import Path

#checking the file exist
path = Path('/var/log/apache2/access.log')
print (path.is_file())

#Gather the file locations
filenames = os.system('find /var/log/apache2  -name \*.log')
s= str(filenames)
splitted = s.split("/")
print(filenames)
print(type(filenames))
print(type(splitted))
print(splitted)

