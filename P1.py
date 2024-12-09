price = 0
bill =0
while True:
    print('Welcome to restaurant')
    d = {'idli': 50, 'poori': 60, 'dosa': 65, 'tea': 10, 'exit': None}
    ch = input("Enter the choice = ").lower()
    print("You have selected = ", ch)
    if ch in ("idli","poori","dosa","tea"):
        qty = int(input("Enter the qty = "))
        price = d[ch] * qty
    elif  ch.lower() == "exit":
        print("PRICE = ",bill)
        break
    else:
        print('Invalid choice "Contact LENSCART"')
        price = 0
    bill = bill + price