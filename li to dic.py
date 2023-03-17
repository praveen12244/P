def dic_na(q):
    g={}
    
    g["costumer name"]=q[0]
    g["product name"]=q[1]
    g["quantity"]=q[2]
    g["price"]=q[3]
    g["revenue"]=int(q[2])*int(q[3])
    return g

i=input("enter the costumer name,enter he product name,enter the quantity:,enter the price").split(" ")
print(i)
b=tuple(i)
o=dic_na(b)
print(o)