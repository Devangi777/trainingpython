file_path = "demo.txt"

try:
    with open(file_path, 'r') as f:
        text = f.read()
        if text == "":
            print("The file is empty.")
        else:
            lines = text.splitlines()
            words = text.split()
            print("Number of lines:", len(lines))
            print("Number of words:", len(words))
            print("Number of characters:", len(text))
except FileNotFoundError:
    print("File not found.")
