# ``` #!/bin/bash

echo "Enter the folder name: " read folder_name

if [ ! -d "$folder_name" ]; then echo "Folder does not exist." exit 1 fi