l = [11,22,33]

for x in l:
    print(x)
print(l)
print("-----------------------------------")
for i in range(len(l)):
    l[i]=99
    print(l[i])
print(l)