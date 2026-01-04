print ("Hello, welcome to ĐengHui coffee!!!!!")

name = input ("What is your name? \n")

#coffee 
menu = ("Black cf, Capuchino, Matcha latte, Atom bomb")

#ban name
if name == "Ben" or name == "Patrick" or name == "Loki":
    evil_status = input ("Are you evil?\n")
    good_deeds = int (input ("How many good things you done today?\n"))

    if evil_status == "Yes" and good_deeds < 4:
        print ("GET OUT!!! You are not wellcome evil " + name + "!!!")
        exit ()
    else:
        print ("So you are good " + name + ", wellcome!!")
else: 
    print ("Hello " + name + ", thank you for coming today.\n\n\n")

print (name + ", what you like to order today, here is our menu\n" + menu)

#Caculate bills 
order = input ()

#price
if order == "Atom bomb":
    price = 100
elif order == "Black cf":
    price = 5
elif order == "Capuchino":
    price = 6
elif order == "Matcha latte":
    cream = input ("Do you want extra cream?\n")
    if cream == "Yes":
        price = 11
    else:
        price = 8
else:
    print ("Sorry, we don't have that here")
    price = 0
    exit ()

quantity = input ("How many coffees would you want?\n")
print ("It will cost " + str(price) + " for each.")
total = price * int (quantity)

print ("Your total is: $" + str (total))

print ("Sound good " + name + ". We'll have your " + quantity + " " + order + " right in the moment.")
