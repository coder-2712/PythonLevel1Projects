import random

print('Welcome to the Ficticious Grocery Store!')
print()
special = random.randint(0,6)
if special == 1:
    print("Today's special: Blue Lobsters")

menu = ['Apples','Oranges','Tomatoes','Onions', 'Milk  ','Eggs        ','Butter','Cheese','Rice       ','Flour','Cereal','Bread',' Sauce','Peanuts','Jam     ','Chips','Cookies','Cocoa','Candy','Water','Juice','Soda','Lemonade']
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


next_500 = 500*(grand_tot//500+1)
gap_500 = next_500 - grand_tot

print()
kk = 1
dctratelist = [10.0,20.0,30.0]
dctrate = 10.0
next500_list = []


for jj in range(len(dctratelist)):
    dctrate = dctratelist[jj]
    searching = True
    kk = 1
    while searching:
        next_500 = 500 * (grand_tot//500+kk)
        gap_500 = next_500 - grand_tot
        dct = next_500*dctrate/100
        if gap_500>dct:
            searching = False
        else:
            kk+=1
    next500_list.append(next_500)



for kk in range(1,len(next500_list)):
    if next500_list[kk]<=next500_list[kk-1]:
        next500_list[kk] = next500_list[kk-1]+ 500

print("We have some offers for you!")
print()
for kk in range(len(dctratelist)):
    print(str(kk+1) + '.' ,'Purchase for (in INR)',next500_list[kk],'to get a',dctratelist[kk],'% discount.')

dw = int(input('Which offer would you want to take? (Select 1,2,3, for respective discounts, or any other number for checkout.)'))
add_quant=[]
if dw == 1 or dw == 2 or dw == 3 :
    gap_500 = next500_list[dw-1]- grand_tot
    dctrate = dctratelist[dw-1]
    print('You have the following options\n')
    for kk in range(len(menu)):
        add_quant.append((int(gap_500//price[kk]+1)))
        print(str(kk+1), '. Add', menu[kk], str(add_quant[kk]), 'units')
    
    add_on = int(input('Please indicate your preference\n'))

    if menu[add_on-1] in shopping_cart:
        idx = shopping_cart.index(menu[add_on-1])
        shopping_quant[idx]+=add_quant[add_on-1]
    else:
        shopping_cart.append(menu[add_on-1])        
        shopping_quant.append(add_quant[add_on-1])        

    print('shopping cart updated')
    print('Proceed to checkout')    
else:
    print('Proceed to checkout')
    dctrate=0.0

# Give title to the shopping cart. 
# Add the price of every item in the shopping cart, and also the total. 
grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

print()

tax_rate = 10.0; 

if dw == 1 or dw == 2 or dw == 3:
    discount = round(dctrate/100.0*grand_tot, 2)
else:
    discount = 0.0; 

tax = round(tax_rate/100.0*(grand_tot-discount), 2)

print('Your total order is (INR)', grand_tot)
print('Discount (10%) is (INR)', discount)
print('Your order value, after discount is (INR)', round(grand_tot-discount, 2))
print('Tax (10%) is (INR)', round(tax, 2)); 
print('Total you have to pay (INR) ', round(grand_tot - discount + tax, 2))

print('Thanks')
print('Bye')
