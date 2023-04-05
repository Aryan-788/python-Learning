# Dictionary is nothing but key value pairs
d1 = { }
# print(type (d1))
d2 = { "harry":"burger", "rohan":"fish", "shubham":"maggie", "aryan":{"B":"maggie", "L":"roti", "D":"chicken"}  }
print(d2)
d2["ankit"] = "junk Food"
d2["rohit"] = "kebabs"
print(d2["aryan"])
print(d2)
d3 = d2
d3 = d2.copy()
del d3["harry"]
d2.update({"leena":"Toffee"})
print(d2)
print(d2.keys())
print(d2.items())

