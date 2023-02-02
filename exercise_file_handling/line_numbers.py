from string import  punctuation

with open("input_files/text.txt", 'r') as file:
    text = file.readlines()

output = open("output_files/output.txt", "w")

for i in range(len(text)):
    row = text[i]

    letters = 0
    marks = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output.write(f"Line {i+1}: {row[:-1]} ({letters})({marks})\n")

output.close()