print("kindly wait while everything is set up for you. . .","\n")

#importing modules

import random
import mysql.connector as cn
import sys
import time
import matplotlib.pyplot as plt

#defining functions

def dice_roll():        #craps function
    dice_rolled=random.randint(2,12)
    return dice_rolled

def craps(bet):         #craps function
    ans_to_repeat_round='y'

    while ans_to_repeat_round=='y':
        print("We will be starting a new round")
        ans_shooter_or_not=input("Do you want to be the shooter? y/n: ")
        
        if ans_shooter_or_not=='y':
            print("You are the shooter. To start the game, select (type in) any 2 of these 5 dice.")
            dice_list=['Dice1', 'Dice2', 'Dice3', 'Dice4', 'Dice5']
            dice_choice=[]
            
            for p in range(2):
                dice=input(dice_list)
                dice_list.remove(dice)
                dice_choice.append(dice)
            print('The dice the shooter has chosen are',dice_choice)
            print("The shooter now chooses if they want to bet on the:\n1. Pass Line\n2. Don't Pass Line")
            comeout_bet=int(input("Enter 1 or 2 depending on your betting choice: "))
            bet_placed=int(input("Enter amount you would like to bet (increments of 5$, min bet is 5$): "))
            bet=bet-bet_placed
            if comeout_bet==1:
                print("You are betting",bet_placed," on the Pass Line")
                print("The shooter is rolling the come-out roll!")
                comeout_roll=dice_roll()
                print("The shooter has rolled a",comeout_roll)
                if comeout_roll==7 or comeout_roll==11:
                    print("The crowd cheers as the come-out roll wins!")
                    print("You have won",bet_placed*3,'$. ',end='')
                    bet=bet+(bet_placed*3)
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        print()
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break

                elif comeout_roll in [2,3,12]:
                    print("The crowd boos as the come-out roll loses!")
                    print("You have lost",bet_placed,'$. ',end='')
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break
                elif comeout_roll in [4,5,6,8,9,10]:
                    print("The shooter's point is now",comeout_roll)
                    print("Now the aim of the game is to land your point before you roll a 7 OR 11")
                    c=1
                    while c>=1:
                        j=dice_roll()
                        dice_rolled_in_round=j
                        print()
                        ans_to_more_bets=input("Do you want to place a single roll bet? y/n: ")
                        if ans_to_more_bets=='y':
                            print("Choose any one single roll bet you would like to make: ")
                            print("1. Three (Ace Deuce)- Payout=15:1")
                            print("2. Any 7 (Big Red)- Payout=4:1")
                            print("3. Any Craps (Three way)- Payout=7:1")
                            print("4. Two Craps or Aces (Snake Eyes)- Payout=30:1")
                            print("5. Twelve Craps (Boxcars or Midnight)- Payout=30:1")
                            print("6. Field Bet- Payout=2:1")
                            single_roll_bet_option=int(input("Enter option number of whichever bet you prefer: "))
                            bet_placed_sr=int(input("Enter amount you would like to bet (increments of 5$, min bet is 5$): "))
                            bet=bet-bet_placed_sr
                            for i in range(1):
                                print("The number rolled by the shooter (for single roll bet) is ",dice_rolled_in_round)
                                if single_roll_bet_option==1:
                                    if dice_rolled_in_round==3:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*15,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==2:
                                    if dice_rolled_in_round==7:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*4,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==3:
                                    if dice_rolled_in_round in [2,3,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*7,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==4:
                                    if dice_rolled_in_round==2:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==5:
                                    if dice_rolled_in_round==12:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==6:
                                    if dice_rolled_in_round in [2,3,4,9,10,11,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*2,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                        else:
                            pass
                        
                        print("The number rolled by the shooter (for main Line bet) is",dice_rolled_in_round)
                        if dice_rolled_in_round in [7,11]:
                            print("The crowd moans as the bettors who played for Pass Line have lost!")
                            print("You have lost",bet_placed,'$. ',end='')
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round==comeout_roll:
                            print("The crowd bursts in cheers as the bettors who played the Pass Line have won!")
                            print("You have won",bet_placed*2,'$. ',end='')
                            bet=bet+(bet_placed*2)
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round in [2,3,4,5,6,8,9,10,12]:
                            print("The crowd waits in anticipation for the next roll")
                            continue
            if comeout_bet==2:
                print("You are betting",bet_placed," on the Don't Pass Line")
                print("The shooter is rolling the come-out roll!")
                comeout_roll=dice_roll()
                print("The shooter has rolled a",comeout_roll)
                if comeout_roll==7 or comeout_roll==11:
                    print("The crowd moans as the come-out roll loses!")
                    print("You have lost",bet_placed,'$. ',end='')
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        print()
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break
                elif comeout_roll in [2,3,12]:
                    print("The crowd cheers as the come-out roll win!")
                    print("You have won",bet_placed*3,'$. ',end='')
                    bet=bet+(bet_placed*3)
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break
                elif comeout_roll in [4,5,6,8,9,10]:
                    print("The shooter's point is now",comeout_roll)
                    print("Now the aim of the game is to land a 7 or 11 before the shooter lands his point")
                    c=1
                    while c>=1:
                        j=dice_roll()
                        dice_rolled_in_round=j
                        print()
                        ans_to_more_bets=input("Do you want to place a single roll bet? y/n: ")
                        if ans_to_more_bets=='y':
                            print("Choose any one single roll bet you would like to make: ")
                            print("1. Three (Ace Deuce)- Payout=15:1")
                            print("2. Any 7 (Big Red)- Payout=4:1")
                            print("3. Any Craps (Three way)- Payout=7:1")
                            print("4. Two Craps or Aces (Snake Eyes)- Payout=30:1")
                            print("5. Twelve Craps (Boxcars or Midnight)- Payout=30:1")
                            print("6. Field Bet- Payout=2:1")
                            single_roll_bet_option=int(input("Enter option number of whichever bet you prefer: "))
                            bet_placed_sr=int(input("Enter amount you would like to bet (increments of 5$, min bet is 5$): "))
                            bet=bet-bet_placed_sr
                            for i in range(1):
                                print("The number rolled by the shooter (for single roll bet) is ",dice_rolled_in_round)
                                if single_roll_bet_option==1:
                                    if dice_rolled_in_round==3:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*15,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==2:
                                    if dice_rolled_in_round==7:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*4,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==3:
                                    if dice_rolled_in_round in [2,3,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*7,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==4:
                                    if dice_rolled_in_round==2:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==5:
                                    if dice_rolled_in_round==12:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                        print("You now have",bet)
                                elif single_roll_bet_option==6:
                                    if dice_rolled_in_round in [2,3,4,9,10,11,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*2,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                        else:
                            pass
                        
                        print("The number rolled by the shooter (for main Line bet) is",dice_rolled_in_round)
                        if dice_rolled_in_round in [7,11]:
                            print("The crowd cheers as the bettors who played for Don't Pass Line have won!")
                            print("You have won",bet_placed*2,'$. ',end='')
                            bet=bet+(bet_placed*2)
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round==comeout_roll:
                            print("The crowd moans as the bettors who played the Don't Pass Line have lost!")
                            print("You have lost",bet_placed,'$. ',end='')
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round in [2,3,4,5,6,8,9,10,12]:
                            print("The crowd waits in anticipation for the next roll")
                            continue

        elif ans_shooter_or_not=='n':
            print("The player now chooses if they want to bet on the:\n1. Pass Line\n2. Don't Pass Line")
            comeout_bet=int(input("Enter 1 or 2 depending on your betting choice: "))
            bet_placed=int(input("Enter amount you would like to bet (increments of 5$, min bet is 5$): "))
            bet=bet-bet_placed
            if comeout_bet==1:
                print("You are betting",bet_placed," on the Pass Line")
                print("The shooter is rolling the come-out roll!")
                comeout_roll=dice_roll()
                print("The shooter has rolled a",comeout_roll)
                if comeout_roll==7 or comeout_roll==11:
                    print("The crowd cheers as the come-out roll wins!")
                    print("You have won",bet_placed*3,'$. ',end='')
                    bet=bet+(bet_placed*3)
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        print()
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break

                elif comeout_roll in [2,3,12]:
                    print("The crowd boos as the come-out roll loses!")
                    print("You have lost",bet_placed,'$. ',end='')
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break
                elif comeout_roll in [4,5,6,8,9,10]:
                    print("The shooter's point is now",comeout_roll)
                    print("Now the aim of the game is for the shoooter to land point before he/she rolls a 7 OR 11")
                    c=1
                    while c>=1:
                        j=dice_roll()
                        dice_rolled_in_round=j
                        print()
                        ans_to_more_bets=input("Do you want to place a single roll bet? y/n: ")
                        if ans_to_more_bets=='y':
                            print("Choose any one single roll bet you would like to make: ")
                            print("1. Three (Ace Deuce)- Payout=15:1")
                            print("2. Any 7 (Big Red)- Payout=4:1")
                            print("3. Any Craps (Three way)- Payout=7:1")
                            print("4. Two Craps or Aces (Snake Eyes)- Payout=30:1")
                            print("5. Twelve Craps (Boxcars or Midnight)- Payout=30:1")
                            print("6. Field Bet- Payout=2:1")
                            single_roll_bet_option=int(input("Enter option number of whichever bet you prefer: "))
                            bet_placed_sr=int(input("Enter amount you would like to bet (increments of 5$, min bet is 5$): "))
                            bet=bet-bet_placed_sr
                            for i in range(1):
                                print("The number rolled by the shooter (for single roll bet) is ",dice_rolled_in_round)
                                if single_roll_bet_option==1:
                                    if dice_rolled_in_round==3:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*15,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==2:
                                    if dice_rolled_in_round==7:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*4,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==3:
                                    if dice_rolled_in_round in [2,3,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*7,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==4:
                                    if dice_rolled_in_round==2:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==5:
                                    if dice_rolled_in_round==12:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==6:
                                    if dice_rolled_in_round in [2,3,4,9,10,11,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*2,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                        else:
                            pass
                        
                        print("The number rolled by the shooter (for main Line bet) is",dice_rolled_in_round)
                        if dice_rolled_in_round in [7,11]:
                            print("The crowd moans as the bettors who played for Pass Line have lost!")
                            print("You have lost",bet_placed,'$. ',end='')
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round==comeout_roll:
                            print("The crowd bursts in cheers as the bettors who played the Pass Line have won!")
                            print("You have won",bet_placed*2,'$. ',end='')
                            bet=bet+(bet_placed*2)
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round in [2,3,4,5,6,8,9,10,12]:
                            print("The crowd waits in anticipation for the next roll")
                            continue
            if comeout_bet==2:
                print("You are betting",bet_placed," on the Don't Pass Line")
                print("The shooter is rolling the come-out roll!")
                comeout_roll=dice_roll()
                print("The shooter has rolled a",comeout_roll)
                if comeout_roll==7 or comeout_roll==11:
                    print("The crowd moans as the come-out roll loses!")
                    print("You have lost",bet_placed,'$. ',end='')
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        print()
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break
                elif comeout_roll in [2,3,12]:
                    print("The crowd cheers as the come-out roll wins!")
                    print("You have won",bet_placed*3,'$. ',end='')
                    bet=bet+(bet_placed*3)
                    print("You now have",bet,"$")
                    print("The round is now over")
                    ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                    if ans_to_repeat_round=='y':
                        continue
                    else:
                        print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                        break
                elif comeout_roll in [4,5,6,8,9,10]:
                    print("The shooter's point is now",comeout_roll)
                    print("Now the aim of the game is to land a 7 or 11 before the shooter lands his point")
                    c=1
                    while c>=1:
                        j=dice_roll()
                        dice_rolled_in_round=j
                        print()
                        ans_to_more_bets=input("Do you want to place a single roll bet? y/n: ")
                        if ans_to_more_bets=='y':
                            print("Choose any one single roll bet you would like to make: ")
                            print("1. Three (Ace Deuce)- Payout=15:1")
                            print("2. Any 7 (Big Red)- Payout=4:1")
                            print("3. Any Craps (Three way)- Payout=7:1")
                            print("4. Two Craps or Aces (Snake Eyes)- Payout=30:1")
                            print("5. Twelve Craps (Boxcars or Midnight)- Payout=30:1")
                            print("6. Field Bet- Payout=2:1")
                            single_roll_bet_option=int(input("Enter option number of whichever bet you prefer: "))
                            bet_placed_sr=int(input("Enter amount you would like to bet (increments of 5$, min bet is 5$): "))
                            bet=bet-bet_placed_sr
                            for i in range(1):
                                print("The number rolled by the shooter (for single roll bet) is ",dice_rolled_in_round)
                                if single_roll_bet_option==1:
                                    if dice_rolled_in_round==3:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*15,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==2:
                                    if dice_rolled_in_round==7:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*4,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==3:
                                    if dice_rolled_in_round in [2,3,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*7,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==4:
                                    if dice_rolled_in_round==2:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                        print("You now have",bet)
                                elif single_roll_bet_option==5:
                                    if dice_rolled_in_round==12:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*30,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                                elif single_roll_bet_option==6:
                                    if dice_rolled_in_round in [2,3,4,9,10,11,12]:
                                        print("You have won this single roll bet! Congrats")
                                        print("You have won",bet_placed_sr*2,'$. ',end='')
                                        bet=bet+bet_placed_sr
                                        print("You now have",bet)
                                    else:
                                        print("You have lost this single roll bet!")
                                        print("You have lost",bet_placed_sr,'$. ',end='')
                        else:
                            pass
                        
                        print("The number rolled by the shooter (for main Line bet) is",dice_rolled_in_round)
                        if dice_rolled_in_round in [7,11]:
                            print("The crowd cheers as the bettors who played for Don't Pass Line have won!")
                            print("You have won",bet_placed*2,'$. ',end='')
                            bet=bet+(bet_placed*2)
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round==comeout_roll:
                            print("The crowd moans as the bettors who played the Don't Pass Line have lost!")
                            print("You have lost",bet_placed,'$. ',end='')
                            print("You now have",bet,"$")
                            print("The round is now over")
                            ans_to_repeat_round=input("Would you like to play another round? y/n: ")
                            if ans_to_repeat_round=='y':
                                print()
                                break
                            else:
                                print("Thank you for playing. The total money you are leaving with is",bet,". Goodbye!")
                                return(bet)
                        elif dice_rolled_in_round in [2,3,4,5,6,8,9,10,12]:
                            print("The crowd waits in anticipation for the next roll")
                            continue



def input_bet():        #function to place bet
    global plyr_mny
    while True:
        try:
            print()
            x=int(input("how much are you betting for this game?"))
            if x<=plyr_mny and x>0:
                break
            else:
                plyr_mny=int(1/0)
        except:
            print()
            print("INVALID VALUE. Please enter a positive integer value that is less than or equal to ",plyr_mny,'\n')
    plyr_mny-=x
    return(x)

def hit(li,ten,player_card,player_carddis): #blackjack function
    li=[1,2,3,4,5,6,7,8,9,10]
    ten=[10,'King','Queen','Jack','Ace']
    import random
    cards=random.choice(li)
    if cards==10:
        num=random.choice(ten)
        player_carddis.append(num)
        player_card.append(10)                  #1 should be represented as an ace
    else:
        player_card.append(cards)
        player_carddis.append(cards)
    print('your cards are :-')
    for i in player_carddis:
        print('|',i,end=' |')
    print()
    print()


def wingame():                                  #blackjack function
    print()
    print('You have won the game')
    print()
    winfile=open('win.txt','r')
    lines=winfile.read()
    print(lines)
    winfile.close()
    print()
    

def losegame():                               #blackjack function
    print()
    print('The dealer has won the game')
    print()
    print()
    losefile=open('lose.txt','r')
    lines=losefile.read()
    print(lines)
    losefile.close()
    print()
    

def drawgame():                             #blackjack function
    print()
    print('The game is a draw')
    print()
    drawfile=open('draw.txt','r')
    lines=drawfile.read()
    print(lines)
    drawfile.close()
    print()
    

def maingame(bet):      #blackjack function
    
    #Prints the rules
    rulz=open('rules.txt','r')
    sent=rulz.read()
    print(sent)
    rulz.close()
    print()
    print()

    dealamt=random.choice([10000,12000,15000,4000,7000,9000,13000,14000,16000,17000,18000,19000,20000])
    print()
    print('The Dealer has bet Rs.',dealamt)
    print()

    player_card=[]
    player_carddis=[]
    li=[1,2,3,4,5,6,7,8,9,10]
    ten=[10,'King','Queen','Jack','Ace']
    for i in range(2):
        
        cards=random.choice(li)
        if cards==10:
            num=random.choice(ten)
            player_carddis.append(num)
            player_card.append(10)
        else:
            player_card.append(cards)
            player_carddis.append(cards)
    print('Your cards are:-')
    for i in player_carddis:
        print('|',i,end=' |')
    #The main menu driven program
    op='opt'
    gamesum=0
    while op!=2:
        print('''
        You have three options which are
        1)Hit
        2)Stay
                ''')
        op=int(input("Enter the option number:-" ))

        
        if op==1:
            gamesum=0
            hit(li,ten,player_card,player_carddis)
            length=len(player_card)
            for i in range(0,length):
                gamesum+=player_card[i]
            if gamesum==21:
                break
            if gamesum>21:
                break
        elif op==2:
            break
        else:
            print()
            print('!!!INVALID OPTION!!!')
            
    print("Staying!!!") 
    print()       
    sum1=0
    length=len(player_card)
    for i in range(0,length):
        sum1+=player_card[i]
    print('The sum of your original cards is:- ',sum1)
    print()

    sum2=random.choice([16,17,18,19,20,21,22,23,24,25,26])
    print('The total of dealers card is:- ',sum2)
    print()
    lose=0
    win=0
    draw=0
    if sum1>21 and sum2>21:
        draw=1
    if sum1<=21 and sum2>21:
        win=1
    if sum1<=21 and sum2<21:
        lose=1
    if sum1>21 and sum2<=21:
        lose=1
    if sum1<21 and sum2<21:
        if sum1>sum2:
            win=1
        if sum1==sum2:
            draw=1
        if sum1<sum2:
            lose=1
    if draw==1:
        print()
        result=bet
        print('YOU DID NOT LOSE ANY MONEY')
        print()
        return result
    if win==1:
        wingame()
        print()
        print('YOU HAVE GAINED RS.',bet+dealamt)
        result=bet+dealamt
        print()
        return result
    if lose==1:
         losegame()
         print('YOU HAVE LOST RS.',bet)
         result=0
         print()
         print()
         return result


def slotmachine(bet):
    
    #printing rules
    
    prizes=open("explanation.txt")
    for i in prizes:
        print(i,end='')
        time.sleep(1)
    prizes.close()

    #spinning slot machine
    
    print("time to spin the slot machine")
    print()
    ml=['( )','777','###','@.@','.!.','O.O','|||','<$>','^_^']
    r1=[];r2=[];r3=[]
    for i in range(3):
        r1.append(random.choice(ml))
        r2.append(random.choice(ml))
        r3.append(random.choice(ml))

    #printing slot machine
        
    time.sleep(1)
    print('|  ',end='')
    for i in r1:
        print(i,'  |  ',end='')
    time.sleep(1)
    print()
    print()
    print('|  ',end='')
    for i in r2:
        print(i,'  |  ',end='')
    time.sleep(1)
    print()
    print()
    print('|  ',end='')
    for i in r3:
        print(i,'  |  ',end='')
    print()
    print()
    
    #checking win conditions row +200 col +300 cross +500 all +1000
    
    print('CHECKING FOR WIN CONDITIONS...')
    print()
    time.sleep(2)
    win=False
    allwin=True

    #row wins
    
    if r1[0]==r1[1]==r1[2]:
        bet+=100
        win=True
    else:
        allwin=False
    if r2[0]==r2[1]==r2[2]:
        bet+=100
        win=True
    else:
        allwin=False
    if r3[0]==r3[1]==r3[2]:
        bet+=100
        win=True
    else:
        allwin=False
        
    #column wins
        
    if r1[0]==r2[0]==r3[0]:
        bet+=200
        win=True
    if r1[1]==r2[1]==r3[1]:
        bet+=200
        win=True
    if r1[2]==r2[2]==r3[2]:
        bet+=200
        win=True
        
    #cross wins
        
    if r1[0]==r2[1]==r3[2]:
        bet+=500
        win=True
    if r1[2]==r2[1]==r3[0]:
        bet+=500
        win=True
    if allwin:
        bet+=1000

    if win==False:
        bet=0
        
    #returning money
        
    if win==True:
        print('YOU HAVE WON ',bet,' FROM THE SLOT MACHINE (ᵔᴥᵔ)')
    else:
        print("YOU LOSE. BETTER LUCK NEXT TIME")
    return bet

#MAIN PROGRAM

#setting up mysql table

while True:
    try:
        p123=input("Enter your mysql password.")
        conn=cn.connect(host='localhost',user='root',password=p123,database='')
        break
    except:
        print("The password entered is incorrect")
cur=conn.cursor()
try:
    cur.execute('create database if not exists casino;')
    cur.execute("use casino;") 
    cur.execute('create table if not exists playerdata(NAME varchar(30) primary key,MONEY int);')
    conn.commit()
except:
    conn=cn.connect(host='localhost',user='root',password='mysql',database='casino')
    cur=conn.cursor()

print("WELCOME TO THE CASINO",'\n')
time.sleep(1)

#player introduction

plyr_nam=input("What is your name?").upper()
time.sleep(1)
while True:
    try:
        print()
        plyr_mny=int(input("How much money do you want to convert to chips?"))
        if plyr_mny>=0:
            break
        else:
            plyr_mny=int(1/0)
    except:
        print("INVALID VALUE. Please enter a positive integer value",'\n')
print()
st="select * from playerdata where name='"+plyr_nam+"';"
cur.execute(st)
if cur.fetchall()==[]:
    time.sleep(1)
    print('Ahh a new player. We appreciate your visit','\n')
    time.sleep(1)
    cur.execute("insert into playerdata values('"+plyr_nam+"',"+str(plyr_mny)+");")
    conn.commit()
else:
    time.sleep(1)
    print("Ahh welcome back. We've missed you",'\n')
    time.sleep(1)
    cur.execute("update playerdata set money="+str(plyr_mny)+" where name='"+plyr_nam+"';")
    conn.commit()

#menu driven game selection
    
mnu='bruh'
while mnu!=4:
    while True: #error handling block 
        try:
            mnu=int(input("""What do you wanna play?

Enter 1-Blackjack
      2-Slot Machine
      3-Craps Table
      4-Exit the Casino"""))
            if mnu==1 or mnu==2 or mnu==3 or mnu==4:
                break
            else:
                mnu=int(1/0)
        except:
            print("INVALID VALUE. Please a valid option number",'\n')
    if mnu==1:
        amt_won=maingame(input_bet())
        plyr_mny+=amt_won
        cur.execute("update playerdata set money="+str(plyr_mny)+" where name='"+plyr_nam+"';")
        conn.commit()
    elif mnu==2:
        amt_won=slotmachine(input_bet())
        plyr_mny+=amt_won
        cur.execute("update playerdata set money="+str(plyr_mny)+" where name='"+plyr_nam+"';")
        conn.commit()
    elif mnu==3:
        print("Welcome to Craps, the game based on probability and the luck of a dice throw")
        print("This game unites all those taking part in it, because the goal is common and is achieved in the same manner by everyone.")
        print("The goal being making money!")
        print()
        instruct=input("Do you want to see the instructions on how to play the game? y/n: ")
        if instruct=='y':
            prizes=open("craps_instruct.txt")
            for i in prizes:
                print(i,end='')
                time.sleep(1)
            prizes.close()
            print()
        else: 
            print("Let's get on with the game then shall we!\n")
        amt_won=craps(input_bet())
        plyr_mny+=amt_won
        cur.execute("update playerdata set money="+str(plyr_mny)+" where name='"+plyr_nam+"';")
        conn.commit()
    elif mnu==4:
        print("You're leaving. . .  :(")
        print("Here's some player statistics before you leave",'\n')

        #matplotlib usage
        
        time.sleep(3)
        cur.execute("select * from playerdata;")
        plyrnms=[]
        plyrmny=[]
        for i in cur.fetchall():
            plyrnms+=[i[0]]
            plyrmny+=[i[1]]
        plt.bar(plyrnms,plyrmny,color='red')
        plt.xlabel("PLAYER NAME")
        plt.ylabel("PLAYER WORTH")
        plt.title("PLAYER STATISTICS")
        plt.show()
        print("Hope you visit again")
        sys.exit(0)
        
