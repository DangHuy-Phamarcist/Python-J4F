#python list
mobilesuitList = ["Zaku II", "Gyan", "Dom", "Z'Gok", "Big Zam", "Sinanju", "Gelgoog", "Zeong", "Gouf"]
#zeonNumb = ["Zaku II", 6, 12.6, True]

mobilesuitList.extend (["Sazabi", "Black Tri Star"])
#mobilesuitList.clear ()
mobilesuitList.remove("Zaku II")
print (mobilesuitList.pop(1))
print ("The mobile suit just destroy: ")
#print (*mobliesuitList, sep = "\n")
print (mobilesuitList)

#python list can be change
mobilesuitList [2] = "Denghui"
print (mobilesuitList)

#python tuble can't be change, faster loading
#mobilesuitList (2) = "DengHui"
#print (mobilesuitList)
