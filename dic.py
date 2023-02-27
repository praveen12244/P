t={'em1_100':124,'em2_123':767,'em3_234':98,'em4_124':9000,'em5_125':768}
print(t)
sa=[]
for i in t.values():
    sa.append(i)

sa.sort()
print(sa)
sec=sa[-2]
print(sec)
aa=sa.index(sec)
print(aa)
bb=[]
for j in t.keys():
    bb.append(j)
print(bb[sa] )   

