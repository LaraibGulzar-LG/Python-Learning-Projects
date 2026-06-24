import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Score'])
    writer.writerow(['Ali', 85])
print("Output.csv created!")
