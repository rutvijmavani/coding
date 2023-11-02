with open("doc.txt", "r") as file:
    content = file.read()

words = content.split()

even_len_words = [word for word in words if len(word) % 2 == 0]

result = ' '.join(even_len_words)

print(result)
