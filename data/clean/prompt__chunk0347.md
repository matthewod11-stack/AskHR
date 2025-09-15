# files=( "$folder_name"/* )

for file in "${files[@]}"; do new_file_name="draft_$(basename "$file")" mv "$file" "$new_file_name" done

echo "Files renamed successfully." ```

```python import os import shutil