#BlackJack 
import random
play_again = "Y"
bet_for_game = 0 
user_card_total = 0 
dealer_card_total = 0
round_counter = 0 
user_win = False
dealer_win = False
repeat_game = "N"

#Dictionary of all cards and their values
card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

print ("Welcome to 'One Card At A Time BlackJack'! You and the computer, aka the 'Dealer', will both be dealt one card after you have made a bet. ")
print ("The goal of the game is to get as close to 21 as possible, without going over. You will make an ititial bet, and then can double it each round.")
print ("I hope you have fun!")
balance = 1000
    
print (f"You will start with a balance of {balance}. Now, Let's begin!")

#Now we have a balance, we can begin the game.

def wager (bet_for_round):
    global bet_for_game
    global balance
    global round_counter
    round_counter += 1
    print (f"Welcome to round {round_counter}.")

    #Gets a valid bet from the user
    if bet_for_round != 0:
        while True:
            try:
                double_down = str(input(f"Please enter 'Y' if you would like to double your bet, and 'N' if you would just like to hit (Your current bet is {bet_for_round}): "))
                if double_down.upper() == "Y":
                    if balance - bet_for_round < 0:
                        print ("Your balance is too low to double down. You will just hit")
                        break
                    else:
                        balance = balance - bet_for_round
                        bet_for_game = bet_for_round + bet_for_round
                        break
                else:
                    break
            except:
                print ("An error occurred! Please try again! (Make sure you are entering just the letter)")
            
    if bet_for_round == 0:
        while True:
            try:
                bet_for_round = int(input(("Please enter your bet. By doing so, you will draw a random card: ")))
                while bet_for_round > balance:
                    bet_for_round = int(input("Bet cannot be greater than current balance. Please enter a valid bet: "))
                break
            except:
                print ("An error occurred! Please try again! (Make sure you are entering an integer)")
        balance = balance - bet_for_round
        bet_for_game = bet_for_round

def play_round (user_total, dealer_total):
    global repeat_game

    #Card Drawing and Adding to Total
    global play_again
    if play_again == "Y":
            user_draw = random.choice(list(card_values))
            numeric_user_draw = card_values[user_draw]
            global user_card_total
            if user_draw != "A":
                user_total = user_total + numeric_user_draw
    
    global dealer_card_total
    if dealer_total >= 16:
        dealer_will_draw = False
        
    if dealer_total <= 16:
        dealer_will_draw = True
        house_draw = random.choice(list(card_values))
        numeric_dealer_draw = card_values[house_draw]
        dealer_total = dealer_total + numeric_dealer_draw
    
    else:
        print ("The dealer cannot draw anymore")
        
    if play_again == "Y":
        print (f"You drew: {user_draw}")
    
    if user_draw == "A":
        while True:
            try:
                numeric_user_draw = int(input(("You drew an ace! Type 1 for it to equal 1, or 11 for it to equal 11: ")))
                user_total = user_total + numeric_user_draw
                break
            except:
                print ("An error occurred! Please try again! (Make sure you are entering an integer)")
    
    user_card_total = user_total
    dealer_card_total = dealer_total
    
    print (f"Your total is: {user_total}")
    
    if dealer_will_draw == True:
        print (f"The dealer drew: {house_draw}")
    
    print (f"The dealer's total is: {dealer_card_total}")
    
    if dealer_total == 21:
        print ("Dealer BlackJack! You Lose!")
        global dealer_win
        dealer_win = True
        
    if user_total > 21:
        print ("You Went Bust! The Dealer Wins!")
        dealer_win = True
        
    elif dealer_total > 21 and user_total <= 21:
        print("The Dealer Went Bust! You Win!")
        global user_win
        user_win = True
        
    elif user_total == 21 and dealer_total == 21:
        print ("Both have Blackjack! Dealer wins!")
        dealer_win = True
        
    elif dealer_total != 21 and user_total == 21:
        print("You got Blackjack! You Win!")
        user_win = True
    
wager(0)
play_round (0, 0)

play_again = str(input("Would you like to play another round? Please type 'Y' if you would like to continue, and 'N' if you would like to stand: "))

while play_again == "Y" and user_card_total < 21 and user_win != True and dealer_win != True:
    wager(bet_for_game)
    play_round (user_card_total, dealer_card_total)
    if user_card_total < 21 and user_win != True and dealer_win != True:
        play_again = str(input("Would you like to play another round? Please type 'Y' if you would like to continue, and 'N' if you would like to stand: "))


def dealer_only():
    
    global dealer_card_total
    while dealer_card_total <= 16:
        house_draw = random.choice(list(card_values))
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
    global user_card_total, dealer_card_total, dealer_win, user_win, bet_for_game, winnings, balance, round_counter, play_again
    if user_card_total > dealer_card_total and dealer_win != True or user_win == True:
        print ("You win!")
        winnings = bet_for_game * 3
        balance = balance + winnings
        print (f"Your winnings were: {winnings}")
    
    else:
        print ("You Lost!")
    
    print (f"Your total balance is now {balance}")
    
    #Resetting the Variables for the Next Game
    round_counter = 0
    bet_for_game = 0
    play_again = "Y"
    winnings = 0 
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
    
    wager(0)
    play_round (0, 0)

    play_again = str(input("Would you like to play another round? Please type 'Y' if you would like to continue, and 'N' if you would like to stand: "))

    while play_again == "Y" and user_card_total < 21 and user_win != True and dealer_win != True:
        wager(bet_for_game)
        play_round (user_card_total, dealer_card_total)
        if user_card_total < 21 and user_win != True and dealer_win != True:
            play_again = str(input("Would you like to play another round? Please type 'Y' if you would like to continue, and 'N' if you would like to stand: "))
    
    dealer_only ()
    
    check_win ()
    
    repeat()
    
print (f"Thanks for playing! You've left with a balance of {balance}")