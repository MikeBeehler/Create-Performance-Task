#BlackJack 
#PROBLEMS: USER CAN ONLY BET ONCE DURING ADDITIONAL ROUNDS
import random
play_again = "Y"
bet = 0 
user_card_total = 0 
dealer_card_total = 0
round_counter = 0 
user_win = False
dealer_win = False
repeat_game = "N"
#Dictionary of all cards and their values
card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

#Asking the user if they know how to play the game
know_rules = input("Welcome to my take on the game of BlackJack! If you want to see my rules, please type 'Y'. If not, type 'N': ")

while True:
    
    if know_rules.upper() == "Y" or know_rules.upper() == "YES":
        #TYPE OUT RULES!
        print ("Try looking at Wikipedia for the general rules!")
        break
    
    elif know_rules.upper() == "N" or know_rules.upper() == "NO":
        break
        
    else:
        know_rules = str(input(("Invalid input. Please try again.")))


#Getting the User to enter a valid balance   
while True:
    try:
        balance = int(input(("Please enter your starting balance: ")))
        break
    except:
        print ("An error occurred! Please try again! (Make sure you are entering an integer)")
    

#Now we have a balance, we can begin the game.

def play_round (money, user_total, dealer_total):
    global bet
    global balance
    global round_counter
    round_counter += 1
    print (f"Welcome to round {round_counter}.")
    #Gets a valid bet from the user
    if bet == 0:
        while True:
            try:
                bet = int(input(("Please enter your bet: ")))
                while bet > balance:
                    bet = int(input("Bet cannot be greater than current balance. Please enter a valid bet: "))
                break
            except:
                print ("An error occurred! Please try again! (Make sure you are entering an integer)")
        balance = balance - bet
        
    else:
        while True:
            try:
                double_down = str(input(f"Please enter 'Y' if you would like to double down, and 'N' if you would just like to hit (Your current bet is {bet}): "))
                if double_down.upper() == "Y":
                    if balance - bet < 0:
                        print ("Your balance is too low to double down. You will just hit")
                        break
                    else:
                        balance = balance - bet
                        bet = bet + bet
                        break
                else:
                    break
            except:
                print ("An error occurred! Please try again! (Make sure you are entering just the letter)")
            
    
    #Card Drawing and Adding to Total
    global play_again
    if play_again == "Y":
            user_draw = random.choice(list(card_values.keys()))
            numeric_user_draw = card_values[user_draw]
            global user_card_total
            if user_draw != "A":
                user_card_total = user_card_total + numeric_user_draw
    
    global dealer_card_total
    if dealer_card_total >= 16:
        dealer_will_draw = False
        
    if dealer_card_total <= 16:
        dealer_will_draw = True
        house_draw = random.choice(list(card_values.keys()))
        numeric_house_draw = card_values[house_draw]
        dealer_card_total = dealer_card_total + numeric_house_draw
    
    else:
        print ("The dealer cannot draw anymore")
        
    if play_again == "Y":
        print (f"You drew: {user_draw}")
    
    if user_draw == "A":
        while True:
            try:
                numeric_user_draw = int(input(("You drew an ace! Type 1 for it to equal 1, or 11 for it to equal 11: ")))
                user_card_total = user_card_total + numeric_user_draw
                break
            except:
                print ("An error occurred! Please try again! (Make sure you are entering an integer)")
    
    print (f"Your total is: {user_card_total}")
    
    if dealer_will_draw == True:
        print (f"The dealer drew: {house_draw}")
    
    print (f"The dealer's total is: {dealer_card_total}")
    
        

    if dealer_card_total == 21:
        print ("Dealer BlackJack! You Lose!")
        global dealer_win
        dealer_win = True
        
    if user_card_total > 21:
        print ("You Went Bust! The Dealer Wins!")
        dealer_win = True
        
    elif dealer_card_total > 21 and user_card_total <= 21:
        print("The Dealer Went Bust! You Win!")
        global user_win
        user_win = True
        
    elif user_card_total == 21 and dealer_card_total == 21:
        print ("Both have Blackjack! Dealer wins!")
        dealer_win = True
        
    elif dealer_card_total != 21 and user_card_total == 21:
        print("You got Blackjack! You Win!")
        user_win = True
    
    
play_round (balance, user_card_total, dealer_card_total)

play_again = str(input("Would you like to play another round? Please type 'Y' if you would like to continue, and 'N' if you would like to stand: "))

while play_again == "Y" and user_card_total < 21 and user_win != True and dealer_win != True:
    play_round (balance, user_card_total, dealer_card_total)
    if user_card_total < 21:
        play_again = str(input("Would you like to play another round? Please type 'Y' if you would like to continue, and 'N' if you would like to stand: "))


def dealer_only():
    
    global dealer_card_total
    while dealer_card_total <= 16:
        house_draw = random.choice(list(card_values.keys()))
        numeric_house_draw = card_values[house_draw]
        dealer_card_total = dealer_card_total + numeric_house_draw

        print (f"The dealer drew: {house_draw}")
        print (f"The dealer's total is: {dealer_card_total}")

        if dealer_card_total > 21:
            print("The Dealer Went Bust! You Win!")
            global user_win
            user_win = True

if dealer_card_total <=16 and user_card_total < 21:
    dealer_only()
    
def check_win():
    #Check Win Conditions
    global user_card_total, dealer_card_total, dealer_win, user_win, bet, winnings, balance, round_counter, play_again
    if user_card_total > dealer_card_total and dealer_win != True or user_win == True:
        print ("You win!")
        winnings = bet * 3
        balance = balance + winnings
        print (f"Your winnings were: {winnings}")
    
    else:
        print ("You Lost!")
    
    print (f"Your total balance is now {balance}")
    
    #Resetting the Variables for the Next Game
    round_counter = 0
    bet = 0
    play_again = "Y"
    winnings = 0 
    user_card_total = 0
    dealer_card_total = 0
    user_win = False
    dealer_win = False
    
check_win()

def repeat():
    global repeat_game
    while True:
        try:
            repeat_game = str(input("Would you like to play again? Type 'Y' if you would, and 'N' if you would like to end the game: "))
            
            if repeat_game.upper() == "Y" or repeat_game.upper() == "N":
                break
            
            else:
                print("Please enter a valid input (Y or N)")

        except:
            print ("Please enter a valid input (Y or N)")
            
            
repeat ()
while repeat_game == "Y":
    play_round (balance, 0, 0)
    dealer_only ()
    check_win ()
    repeat()
    
print (f"Thanks for playing! You've left with a balance of {balance}")