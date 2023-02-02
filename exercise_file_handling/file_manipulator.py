import os


def file_manipulator(*args):
    command = args[0]
    file_name = args[1]
    if command == "Create":
        file = open(f"output_files/{file_name}", 'w')
        file.close()

    elif command == "Add":
        content = args[2]
        with open(f"output_files/{file_name}", 'a') as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        if os.path.exists(f"output_files/{file_name}"):
            old_content = args[2]
            new_content = args[3]
            with open(f"output_files/{file_name}", 'r') as file:
                text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(old_content, new_content)

            with open(f"output_files/{file_name}", 'w') as file:
                file.write("".join(text))

        else:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(f"output_files/{file_name}"):
            os.remove(f"output_files/{file_name}")
        else:
            print("An error occurred")


line = input()

while line != "End":
    com = line.split("-")
    file_manipulator(*com)
    line = input()
