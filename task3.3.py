STRING = "python"
MY_SET = set()
for i in range(len(STRING)):
    for j in range(i + 1, len(STRING) + 1):
        if STRING[i:j] != STRING:
            MY_SET.add(hash(STRING[i:j]))
print(f'{len(MY_SET)} unique substrings')
print(MY_SET)
