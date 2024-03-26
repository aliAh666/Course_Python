# list="Ali youssef ahmad"
# print("s" in list)
# print("A" in list)
# print("G" in list)

# list1 = ['ali','ahmad','meme','ooo']
# print("ali" in list1)

# myCountry = input("please enter your country\t")

# countryOne = ['usa','russia','swiden','portogal','lebanon']
# countryTow = ['syria','ksa','uae','jorden','egypt']

# disCount1 = 20
# disCount2 = 50

# if myCountry in countryOne :
#     print(f"welcome you have {disCount1} discount")

# if myCountry in countryTow :
#     print(f"welcome you have {disCount2} discount")


# ===========================================================================



# import emoji
# admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# print(emoji.emojize('welcome to our website  :red_heart:'))
# name = input("please enter your name \n").strip().capitalize()

# if name in admins:

#     print(f"welcome back {name}")
#     option = input("Enter Update[U] or Delete[D] ?").strip().capitalize()
#     if option == "Update" or option == "U":

#         thenewName = input("Enter your new name please \n").strip().capitalize()
#         admins[admins.index(name)] = thenewName
#         print(emoji.emojize('Your name updated  :red_heart:'))
#         print(f"wow nice name {thenewName} or {name} hahaha sory")

#     elif option == "Delete" or option == "D":
#         admins.remove(name)
#         print(emoji.emojize("Your name deleted  :green_heart:"))
#         print(admins)
#     else:
#         print("wrong entry")

# else:
#     print("sorry You do not have permission to enter.. ")
#     register = input("Do you want to register with us? Yes[Y],No[N] \n").strip().capitalize()
#     if register =="Yes" or register =="Y" :
#         print(emoji.emojize('you are regestred thank you"  :red_heart:'))
#         admins.append(name)
#         print(admins)
#     elif register =="No" or register =="N" :
#         print("like you want")
#         print(emoji.emojize('visite our website bro later  :green_heart:'))
#     else:
#          print("wrong entry")

    

# ===========================================================================



# my_website = []
# maximum_num = 5
# while maximum_num > 0 :
#     add_website = input("enter your website please\n").strip().capitalize()
#     my_website.append(f"https://{add_website.strip().lower()}")
#     maximum_num -= 1


# else:
#     print("you cant add any more")
#     print(my_website)

    

# ===========================================================================


# mylist = [1,2,3,4,5,6,7,8,9]
# for number in mylist:
#     if number %2 ==0 :
#         print(f"this number [{number}] even")
#     else:
#         print(f"this number [{number}] odd")



# ===========================================================================

# 1  d     ==  1000 y
# 24 h     ==  1000 y
# 1  h     ==  41.666666666666666666666666666667 y
# 1  m     ==  0.694444444444444444444444444444445 y
# 1  s     ==  0.01157407407407407407407407407 y
                 

# ===========================================================================

# mySlills = {
#     "Html"   : "90%",
#     "Css"    : "70%",
#     "Js"     : "40%",
#     "Python" : "60%"
# }

# print(mySlills)
# print(mySlills["Js"])

# for i in mySlills:

#     print(f"My Progress in Lang {i} is: {mySlills.get(i)}")
    
# print("="*50)

# for i in mySlills:
#     print(f"My Progress in Lang {i} is: {mySlills[i]}")



# ===========================================================================


# peoples = {
#   "Osama": {
#     "Html": "70%",
#     "Css": "80%",
#     "Js": "70%"
#   },
#   "Ahmed": {
#     "Html": "90%",
#     "Css": "80%",
#     "Js": "90%"
#   },
#   "Sayed": {
#     "Html": "70%",
#     "Css": "60%",
#     "Js": "90%"
#   }
# }


# for name in peoples:
#     print(f"{name}")
#     for skills in peoples[name]:
#         print(f"the skills in {skills} is {peoples[name][skills]}")




# ===========================================================================



# peoples = {
#   "Osama": {
#     "Html": "70%",
#     "Css": "80%",
#     "Js": "70%"
#   },
#   "Ahmed": {
#     "Html": "90%",
#     "Css": "80%",
#     "Js": "90%"
#   },
#   "Sayed": {
#     "Html": "70%",
#     "Css": "60%",
#     "Js": "90%"
#   }
# }

# for main_key_pepoles, main_value_pepoles in peoples.items():
#     print("="*50)
#     print(f"{main_key_pepoles}")
#     for chiled_key,chiled_value in main_value_pepoles.items():
#       print(f"Progress in {chiled_key} is: {chiled_value}")



# ===========================================================================


# def sey_name(first_name,midel_name,last_name):
#     print(f"hello {first_name.capitalize()} {midel_name.upper().capitalize()} {last_name.capitalize():.2s}")

# sey_name("ali","youseef","ahmad")

# def employe (name,age,country="unknown"):
#     print(f"first employe is:\n {name} age: {age} and country: {country}")
  
# employe("ali ahmad",26,"syria")
# employe("lamis ahmad",27)
# employe("abeer ahmad",28)


print(type(-100))
print(type(1.3))