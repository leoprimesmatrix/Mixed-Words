import random
import time
import colorama
from colorama import Fore,Back,Style
import os
os.system("")

colorama.init()

class game():
    def main_game(self):
        self.SELECT_WORD = random.choice(self.WORD_LIST)
        self.SCAMBLED_WORD = ''.join(random.sample(self.SELECT_WORD, len(self.SELECT_WORD)))
        self.PRINT(self.BLUE + f"Your scrambled word is: {self.SCAMBLED_WORD}")
        self.GAME_INPUT = self.USER_INPUT("Enter your guess: ")
        if self.GAME_INPUT.lower() == self.SELECT_WORD.lower():
            self.PLAY_AGAIN_INPUT = ""
            while self.PLAY_AGAIN_INPUT != "y" and self.PLAY_AGAIN_INPUT != "n":
                self.PLAY_AGAIN_INPUT = self.USER_INPUT(self.GREEN + "GREAT JOB! You got it right! Play again (y/n)? ")

                if self.PLAY_AGAIN_INPUT == "y":
                    self.queue()
                    break

                if self.PLAY_AGAIN_INPUT == "n":
                    self.DESCRIPTION = "Thanks for playing! Come back soon!"
                    self.PRINT(self.RED + self.DESCRIPTION)
                    exit()


        else:
            self.PRINT(self.RED + f"Dang it! You got it wrong. The correct word was {self.SELECT_WORD}")
            self.PLAY_AGAIN_INPUT = ""
            while self.PLAY_AGAIN_INPUT != "y" and self.PLAY_AGAIN_INPUT != "n":
                self.PLAY_AGAIN_INPUT = self.USER_INPUT(self.GREEN + "It was a nice try though. Mind playing again? (y/n) ")

                if self.PLAY_AGAIN_INPUT == "y":
                    self.queue()
                    break

                if self.PLAY_AGAIN_INPUT == "n":
                    self.DESCRIPTION = "Thanks for playing! Come back soon!"
                    self.PRINT(self.RED + self.DESCRIPTION)
                    exit()


    def queue(self):
        self.QUEUE_DESC1 = "Looking for match."
        self.QUEUE_DESC2 = "Looking for match.."
        self.QUEUE_DESC3 = "Looking for match..."
        self.QUEUE_FOUND = "Match found!"
        self.QUEUE_JOIN = "Joining Match!"
        self.COOLDOWN = 1
        self.QUEUE_SELECTED_DESCRIPTION = 1
        self.QUEUE_SEARCH_TIME = random.randint(1,5)
        self.QUEUE_FIND_CHANCE = random.randint(1,4)
        self.CAN_TELEPORT = False
        
        self.TRIES = 0
        
        while self.TRIES < 5:  # limit the number of attempts to find a match to 5
            #print(self.QUEUE_FIND_CHANCE)
            self.PRINT(self.BLUE + self.QUEUE_DESC1)
            self.WAIT(self.COOLDOWN)
            self.PRINT(self.BLUE + self.QUEUE_DESC2)
            self.WAIT(self.COOLDOWN)
            self.PRINT(self.BLUE + self.QUEUE_DESC3)
            self.WAIT(self.COOLDOWN)
            
            if self.QUEUE_FIND_CHANCE in [1, 2, 3]:
                self.DESCRIPTION = "Match found! Entering now."
                self.PRINT(self.YELLOW + self.DESCRIPTION)
                self.main_game()
                break
            else:
                self.TRIES = self.TRIES + 1
                self.DESCRIPTION = f"Failed finding match. Stand by! Attempt {self.TRIES}/5."
                self.PRINT(self.RED + self.DESCRIPTION)

        if self.TRIES == 5:
            self.DESCRIPTION = f"Failed to find match after {self.TRIES} attempts. Please re-open the file, if the problem persists, please contact PrimeDev#2349 on Discord."
            self.PRINT(self.RED + self.DESCRIPTION)
            exit()

            

            



    def welcome(self):
        self.WELCOME_INPUT = ""
        self.WELCOME_INPUT.lower()
        self.COOLDOWN = 6
        self.OVERHEAT_TRIES = 11
        while self.WELCOME_INPUT != "y" and self.WELCOME_INPUT != "n":
            self.OVERHEAT_TRIES = self.OVERHEAT_TRIES - 1
            if self.OVERHEAT_TRIES <= 1:
                self.OVERHEAT_TRIES = 0
                print(self.RED + "Slow down there! Your spamming a bit, enter the chill zone.")
                self.WAIT(5)
                self.OVERHEAT_TRIES = 10
                if self.OVERHEAT_TRIES == 10:
                    continue
            self.DESCRIPTION = "Welcome to Mixed Words. Begin game (y/n)? "
            self.WELCOME_INPUT = self.USER_INPUT(self.BLUE + self.DESCRIPTION)
            self.WELCOME_INPUT = self.WELCOME_INPUT.lower()
            if self.WELCOME_INPUT == "y":
                self.queue()

            if self.WELCOME_INPUT == "n":
                self.DESCRIPTION = "Come back soon! Thanks for visiting us!"
                self.PRINT(self.BLACK + self.DESCRIPTION)

            if self.WELCOME_INPUT != "y" and self.WELCOME_INPUT != "n":
                self.DESCRIPTION = "Invalid option. Please enter a valid option to proceed."
                self.PRINT(self.RED + self.DESCRIPTION)
    
    def __init__(self):
        self.NONE = ""
        self.RED = Fore.RED
        self.BLUE = Fore.BLUE
        self.GREEN = Fore.GREEN
        self.BLACK = Fore.BLACK
        self.YELLOW = Fore.YELLOW
        self.WHITE = Fore.WHITE
        self.USER_INPUT = input
        self.WORD_LIST = ["PRIME", "HELLO", "WELCOME", "VIDEOGAME", "AIRPLANE", "BIRD", "COMMAND", "PASS", "ROBLOX", "BEDWARS", "PYRO", "SPIRIT", "CATCHER", "RAVEN", "JADE", "BEEKEEPER", "BEATRIX", "WARRIOR", "BOUNTY", "HUNTER", "KILL", "STREAK", "WIN", "BLOOD", "DEAL", "ARES"]
        self.BANNED_USERS = [self.NONE]
        self.BAN_TIME = 0
        self.COOLDOWN = 0
        self.OVERHEAT_TRIES = 0
        self.WAIT = time.sleep
        self.PRINT = print
        self.DESCRIPTION = ""
        self.welcome()
v1 = game()
