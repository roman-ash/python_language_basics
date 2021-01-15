with open("file1.txt", "r") as f:
    str_count = 0
    for line in f:
        str_count += 1
        word_count = 0
        for word in line.split():
            word_count += 1
        if word_count == 0:
            break
        print(f"{word_count} words on line {str_count}")
print(f"Number of lines: {str_count - 1}")
