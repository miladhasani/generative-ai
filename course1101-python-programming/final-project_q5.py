vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
allowed_characters = [".", "!", "?"]

n = str.split(input(), sep=" ")

counter = 0

for word in n:
    if len(word) < 5:
        continue

    for character in word:
        if character in allowed_characters or character in vowels:
            counter = 0
            continue
        else:
            counter += 1
    if counter > 4:
        print(word, end=" ")
    counter = 0