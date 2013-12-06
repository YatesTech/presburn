import sys, os



def news():
	#News Headline
	print (" \n News ")
	#Actual News
	print (" \n ")
	print ("RIP M. Mandela. You will never be forgotten.     ")
	
def citizenship():
	#info
	
	#breaking the two spaces
	print (" \n ")
	#start info
	print ("Want citizenship? \n To get citizenship, go to our website at http://www.presburn.tk/ \n")
	#IRC info
	print ("To get in contact with us, go to our IRC channel on freenode: #presburn. \n")
def help():
	print ("Welome to the help menu! For news, type the letter 'n'. For Info on citizenship, \n type in the  letter 'c'. For this message, type in the letter 'h'. Remember, at the end of this message, \n you'll have to relaunch the program with './launcher.sh' if you're on linux.") 

print ("Welcome to the Presburn Information Centre! \n Type a command to continue (h for help) \n ")
command = raw_input("user@presburnapp:~$ ")
if command == 'h':
	print(help())	
if command == 'n':
	print(news())
if command == 'c':
	print(citizenship())
command = raw_input("user@presburnapp:~$ ")

if command == 'h':
        print(help())
if command == 'n':
        print(news())
if command == 'c':
        print(citizenship())


command = raw_input("user@presburnapp:~$ ")
if command == 'h':
        print(help())
if command == 'n':
        print(news())
if command == 'c':
        print(citizenship())

