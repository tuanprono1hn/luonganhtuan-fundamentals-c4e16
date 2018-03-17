sample = "ThiS is String with Upper and lower case Letters".lower()
# split_sample = list(sample.lower())
letter_count = {}
for letter in sample:
    letter_count[letter] = letter_count.get(letter, 0) + 1
# letter_count
for a in letter_count:
    if letter_count[a] == " ":
        del letter_count[a]
for i, k in sorted(letter_count.items()):
    print(i, k)
