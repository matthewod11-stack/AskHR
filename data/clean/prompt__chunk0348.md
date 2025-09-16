---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 1942e7b1c04428dc843a961fde9e25b0aa9030c2
title: prompt
---
# files=( "$folder_name"/* )

for file in "${files[@]}"; do new_file_name="draft_$(basename "$file")" mv "$file" "$new_file_name" done

echo "Files renamed successfully." ```

```python import os import shutil
