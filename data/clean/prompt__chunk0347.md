---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 983824f640fa4ccdbe2476594a4c80f6de79d747
title: prompt
---
# ```bash #!/bin/bash

echo "Enter the folder name: " read folder_name

if [ ! -d "$folder_name" ]; then echo "Folder does not exist." exit 1 fi
