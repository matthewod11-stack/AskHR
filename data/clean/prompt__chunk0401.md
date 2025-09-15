# Print a success message print("Files renamed successfully.") ```

Additionally, there are a few other improvements that can be made to the code:

- 1. The (cid:450)le extension of the new (cid:450)lenames is not kept. It’s be(cid:459)er to extract the extension from the original (cid:450)lename and append it to the new (cid:450)lename.

- 2. The code assumes that there are no spaces in the folder name. However, it is a good practice to handle spaces gracefully by replacing them with underscores or hyphens.

- 3. Using the `f` string syntax for string interpolation is more readable and