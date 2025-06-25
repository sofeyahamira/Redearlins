## imports 
import sys
import time
from colorama import Fore, Style
import os
import random

# clear function
def clear():
     os.system('clear')

# write function

def write(write):
    # Repeats for each letter.
    for i in write:
        # sys.stdout.write doesn't create a new line for each write
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)
    # Do you want to continue to the next text?
    next = input()

#variables
name = ''
attack = 0
defense = 0
stamina = 10
ending = []

# intro

write('Welcome to Redearlins')
write("A city, known for fierce battles.")
write("Each month,")
write("a prize of $10,000 is given to the last person standing in the circle")
write("and the rest lose.")
time.sleep(.5)
print("""
█▀█ █▀▀ █▀▄ █▀▀ ▄▀█ █▀█ █░░ █ █▄░█ █▀
█▀▄ ██▄ █▄▀ ██▄ █▀█ █▀▄ █▄▄ █ █░▀█ ▄█
""")
time.sleep(.5)
input(f"{Fore.RED}Press ENTER to continue{Fore.RESET}")
clear()

# check-in
print("""
█▀▀ █░█ █▀▀ █▀▀ █▄▀ ▄▄ █ █▄░█
█▄▄ █▀█ ██▄ █▄▄ █░█ ░░ █ █░▀█
""")
write("You: I came to this event, in order to pay my debt")
write("You: My home was taken from me by outlawed men named: The Baayls")
write("Clerk: I asked for your name, not your backstory.")
write("You: Oh yeah, right, my name is...")

name = input("What's your name?\n> ")

write(f"Clerk: Thank you {name}.")
write("I have registered you into the database.")
write("Have fun, and don't lose.")
write("You (whispering): Right, I'm sure you say that to everyone")
clear()

#room
print("""
█▀█ █▀█ █▀█ █▀▄▀█
█▀▄ █▄█ █▄█ █░▀░█
""")
write("You: Tomorow's a big day")
write("I should read this intoductory manual the check-in clerck gave me.")
write(f"{Style.BRIGHT}Manual: Welcome Player to The Readearlins Tournament!")
write("There are 3 areas you must travel in order to recive the grand prize of $10,000.")
write(f"Eliminate as many playes as possible and survive till the end.\n{Style.RESET_ALL}")

write("You: This match is no joke.")
input(f"{Style.BRIGHT}1. I should train hard\n2. I hope luck favours me\n> {Style.RESET_ALL}")
write("The manual says: ")
write("'Report to the player lounge at noon,")
write("to meet the other players and also to get gear.'")
write("Looks like I know what I'll be doing.")
clear()

#lounge
print("""
█░░ █▀█ █░█ █▄░█ █▀▀ █▀▀
█▄▄ █▄█ █▄█ █░▀█ █▄█ ██▄
""")
write("You: So this is lounge")
write("Hey everyone")
write(f"{Style.DIM}Everyone looks at you.{Style.RESET_ALL}")
write("You (whispering): Why's everyone so gloomy?")
write(f"{Fore.LIGHTRED_EX}???: Hello and Welcome players!")
write("My name is Hector, I'm the host of The Readearlins Tournament.")
write("I assume you have all read the manual and are well aquainted with the rules.")
write("That said, the tournament starts tomorow at 8:00 AM sharp.")
write("Don't be late or you will risk disqualification.")
write(f"You can each pick a weapon from this table.{Fore.RESET}")
write(f"{Style.DIM}Hector gestures at a table layered with weapons{Style.RESET_ALL}")
write(f"{Fore.LIGHTRED_EX}Your names will be drawn from this hat.")
write(f"Once you here your name, feel free to take whatever weapon is left.{Fore.RESET}")
write(f"{Style.DIM}Hector starts calling names{Style.RESET_ALL}")
write(f"{Fore.LIGHTRED_EX}...{name}! Pick from these 3 weapons...{Fore.RESET}")
write(f"{Style.BRIGHT}1. Hatchet\n2. Sword\n3. Gun \n(Press ENTER to choose){Style.BRIGHT}")

weapon = input('> ')
if weapon == '1':
  weapon = 'Hatchet'
  attack += 10
elif weapon == '2':
  weapon = 'Sword'
  attack += 15
elif weapon == '3':
  weapon = 'Gun'
  attack += 20 
else:
  weapon = 'Hatchet'
  attack += 10

write(f"{Style.BRIGHT}Obtained {weapon}{Style.RESET_ALL}")
write(f"{Fore.LIGHTRED_EX}Hector: That is the only thing we will be giving to you.")
write("You may collect armour during the Tournament.")
write(f"I wish you all the best. And... Don't lose.{Fore.RESET}")
clear()

#room 2
print("""
█▀█ █▀█ █▀█ █▀▄▀█
█▀▄ █▄█ █▄█ █░▀░█
""")
write("You: Alright, time to come up with a strategy.")
write("My first move is to... ")
write(f"{Style.BRIGHT}1. Get armour\n2. Attack \n(Press ENTER to choose){Style.RESET_ALL}")

first_move = input('> ')
if first_move == '1':
  write("Right, my first move is to get armour")
elif first_move == '2':
  write("Right, my first move is to attack")
else:
  write("Right, my first move is to get armour")

write("Well, it's getting late.")
write("I need a lot of sleep for tomororw.")
write("Less sleep causes reaction times to decrease after all...")
write(f"{Fore.RED}Press ENTER to go to sleep{Fore.RESET}")
clear()
time.sleep(1)

write(f"{Style.DIM}Your Alarm is ringing{Style.RESET_ALL}")
write(f"{Fore.RED}Press ENTER to switch it off{Fore.RESET}")
write("You: Today's the day...")
write("I win this tournament...")
write("And reclaim what was taken from me...")
clear()

#tournament area 1
print("""
▀█▀ █▀█ █░█ █▀█ █▄░█ ▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   ▄▀█ █▀█ █▀▀ ▄▀█   ▄█
░█░ █▄█ █▄█ █▀▄ █░▀█ █▀█ █░▀░█ ██▄ █░▀█ ░█░   █▀█ █▀▄ ██▄ █▀█   ░█
""")
write(f"{Fore.LIGHTRED_EX}Hector: Welcome everyone to the Readearlins Tournament!{Fore.RESET}")
write(f"{Style.DIM}The crowd starts cheering{Style.RESET_ALL}")
write(f"{Fore.LIGHTRED_EX}Hector: Dear Players, You may start in 3...")
write("2...")
write("1...")
write(f"GO{Fore.RESET}")
write(f"{Style.DIM}Everyone starts running, you do so as well{Style.RESET_ALL}")
write("You: Alright time to execute my plan")

if first_move == '1':
  write("There! Armour!")
  write(f"{Style.BRIGHT}Obtained Leather Armour{Style.RESET_ALL}")
  defense =+ 5
  write("Alright, let's attack now")
  write("You (whispering): There's someone")
  write("Goodbye, player.")
  write(f"{Style.BRIGHT}Player 7 has been eliminated")
  write("Your Player Rank (PR) has increased by one")
  player_rank =+ 1
  write(f"Eliminate more players to increase your rank{Style.RESET_ALL}")
  
elif first_move == '2':
  write("You (whispering): There's someone")
  write("Goodbye, player.")
  write(f"{Style.BRIGHT}Player 7 has been eliminated")
  write("Your Player Rank (PR) has increased by one")
  player_rank =+ 1
  write(f"Eliminate more players to increase your rank{Style.RESET_ALL}")
  
write("You: Time to advance to the next area...")
clear()

#tournament area 2
print("""
▀█▀ █▀█ █░█ █▀█ █▄░█ ▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   ▄▀█ █▀█ █▀▀ ▄▀█   ▀█
░█░ █▄█ █▄█ █▀▄ █░▀█ █▀█ █░▀░█ ██▄ █░▀█ ░█░   █▀█ █▀▄ ██▄ █▀█   █▄
""")
write("You: Time to look for my next target.")
write(f"{Style.DIM}You here footsteps behind you...{Style.RESET_ALL}")
write("You: Who's there?")
write(f"{Style.DIM}You turn around and are faced with a sword{Style.RESET_ALL}")
write("You: Oh no.")
write(f"{Style.DIM}You close your eyes, ready for defeat when you here the sound of swords clashing{Style.RESET_ALL}")
write(f"{Fore.LIGHTBLUE_EX}???: Not so fast, let me end you first!{Fore.RESET}")
write(f"{Style.DIM}You watch as player 6 eleminates player 5{Style.RESET_ALL}")
write("You (whispering): Woah that guy's awesome!")
write("Wait, he's gonna attack me next!")
write(f"{Fore.LIGHTBLUE_EX}Hold on, I saved you, now you must help me.{Fore.RESET}")
write("You: Why would I do that?")
write(f"{Fore.LIGHTBLUE_EX}If not, I'll elemenate you too.{Fore.RESET}")

write(f"{Style.BRIGHT}1. Fight him\n2. Help him\nPress ENTER to choose{Style.RESET_ALL}")

choice = input("> ")
if choice == '1':
  write("You: I'd like to see you try.")
  write(f"{Fore.RED}{name} Challenged player 6 to a battle!{Fore.RESET}")
  hit_chance = random.randint(1,3)
  if hit_chance < 3:
    write(f"{Style.BRIGHT}{name} has eleminated player 6")
    write(f"Your PR has been increased by 1{Style.RESET_ALL}")
    player_rank =+ 1
    player_joined_player6 = False
    
  else:
    player_joined_player6 = True
    write("You missed!")
    write(f"{Fore.LIGHTBLUE_EX}One more chance, join me, or say goodbye...{Fore.RESET}")
    write(f"{Style.DIM}You agreed to join{Style.RESET_ALL}")
    write(f"{Fore.LIGHTBLUE_EX}Great, all I need you to do is get rid of that guy, he's player 3{Fore.RESET}")
    write("You: Alright...")
    write(f"{Style.DIM}You attack player 3")
    write("You win!")
    write(f"Your PR has increased by one!{Style.RESET_ALL}")
    player_rank =+ 1
    write(f"{Fore.LIGHTBLUE_EX}Alright, thanks.{Fore.RESET}")
    write("You: Wait! Who are you? And why did you want to eliminate player 3?")
    write(f"{Style.DIM}Player 6 leaves, ignoring your questions{Style.RESET_ALL}")
    write("You: I have a bad feeling about him...")

else:
  player_joined_player6 = True
  write(f"{Style.DIM}You agreed to join{Style.RESET_ALL}")
  write(f"{Fore.LIGHTBLUE_EX}Great, all I need you to do is get rid of that guy, he's player 3{Fore.RESET}")
  write("You: Alright...")
  write(f"{Style.DIM}You attack player 3")
  write("You win!")
  write(f"Your PR has increased by one!{Style.RESET_ALL}")
  player_rank =+ 1
  write(f"{Fore.LIGHTBLUE_EX}Alright, thanks.{Fore.RESET}")
  write("You: Wait! Who are you? And why did you want to eliminate player 3?")
  write(f"{Style.DIM}Player 6 leaves, ignoring your questions{Style.RESET_ALL}")
  write("You: I have a bad feeling about him...")
  
write("You: Time to move to the next area...")
clear()

#final area
print("""
█▀▀ █ █▄░█ ▄▀█ █░░   ▄▀█ █▀█ █▀▀ ▄▀█
█▀░ █ █░▀█ █▀█ █▄▄   █▀█ █▀▄ ██▄ █▀█""")

write(f"{Style.BRIGHT}Players Left: 4{Style.RESET_ALL}")
write("You: Final round, I can try eliminating everyone or just wait around somewhere safe.")

choice = input(f"{Style.BRIGHT}1. Eliminate Everyone\n2. Hide\n> {Style.RESET_ALL}")

#first way
if choice == '1' and player_joined_player6 is False:
  write("You: Violence is key for this")
  write("Player...1")
  hit_chance = random.randint(1,3)
  if hit_chance == 1:
    write(f"{Style.BRIGHT}{name} has eliminated player 1")
    write(f"Your PR increased by 1{Style.RESET_ALL}")
    player_rank =+ 1
  else:
    write(f"{Style.BRIGHT}You missed!")
    write(f"{name} challenged player 1 to a battle!")
    write("Attacking...")
    write(f"{name}has eliminated player 1")
    write(f"Your PR has increased by 1{Style.RESET_ALL}")
    player_rank =+ 1

  #2nd victim
  write("Player 3 and 4...")
  hit_chance = random.randint(1,3)
  if hit_chance == 1:
    write(f"{Style.BRIGHT}{name} has eliminated player 3 and 4")
    write(f"Your PR increased by 2{Style.RESET_ALL}")
    player_rank =+ 2
  else:
    write(f"{Style.BRIGHT}You missed!")
    write(f"{name} challenged player 3 and 4 to a battle!")
    write("Attacking...")
    write(f"{name}has eliminated player 3 and 4")
    write(f"Your PR has increased by 2{Style.RESET_ALL}")
    player_rank =+ 2

    #winning
    write(f"{Fore.LIGHTRED_EX}Am I seeing things right?{name} Has single handedly taken out every player! Well done!{Fore.RESET}")
    ending.append("Elimination")

#2nd way
if choice == '2' and player_joined_player6 is False:
  write(f"{Style.DIM}You watch as the other players eliminate each other...{Style.RESET_ALL}")
  write("You: Those 2 are fightitng hard.")
  write("I'll battle the last person and win this game!")
  write(f"{Style.DIM}You watch as Player 4 eliminates Player 5.")
  write(f"Player 4 then falls from fatigue{Style.RESET_ALL}")
  write("You: Wait, that means...")
  write(f"{Fore.LIGHTRED_EX}While it seems as though everyone has been eliminated, we have a coward, hiding amogst the trees and fallen hero's. {name}! You have won, in a boring way.{Fore.RESET}")
  write("You: Who cares! I won!")
  ending.append("Boring.")

#dealing with player 6 being alive
#first way
if choice == '1' and player_joined_player6 is True:
  write("You: Violence is key for this")
  write("Player...1")
  hit_chance = random.randint(1,3)
  if hit_chance == 1:
    write(f"{Style.BRIGHT}{name} has eliminated player 1")
    write(f"Your PR increased by 1{Style.RESET_ALL}")
    player_rank =+ 1
  else:
    write(f"{Style.BRIGHT}You missed!")
    write(f"{name} challenged player 1 to a battle!")
    write("Attacking...")
    write(f"{name}has eliminated player 1")
    write(f"Your PR has increased by 1{Style.RESET_ALL}")
    player_rank =+ 1

  #2nd victim
  write("Player 4...")
  hit_chance = random.randint(1,3)
  if hit_chance == 1:
    write(f"{Style.BRIGHT}{name} has eliminated player 4")
    write(f"Your PR increased by 2{Style.RESET_ALL}")
    player_rank =+ 2
  else:
    write(f"{Style.BRIGHT}You missed!")
    write(f"{name} challenged player 4 to a battle!")
    write("Attacking...")
    write(f"{name}has eliminated player 4")
    write(f"Your PR has increased by 2{Style.RESET_ALL}")
    player_rank =+ 2

  write(f"{Fore.LIGHTBLUE_EX}Hey, it's you!")
  write("No way you took out everyone!")
  write(f"Well, that makes my job a lot easier{Fore.RESET}")
  write("You: Wait! Before we fight, ")
  write("Why did you make me eliminate player 3")
  write("Why didn't you do it yourself?")
  write(f"{Fore.LIGHTBLUE_EX}Because...")
  write("I promised him I wouldn't take him out")
  write("So I asked you to do it instead")
  write(f"He's a close friend...{Fore.RESET}")
  write("You: You're evil")
  write("Well guess what...")
  write("Maybe I am too.")
  write(f"{Style.DIM}You use your {weapon} to eliminate player 6 from behind!{Style.RESET_ALL}")
  write(f"{Fore.LIGHTBLUE_EX}Agh... Fair played...{Fore.RESET}")
  write(f"{Style.DIM}Player 6 falls...{Style.RESET_ALL}")

  #winning
  write(f"{Fore.LIGHTRED_EX}Am I seeing things right?{name} Has single handedly taken out every player! Well done!{Fore.RESET}")
  ending.append("Honourably played")

#2nd way
if choice == '2' and player_joined_player6 is True:
  write(f"{Style.DIM}You watch as the other players eliminate each other...{Style.RESET_ALL}")
  write("You: Those 2 are fightitng hard.")
  write("I'll battle the last person and win this game!")
  write(f"{Style.DIM}You watch as Player 4 eliminates player 3.")
  write(f"Player 4 then falls from fatigue{Style.RESET_ALL}")
  write("You: Wait, that means...")
  write(f"{Fore.LIGHTBLUE_EX}You thought you won huh?{Fore.RESET}")
  write("You: Oh, it's you")
  write(f"{Fore.LIGHTBLUE_EX}Coward, which means taking you out should be easy.{Fore.RESET}")
  write("You: Wait! Before we fight, ")
  write("Why did you make me eliminate player 3")
  write("Why didn't you do it yourself?")
  write(f"{Fore.LIGHTBLUE_EX}Because...")
  write("I promised him I wouldn't take him out")
  write("So I asked you to do it instead")
  write(f"He's a close friend...{Fore.RESET}")
  write("You: You're evil")
  write("Well guess what...")
  write("Maybe I am too.")
  write(f"{Style.DIM}You use your {weapon} to eliminate player 6 from behind!{Style.RESET_ALL}")
  write(f"{Fore.LIGHTBLUE_EX}Agh... Fair played...{Fore.RESET}")
  write(f"{Style.DIM}Player 6 falls...{Style.RESET_ALL}")
  
  #win
  write(f"{Fore.LIGHTRED_EX}What an intresting battle! {name}! Congratulations on winning the tournament!.{Fore.RESET}")
  ending.append("I know you're a coward")

clear()

#wiiners hall
print("""
█░█░█ █ █▄░█ █▄░█ █▀▀ █▀█ █▀   █░█ ▄▀█ █░░ █░░
▀▄▀▄▀ █ █░▀█ █░▀█ ██▄ █▀▄ ▄█   █▀█ █▀█ █▄▄ █▄▄
""")
write(f"{Fore.LIGHTRED_EX}Congratulations {name}! As promised, Here is your check{Fore.RESET}")
write("You: Time to secure my home...")

write(f"{Style.BRIGHT}You won!")
write(f"Your PR is: {player_rank}")
write("Ending Obtained:")
print(ending[0])
write("Play Again to Unlock Diffrent Endings!")
write("List of Achievements: ")
print("""
Elimination: Rare
Boring.: Rare
Honourably played: Common
Coward!: Common
""")