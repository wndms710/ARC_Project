file_names = []

for i in range(25, 901, 25):
    file_name = 'T.' + '{}'.format(i) + '.txt'
    file_names.append(file_name)

file_names.append('T.918.txt')

with open('T.txt', 'w') as outfile:
    for filename in file_names:
        with open(filename) as file:
            for line in file:
                outfile.write(line)
        print('Merge {} to file'.format(filename))

print("Finish merge")
