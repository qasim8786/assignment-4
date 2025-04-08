with open('output.txt','w') as file:
    write = file.write((input("Enter text to write to the file: ") + "\n"))
print("Data successfully written to output.txt.\n")

with open('output.txt','a') as file:
    second_write = file.write((input("Enter additional text to append: ") + "\n"))
print("Data successfully appended.\n")

print("Final content of output.txt:\n")
with open('output.txt','r') as final:
    reading = final.read()
    print(reading)
