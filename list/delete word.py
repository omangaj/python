text = input("Enter the text = ")
words = text.split()


data = input("Enter the word to delete = ")
status = 0

for word in words:
    if word == data:
        status = 1
        words.remove(data)

if status:
    text = " ".join(words)
    print(text)