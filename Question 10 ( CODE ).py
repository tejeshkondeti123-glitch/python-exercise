# Frequency Counter Using Dictionaries

text = input("Enter a sentence: ")
frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("\nCharacter frequencies:")
for character, count in frequency.items():
    print(character, ":", count)


# output
# Enter a sentence: jainuniversity

# Character frequencies:
# j : 1
# a : 1
# i : 3
# n : 2
# u : 1
# v : 1
# e : 1
# r : 1
# s : 1
# t : 1
# y : 1