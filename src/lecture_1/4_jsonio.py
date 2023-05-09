import json

data = [i**2 for i in range(1000000)]
with open('data.txt', 'w') as f:
    json.dump(data, f)

with open('data.txt', 'r') as f:
    data = json.load(f)
    print(data[100])
