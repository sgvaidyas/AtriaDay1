"""
1
12
123
1234
123
12
1
"""
n = int(input("Enter n = "))
for i in range(1,2*n):
    if i<=n:
        for j in range(1,i+1):
            print(j,end="\t")
    else:
        for j in range(1,2*n-i+1):
            print(j,end="\t")
    print()





"""for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="\t")
    print()
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j,end="\t")
    print()"""