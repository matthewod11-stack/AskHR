---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 2247cec0f058a121ebd7e9fdac707349f744d199
title: prompt
---
# Python

import os import shutil

folder_name = input("Enter the folder name: ") prefix = input("Enter the string to prepend to the filename: ") text = toUpperCase(prefix)

if not os.path.isdir(folder_name): print("Folder does not exist.") exit(1)

files = os.listdir(folder_name)

for file in files: new_filename = f"{text}_{file}"
