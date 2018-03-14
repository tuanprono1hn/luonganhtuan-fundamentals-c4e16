print()
sheepsize = [10, 50, 300, 150, 260, 90, 25, 30]
print("Hello, my name is Tuan and these are my sheep size: ")
print(sheepsize)
print()
print("Now ny biggest sheep has size {}, let shear it!!!".format(max(sheepsize)))
print()
print("After shearing, here is my flock: ")
sheepsize[sheepsize.index(max(sheepsize))] = 8
print()
print(sheepsize)
print("**************************************************")

for j in range(3):
    print("Month ", j + 1)
    for i in range(len(sheepsize)):
        sheepsize[i] += 50
    print("One month has passed, now here is my flock: ")
    print(sheepsize)
    print()
    print("Now ny biggest sheep has size {}, let shear it!!!".format(max(sheepsize)))
    print()
    print("After shearing, here is my flock: ")
    sheepsize[sheepsize.index(max(sheepsize))] = 8
    print(sheepsize)
    print()
    print("**********************************************************")

print()
a = sum(sheepsize)
m = a * 2
print("My flock has size in total: ", a)
print("I would get ", a, "* 2$ = ", str(m) + "$")
