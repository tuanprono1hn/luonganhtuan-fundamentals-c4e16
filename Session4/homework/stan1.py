name = input("Your name: ")
words = name.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()
print("Upadate: ", " ".join(words))
# google
