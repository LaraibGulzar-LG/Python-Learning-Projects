import csv

fieldnames = ['Name', 'Score', 'City'] 

with open('students_dict.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Asad', 'Score': 78, 'City': 'Karachi'})
    writer.writerow({'Name': 'Zainab', 'Score': 95, 'City': 'Lahore'})
print("students_dict.csv created!")