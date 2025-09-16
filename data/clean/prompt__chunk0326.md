---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 22987f9bd16eec60e4ee193ddb14a0f789ccc86c
title: prompt
---
# ``` #!/bin/bash

echo "Enter the folder name: " read folder_name

if [ ! -d "$folder_name" ]; then echo "Folder does not exist." exit 1 fi
