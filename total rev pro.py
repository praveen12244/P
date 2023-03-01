
def calc_total_rev(p):
    total_rev=0
    for pro in p:
        total_rev += pro["price"]*pro["quantity"]
    return total_rev
p=[{"name":"samsung","price":4997654,"quantity":5676},
   {"name":"Hp","price":2300000,"quantity":6567},
   {"name":"lenovo","price":2380000,"quantity":6532}
   ]
total_rev=calc_total_rev(p)
print(total_rev)

