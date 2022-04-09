import random

card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[]
dealer_card = []
status = False  
for i in range(0,2):
    user_card.append(random.randint(2,11))
    dealer_card.append(random.randint(2,11))
print(user_card)
print(dealer_card)
sum_user_card = sum(user_card)
print(f"User : {sum_user_card}")
sum_dealer_card = sum(dealer_card)
print(f"Dealer : {sum_dealer_card}")
if  sum_user_card == 21:
    print("User won!")
elif sum_dealer_card == 21:
    print("Dealer won!")
while not status:
    def card_loop():
        user_card.append(random.randint(2,11))
        print(user_card)
        sum_user_card = sum(user_card)
        print(f"User : {sum_user_card}")
        for i in range(0,len(user_card)):
            if user_card[i] == 11:
                ace = int(input("Do you want to use 1 or 11?"))
                if ace == 1:
                    user_card[i] = 1
                    print(user_card)
                    sum_user_card = sum(user_card)
                    print(f"User: {sum_user_card}")
        # print(user_card)
        # sum_user_card = sum(user_card)
        # print(f"User: {sum_user_card}")
        if  sum_user_card == 21:
            print("User won!")
            
            status = True
        elif sum_dealer_card == 21:
            print("Dealer won!")
            status = True
        if  sum_user_card > 21:
            print("Dealer won!")  
            status = True
            
        elif sum_dealer_card > 21:
            print("User won!") 
            status = True
            
    more_card = input("Do you want to draw another card? y/n").lower()
    if more_card == 'y':
        card_loop()
    elif more_card == 'n':
        while sum_dealer_card < 17:
            dealer_card.append(random.randint(2,11))
            print(dealer_card)
            sum_dealer_card = sum(dealer_card)
            print(f"Dealer : {sum_dealer_card}")
        if sum_dealer_card > 21:
            print("User won!")  
            status = True
        elif sum_dealer_card == sum_user_card:
            print("Draw!") 
            status = True
        elif sum_dealer_card > sum_user_card:
            print("Dealer won!") 
            status = True
        elif sum_dealer_card < sum_user_card:
            print("User won!")
            status = True
       
    
    
                     
                     
    
    
                     

   



