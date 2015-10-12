import os
import hashlib
from os.path import join

hashes = dict()
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.mp3') :
           thefile = os.path.join(dirname,filename)
           size = os.path.getsize(thefile)
           fhand = open(thefile,'r')
           data = fhand.read()
           fhand.close()
           hash = hashlib.md5(data).hexdigest()
           # print thefile, hash
           if hash in hashes:
               print os.path.getsize(thefile), hashes[hash], thefile
               else:
               hashes[hash] = thefile
           