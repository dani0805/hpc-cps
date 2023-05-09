import csv

with open('data.csv', 'a') as f:
    writer = csv.writer(f)
    for i in range(1000000):
        writer.writerow([i, i**2])

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 100:
            print(row)
