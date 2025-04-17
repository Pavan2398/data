import json

# Load missing ECG IDs
with open("missing_files.txt", "r") as file:
    missing_ids = set(int(line.strip()) for line in file)

# Load the JSON data
with open("test.json", "r") as file:
    data = json.load(file)

# Filter out templates with ecg_id in missing_ids
filtered_data = [
    template for template in data
    if not any(ecg_id in missing_ids for ecg_id in template.get("ecg_id", []))
]

# Overwrite the original file with filtered data
with open("test.json", "w") as file:
    json.dump(filtered_data, file, indent=4)