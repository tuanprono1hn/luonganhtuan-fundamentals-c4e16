font = int(input("Enter font size: "))
cao = int(font * 1.5)
if font < 6:
    print("Fail")
else:
    print(font * "* ", 3 * "  ", font * "* ", 3 * "  ", (font - 2) * "* ", 5 * "  ", font * "* ")
    for i in range(1, 3, 1):
        print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font + i - 5) * "  ", 1 * "* ", (5 - i) * "  ", 1 * "* ")
    for j in range(3, (cao - 2), 1):
        print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ")
    for k in range(cao, (cao - 2), -1):
        print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font - 3 + k - cao) * "  ", 1 * "* ", (font + 3 - font - k + cao) * "  ", 1 * "* ")
    print(font * "* ", 3 * "  ", font * "* ", 3 * "  ", (font - 2) * "* ", 5 * "  ", font * "* ")
