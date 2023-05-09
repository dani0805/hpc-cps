with open('example.txt', 'w') as f:
    f.write('This is a sample text.')

f = open('example.txt', 'r')

content = f.read()

f.close()

print(content)

f = open('example.txt', 'a')
f.write("This is a sample text.")
f.close()

