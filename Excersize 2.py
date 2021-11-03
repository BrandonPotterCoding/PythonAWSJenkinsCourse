name =input("Enter your Name: ")

age =input("Enter your Age: ")

code =input("Enter your Years of Coding Experience: ")

user = {
    "name": name,
    "age": age,
    "experience": code
}
first = input("Enter your Three First Coding Languages(seperated by a comma): ")
ogLanguagesList=first.split(",")
ogLanguages=tuple(ogLanguagesList)
favorite =input("Enter your Three Favorite Coding Languages(seperated by a comma): ")
languages = favorite.split(",")
wait = input("wait")
similar = set(ogLanguages).intersection(set(languages))
user["First Languages"]=ogLanguages
user["Favorite Languages"]=favorite
user["First and Favorite"]=similar

print(user)
