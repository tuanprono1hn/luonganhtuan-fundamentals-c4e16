height = float(input("Nhap chieu cao (cm): "))
weight = float(input("Nhap can nang (kg): "))

cao = height/100
bmi = weight/(cao**2)
print("BMI: %.2f" % (bmi))
if bmi < 16:
    print("You are severely underweight")
elif bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are overweight")
else:
    print("Obese")
