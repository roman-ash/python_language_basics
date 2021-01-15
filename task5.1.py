with open("file1.txt", "w") as f:
    while True:
        answer = input("Enter the data. Enter an empty line to finish entering data.\n: ")
        f.write(f"{answer}\n")
        if answer == "":
            break
