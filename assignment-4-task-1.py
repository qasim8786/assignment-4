try:
    with open('sample.txt','r') as file:
        read = file.read()
    print(read)
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")
    