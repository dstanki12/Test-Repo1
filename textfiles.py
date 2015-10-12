import os
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.mp3') :
          thefile = os.path.join(dirname,filename)
          print os.path.getsize(thefile), thefile