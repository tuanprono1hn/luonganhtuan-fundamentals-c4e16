yob = int(input("Input your yob: "))
age = 2018 - yob
print("Your age: ", age)
if age < 10:
    print("Baby")
    print("Bye")
elif age <= 18:
    print("teenager")
elif age == 24:
    print("E")
else:
    print('Not Baby')
    print("Hi")
