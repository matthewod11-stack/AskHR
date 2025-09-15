# files=( "$folder_name"/* )

for file in "${files[@]}"; do new_file_name="draft_$(basename "$file")" mv "$file" "$new_file_name" done

echo "Files renamed successfully." ```

This Bash script pe(cid:455)orms the following tasks:

- 1. **User Input**:

- It prompts the user to enter a folder name using the `echo` and `read`

commands. The entered folder name is stored in the `folder_name` variable.

- 2. **Folder Existence Check**:

- It checks if the folder with the speci(cid:450)ed name exists using the `[ ! -d “$folder_name” ]` condition. If the folder does not exist, it displays an error message (“Folder does not exist.”) and exits the script with an exit code of 1.