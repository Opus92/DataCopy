#
# Copy data files from one protected folder to another shared folder.
# Will be run automatically once per week.
#

import os
import shutil

# Set source and working directory
src = r'C:\Users\kylenehall.FOREST\OneDrive - University of South Florida\Reporting-IS-IT WIP\Data'
dst = r'C:\Users\kylenehall.FOREST\OneDrive - University of South Florida\Reporting-IS-IT\Data'
os.chdir(dst)

# Loop through files in the shared directory and delete all the old files.
for dirName, subdirList, fileList in os.walk(dst):
    for filename in fileList:
        os.remove(filename)
        print(filename, 'was deleted from', dst)

input('Press any key to continue.\n\n')

# Loop through files in the private directory and copy the files to the shared directory.
for dirName, subdirList, fileList in os.walk(src):
    for filename in fileList:
        fileSrc = src + '\\' + filename
        fileDst = dst + '\\' + filename
        
        shutil.copy2(fileSrc, fileDst)
        print(filename, 'was copied to', src)

input('Press any key to continue.')
