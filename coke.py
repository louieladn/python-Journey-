# ammount of coke
coke_value = 50
while coke_value > 0:
    print("Ammount due: ", coke_value)

    coin = int(input("Insert coin: "))

    if coin in [ 25, 10, 5]:
        coke_value -= coin

change = abs(coke_value)        
print( "Change Owed", change)