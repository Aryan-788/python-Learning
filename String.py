mystr = "aryan is a good boy"
mystr1 = "AryanIsaGoodBoy"
print(mystr)
print(len(mystr))
print(mystr [0: 5])  # print index 0 to index 4
print(mystr [0: 5 :3])
print(mystr.isalnum())  # ye check krta h ki sentence me gap h ya ni agar gap h to false return krta h or agar gap ni rhta h to trun return krta h
print(mystr1.isalnum())
print(mystr1.isalpha())
print(mystr.endswith("Boy"))  # ye check krta h ki sentence jo hai , wo end boy se hi kiya h ya ni
print(mystr.count("a"))  #ye count krta h
print(mystr.count("b"))
print(mystr.capitalize()) #phale leter to capital form me krta h
print(mystr.find("good")) #ye find krta h word ko ki wo kitne no. index pr h
print(mystr1.lower()) # ye sare sentence ko lower character me change krta h
print(mystr.upper()) # ye sare sentence ko upper character me change krta h
print(mystr.replace("is","are"))  # ye kisi word ko replace krta h
