with open("text_4.txt", "r") as f:
    translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    my_str = ""
    for line in f:
        for word in line.split():
            if word in translate_dict:
                my_str += line.replace(word, translate_dict[word])
    with open("new_text_4.txt", "w") as x:
        x.write(my_str)
