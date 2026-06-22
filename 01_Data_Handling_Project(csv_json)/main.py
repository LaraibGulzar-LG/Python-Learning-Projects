# This is a single file for all operations #

# CSV read karo
import csv

print("=== CSV READING ===")
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n=== CSV AS DICTIONARY ===")
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['age'], row['city'])

# JSON read karo
import json

print("\n=== JSON READING ===")

with open('users.json', 'r') as file:
    users_data = json.load(file)
    for user in users_data['users']:
        print(user['name'], user['age'])

# Write karo CSV mein
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Score'])
    writer.writerow(['Ali', 85])
    writer.writerow(['Sara', 92])
print("Output.csv created!")

# Write JSON
new_data = {"status": "success", "count": 5}
with open('output.json', 'w') as file:
    json.dump(new_data, file, indent=2)
print("Output.json created!")