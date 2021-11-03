print("Enter your name: ")
name = input()

age =input("Enter your age: ")

names = name.split()

year = (2021-age)

email = names[0]+"."+names[1]+str(year)[-2:]

print(email)
