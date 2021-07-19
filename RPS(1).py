#library
from colorama import Fore
import random
import os
import sys
#---------------------------------------
#banner and first for start the program
def banner():
	print(Fore.CYAN+"""

██████╗ ██████╗ ███████╗            
██╔══██╗██╔══██╗██╔════╝            
██████╔╝██████╔╝███████╗            
██╔══██╗██╔═══╝ ╚════██║            
██║  ██║██║     ███████║            
╚═╝  ╚═╝╚═╝     ╚══════╝""")
	print(Fore.GREEN+"""

 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                    

    """)
	print(Fore.GREEN+"=================================================")
	print(Fore.YELLOW+">>>"+Fore.RED+"Welcome to : "+Fore.CYAN+"RPS GAME")
	print(Fore.YELLOW+">>>"+Fore.RED+"Coded by: "+Fore.CYAN+"Emad")
	print(Fore.YELLOW+">>>"+Fore.RED+"My Github: "+Fore.CYAN+"https://github.com/EmadOldin/")
	print(Fore.GREEN+"=================================================")
#clear
def clear():
	type_of_runner = os.name
	if type_of_runner == 'nt':
		os.system("cls")
	else:
		os.system("clear")



#computer with user
def computer_user():
	userName = input(Fore.WHITE+"Please enter your name: ").upper()
	userRound = int(input(Fore.WHITE+"[?] How many round do you want play? : "))
	for i in range(1 , userRound+1):
		userChoice = input(Fore.WHITE+"[?] enter your choice :  ")
		while userChoice != "rock" and userChoice != "paper" and userChoice != "scissors":
			print(Fore.RED+"[!] please enter the true option! ! !")
			userChoice = input(Fore.WHITE+"[?] enter your choice :  ").lower()

		computerChoice = ""
		userPoint = 0
		computerPoint = 0
		#system selec
		computerChoice_num = random.randint(1,3)
		if computerChoice_num == 1:
			computerChoice = "rock"
		elif computerChoice_num == 2:
			computerChoice = "paper"
		elif computerChoice_num == 3:
			computerChoice = "scissors"
		#game code for computer and user
		#drew
		if userChoice == computerChoice:
			print(Fore.BLUE+"[=] The game doesn't have any winner! ! !")
		#The user choice is paper	
		elif userChoice == "paper":
			if computerChoice == "rock":
				print(Fore.WHITE+f"[#] You selected {userChoice}\n[#] The computer selected {computerChoice}\n"+Fore.GREEN+"[+] You won this round!\n"+Fore.RED+"[-] Computer lost this round!")
				userPoint += 1 
			elif computerChoice == "scissors":
				print(Fore.WHITE+f"[#] You selected {userChoice}\n[#] The computer selected {computerChoice}\n"+Fore.RED+"[-] You lost this round!\n"+Fore.GREEN+"[+] Computer won this round!")			
				computerPoint += 1
		#The user choice is scissors	
		elif userChoice == "scissors":
			if computerChoice == "paper":
				print(Fore.WHITE+f"[#] You selected {userChoice}\n[#] The computer selected {computerChoice}\n"+Fore.GREEN+"[+] You won this round!\n"+Fore.RED+"[-] Computer lost this round!")
				userPoint += 1 
			elif computerChoice == "rock":
				print(Fore.WHITE+f"[#] You selected {userChoice}\n[#] The computer selected {computerChoice}\n"+Fore.RED+"[-] You lost this round!\n"+Fore.GREEN+"[+] Computer won this round!")
				computerPoint += 1
		##The user choice is scissors
		elif userChoice == "rock":
			if computerChoice == "scissors":
				print(Fore.WHITE+f"[#] You selected {userChoice}\n[#] The computer selected {computerChoice}\n"+Fore.GREEN+"[+] You won this round!\n"+Fore.RED+"[-] Computer lost this round!")
				userPoint += 1 
			elif computerChoice == "paper":
				print(Fore.WHITE+f"[#] You selected {userChoice}\n[#] The computer selected {computerChoice}\n"+Fore.RED+"[-] You lost this round!\n"+Fore.GREEN+"[+] Computer won this round!")
				computerPoint += 1
		# os.system("cls" or "clear")
	type_of_runner = os.name
	if type_of_runner == 'nt':
		os.system("cls")
	else:
		os.system("clear")
	print(f"[+]Your point => {userPoint}\n[+] Computer point => {computerPoint}")
	if userPoint > computerPoint :
		print(Fore.GREEN+"[+] You are the winner ! ! !\n"+Fore.RED+"[-] Comper is the loser ! ! !")
	elif userPoint < computerPoint :
		print(Fore.RED+"[-] You are the loser ! ! !\n"+Fore.GREEN+"[+] Comper is the winner ! ! !")
		

#user with user
def user_with_user():
	userPoint1 = 0
	userPoint2 = 0
	userName1 = input(Fore.WHITE+"Please enter your name player one: ").upper()
	userName2 = input(Fore.WHITE+"Please enter your name player two: ").upper()
	userRound = int(input(Fore.WHITE+"[?] How many rounds do you want play? : "))
	# os.system("clear" or "cls")
	type_of_runner = os.name
	if type_of_runner == 'nt':
		os.system("cls")
	else:
		os.system("clear")
	print(f"player 1 =>> {userName1}\nplayer 2 =>>{userName2}")
	for i in range(1 , userRound+1):
		userChoice1 = input(Fore.WHITE+"[?] player 1: enter your choice: ").lower()
		while userChoice1 != "rock" and userChoice1 != "paper" and userChoice1 != "scissors":
			print(Fore.RED+"[!] please enter the true option! ! !")
			userChoice1 = input(Fore.WHITE+"[?] player 1: enter your choice: ")
		userChoice2 = input(Fore.WHITE+"[?] player 2: enter your choice: ").lower()
		while userChoice2 != "rock" and userChoice2 != "paper" and userChoice2 != "scissors":
			print(Fore.RED+"[!] please enter the true option! ! !")
			userChoice2 = input(Fore.WHITE+"[?] player 2: enter your choice: ")
		#drew
		if userChoice1 == userChoice2:
			print(Fore.BLUE+"[=] The game doesn't have any winner ! ! !")
		#the player one choice rock
		elif userChoice1 == "rock":
			if userChoice2 == "paper":
				print(Fore.WHITE+f"[#] {userName1} = You selected ROCK\n[#] {userName2} = You selected PAPER\n"+Fore.RED+f"[-] {userName1} lost this round!\n"+Fore.GREEN+f"[+] {userName2} won this round!")
				userPoint2 += 1
			elif userChoice2 == "scissors":
				print(Fore.WHITE+f"[#] {userName1} = You selected ROCK\n[#] {userName2} = You selected SCISSORS\n"+Fore.GREEN+f"[+] {userName1} won this round!\n"+Fore.RED+f"[-] {userName2} lost this round!")
				userPoint1 += 1
		#the player one choice paper
		elif userChoice1 == "paper":
			if userChoice2 == "scissors":
				print(Fore.WHITE+f"[#] {userName1} = You selected PAPER\n[#] {userName2} = You selected SCISSORS\n"+Fore.RED+f"[-] {userName1} lost this round!\n"+Fore.GREEN+f"[+] {userName2} won this round!")
				userPoint2 += 1
			elif userChoice2 == "rock":
				print(Fore.WHITE+f"[#] {userName1} = You selected PAPER\n[#] {userName2} = You selected ROCK\n"+Fore.GREEN+f"[+] {userName1} won this round!\n"+Fore.RED+f"[-] {userName2} lost this round!")
				userPoint1 += 1
		#the player one choice scissors
		elif userChoice1 == "scissors":
			if userChoice2 == "rock":
				print(Fore.WHITE+f"[#] {userName1} = You selected SCISSORS\n[#] {userName2} = You selected ROCK\n"+Fore.RED+f"[-] {userName1} lost this round!\n"+Fore.GREEN+f"[+] {userName2} won this round!")
				userPoint2 += 1
			elif userChoice2 == "paper":
				print(Fore.WHITE+f"[#] {userName1} = You selected SCISSORS\n[#] {userName2} = You selected PAPER\n"+Fore.GREEN+f"[+] {userName1} won this round!\n"+Fore.RED+f"[-] {userName2} lost this round!")
				userPoint1 += 1
	
	# winner color green and loser color red
	if userPoint1 > userPoint2:
		print(Fore.CYAN+f"Finally points:")
		print(Fore.GREEN+f"{userName1}::::Your Point is::::{userPoint1}")
		print(Fore.RED+f"{userName2}::::Your Point is::::{userPoint2}")
	if userPoint1 < userPoint2:
		print(Fore.CYAN+f"Finally points:")
		print(Fore.RED+f"{userName1}::::Your Point is::::{userPoint1}")
		print(Fore.GREEN+f"{userName2}::::Your Point is::::{userPoint2}")


#run
banner()
print(Fore.YELLOW+"[1]"+Fore.CYAN+" Start")
print(Fore.YELLOW+"[2]"+Fore.CYAN+" Exit")
print(Fore.YELLOW+"[3]"+Fore.CYAN+" Help")
choice = int(input(Fore.WHITE+"[?] Choice one option: "))
clear()
banner()
#start
if choice == 1 :
	print(Fore.YELLOW+">>>"+Fore.GREEN+" [1] computer && user")
	print(Fore.YELLOW+">>>"+Fore.GREEN+" [2] user && user")
	choice = int(input(Fore.WHITE+"[?] Choice one option: "))
	if choice == 1:
		clear()
		banner()
		computer_user()
	elif choice == 2 :
		clear()
		banner()
		user_with_user()
#exit
if choice == 2:
	clear()
	banner()
	print(Fore.GREEN+"Thank you for choice us ! ! !")	
	sys.exit()
#help
if choice == 3:
	clear()
	banner()
	print(Fore.YELLOW+"You should choice between this option :")
	print(Fore.GREEN+"Rock , Paper , Scissors")
