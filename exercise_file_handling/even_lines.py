symbols = {"-", ",", ".", "!", "?"}

with open("input_files/text.txt", 'r') as file:
    text_lines = file.readlines()

for i in range(0, len(text_lines), 2):
    for symbol in symbols:
        text_lines[i] = text_lines[i].replace(symbol, "@")

    print(*text_lines[i].split()[::-1], sep=" ")
