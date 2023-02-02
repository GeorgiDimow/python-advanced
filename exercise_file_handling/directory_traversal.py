import os


def save_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file):
            save_extensions(os.path.join(dir_name, file_name), first_level=True)


directory = input()
extensions = {}

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])
result = []

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"---{file}")

with open(f"output_files/report.txt", "w") as file:
    file.write("\n".join(result))
