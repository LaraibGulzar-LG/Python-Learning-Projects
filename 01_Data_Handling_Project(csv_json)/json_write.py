import json

new_data = {"status": "success", "count": 5}

with open('output.json', 'w') as file:
    json.dump(new_data, file, indent=2)