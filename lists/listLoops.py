letters = ["a", "b", "c"]

for letter in enumerate(letters):
    print(letter)

letters.append(1) # add
letters.insert(0, "-")
letters.pop()

del letters[0:3]
letters.clear()

print(letters)