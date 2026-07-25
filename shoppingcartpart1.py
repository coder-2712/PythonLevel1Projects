import random

print('Welcome to the Ficticious Grocery Store!')
print()
special = random.randint(0,6)
if special == 1:
    print("Today's special: Blue Lobsters")

menu = ['Apples','Oranges','Tomatoes','Onions', 'Milk  ','Eggs        ','Butter','Cheese','Rice       ','Flour','Cereal','Bread',' Sauce','Peanuts','Jam      ','Chips','Cookies','Chocolate','Candy','Water','Juice','Soda','Lemonade']
price = [15.99, 22.99, 19.99, 21.99, 17.99,5.49,20.59,14.99,46.59,37.49,28.99,19.49,12.48,37.29,64.67,28.34,10.67,17.39,19.26,4.49,12.78,14.76,18.98,70.78]
if special == 1:
    print("Today's special: Blue Lobsters")
    menu.append("Blue Lobster")
elif special == 2:
    print("Today's special: Pink Pineapples")
    menu.append("Pink Pineapple")
elif special==3:
    print("Today's Special: Green Honey")
    menu.append("Green Honey")
elif special == 4:
    print("Today's special: Frying Pans")
    menu.append("frying pans")
elif special == 5:
    print("Today's special: Shampoo")
    menu.append("Shampoo")
elif special == 6:
    print("Today's special: Steel Napkins")
    menu.append("Steel napkins")
else:
    print("Today's special: A PS 5")
    menu.append("PS 5       ")
print('ITEM', 'PRICE (INR), excl. Tax', sep='\t\t\t')
for kk in range(len(menu)):
    print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

shopping_cart = [] 
shopping_quant= []
shopping_complete = 0

while shopping_complete==0:

    order = int(input('Enter 1 to 24 to select an item, 25 to proceed to checkout.\n')) 
    
   
    
    if order <= 24:
        print('You selected', menu[order-1])
        quant = int(input('How many units do you wish to purchase?\n'))

        if menu[order-1] in shopping_cart:
            idx = shopping_cart.index(menu[order-1])
            
            shopping_quant[idx]+=quant
        else:
            shopping_cart.append(menu[order-1])        
            shopping_quant.append(quant)        
        
        print('Added to shopping cart:', quant, 'units of', menu[order-1])
    elif order == 25:
        shopping_complete = 1
    else: 
        print("Sorry that was not a valid input.")
        

print()
print('Your Shopping Cart:')

grand_tot = 0.0
print('ITEM', 'QUANTITY', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

grand_tot = round(grand_tot, 2)
print()
print('Your total order is (INR)', grand_tot)