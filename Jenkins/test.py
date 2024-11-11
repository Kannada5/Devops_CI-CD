# Define the file name
filename = 'first.txt'

# Open the file in write mode
with open(filename, 'w') as file:
    # Write some content to the file
    file.write('Hello, World!')

print(f'File {filename} created successfully.')
