import requests

# Define the URL of the raw file on GitHub
github_url = "https://raw.githubusercontent.com/leoprimesmatrix/Mixed-Words-Code/main/mixed_words.py?token=GHSAT0AAAAAAB7Y4RKFC62M362OOISRBZR4ZALOK6Q"

# Download the contents of the file
response = requests.get(github_url)
file_contents = response.text

# Execute the file
exec(file_contents)
