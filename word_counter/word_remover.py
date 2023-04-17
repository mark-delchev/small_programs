import re

# Open the original file for reading
with open("data.txt", "r") as f:
    text = f.read()

# Edit the text
text = re.sub(r"\b(и)\b", "", text)

# Open a new file for writing
with open("edited_data.txt", "w") as f:
    f.write(text)
