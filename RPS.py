#library
from colorama import Fore
import random
import os
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



#computer with user
def computer_user():
	userName = input(Fore.WHITE+"Please enter your name: ").lower()
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
	else:
		print(Fore.RED+"[!] please enter the correct option! ! !")
		exit()
	
def user_with_user():
	userName1 = input("Please enter your name player one: ")
	userName2 = input("Please enter your name player two: ")
	os.system("clear" or "cls")
	print(f"player 1 =>> {userName1}\nplayer 2 =>>{userName2}")


banner()

computer_user()
