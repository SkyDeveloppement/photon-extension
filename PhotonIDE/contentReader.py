# Photon IDE developed by SkyDevelopment
import json

# Dictionary for storing the content of code files
CodeFile = {}

# Open the photon-pack.json file
with open("./photon-pack.json", "r") as pack:
    # Load JSON data
    data = json.load(pack)
    # Access the "code" attribute of JSON
    code_data = data.get("code", {})
    # Access the "file" attribute of "code"
    files = code_data.get("file", [])
    
    # Read the content of each specified file
    for file_name in files:
        with open(file_name) as reader:
            # Check if the key exists in CodeFile, otherwise create an empty list
            if file_name not in CodeFile:
                CodeFile[file_name] = []
            # Read each line of the file and add it to the corresponding list
            for line in reader:
                CodeFile[file_name].append(line)
