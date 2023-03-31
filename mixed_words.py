import random
import time
import colorama
from colorama import Fore,Back,Style
import os
from playsound import playsound
os.system("")

colorama.init()

class game():

    def crate(self):
        self.CHANCE_CONTROLLER = random.randint(1,50)
        self.LIST_CONTROLLER = 1 # random.randint(1,2)
        self.SELECTED_REWARD = self.NONE
        self.COLOR_THEME_CONTROLLER = random.choice(self.CRATE_REWARDS_THEME_TICKETS)
        self.TICKET_CONTROLLER = random.choice(self.CRATE_TICKETS)
        self.CRATE_INPUT = ""
        self.LEGENDARY_HITS = [11, 26, 50]
        self.EPIC_HITS = [31, 8, 6]
        self.RARE_HITS = [4, 7, 14, 17]
        self.UNCOMMON_HITS = [3, 5, 9, 13, 16, 21, 24]
        self.COMMON_HITS = [1, 2, 19, 43, 44, 45, 48, 49, 34, 33]
        self.COLOR_THEME_COLORS = ["red", "blue", "green", "black", "yellow", "magenta", "cyan", "gold"]
        if self.LIST_CONTROLLER == 1:
            self.SELECTED_REWARD = random.choice(self.CRATE_REWARDS)
            if self.CHANCE_CONTROLLER in self.LEGENDARY_HITS:
                if self.SELECTED_REWARD[1] == "Legendary":
                    self.PRINT(self.GREEN + f"You got {self.SELECTED_REWARD[0]}! | {self.GOLD + self.SELECTED_REWARD[1]}")


        

    def locker(self):
        self.LOCKER_INPUT = ""
        self.LOCKER_INPUT.lower()
        self.PRINT(self.GREEN + "Welcome to Locker! What would you like to use today?")
        self.PRINT(self.GREEN + f"1. Lucky Crate (x{self.CRATES_OWNED})")
        self.PRINT(self.GREEN + f"2. Activate a boost (x{self.BOOSTS_OWNED})")
        while self.LOCKER_INPUT != "PLACEMENT_ZERO":
            self.LOCKER_INPUT = self.USER_INPUT("Select what you would like to use. ")
            if self.LOCKER_INPUT == "lucky crate" or self.LOCKER_INPUT == "crate" and self.CRATES_OWNED >= 1:
                self.PRINT(self.RED + "This feature is temporarily disabled.")
                # self.PRINT("Unboxing Crate.")
                # self.WAIT(0.5)
                # self.PRINT("Unboxing Crate..")
                # self.WAIT(0.5)
                # self.PRINT("Unboxing Crate...")
                # self.crate()
                self.locker()
            if self.LOCKER_INPUT == "n" or self.LOCKER_INPUT == "exit":
                self.welcome()
            if self.LOCKER_INPUT != "lucky crate" and self.LOCKER_INPUT != "crate" and self.LOCKER_INPUT != "lc" and self.LOCKER_INPUT != "boost" and self.LOCKER_INPUT != "bt":
                self.PRINT(self.RED + "Unable to proceed. Error: Invalid option.")
            
    def battle_pass(self):
        self.BATTLE_PASS_SEASON = self.BATTLE_PASS_SEASON1
        self.BATTLE_PASS_LEVEL = self.PLAYER_LEVEL
        self.REQUIRED_BATTLE_PASS_LEVEL = 1
        self.REWARD_TEXT_COLOR = random.randint(1, 6)
        self.LEVEL_COLOR = self.REWARD_COLOR_NUMBERS[random.randint(1, 6)]
        self.LEVEL_TYPE_COLOR = self.BATTLE_PASS_REWARD_TYPE_COLOR["Word"]
        self.SET_LEVEL_TYPE = ""
        self.PRINT_TIMES = 0
        sorted_levels = sorted(self.BATTLE_PASS_SEASON.keys())
        self.highest_claimed_level = 0
        print(self.RED + f"(NEW!)" + self.GREEN + " Battle Pass Season 1" + self.BLUE + " (5 weeks remaining)" + self.GREEN + " (50 Levels):\n")
        print(self.RED + f"You're currently Level {self.BATTLE_PASS_LEVEL}.")
        for level_num in sorted_levels:
            reward = self.BATTLE_PASS_SEASON[level_num]
            level_string = self.BATTLE_PASS_REWARD_TYPE_COLOR[reward[1]] + f"(Level {level_num}) {reward[0]}"
            reward_string = f"{reward[1]} | "
            level_color = self.BATTLE_PASS_REWARD_TYPE_COLOR[reward[1]]
            if reward[1] in self.BATTLE_PASS_REWARD_TYPE_COLOR:
                reward_type_color = self.BATTLE_PASS_REWARD_TYPE_COLOR[reward[1]]


            if self.BATTLE_PASS_LEVEL >= level_num:
                level_color = self.REWARD_COLOR_NUMBERS[1]
                reward_string = self.GREEN + f"{reward[1]} | Claimed"
                if reward[1] in ['Word', 'Special Word']:
                    self.WORD_LIST.append(reward[0])


            if self.BATTLE_PASS_LEVEL >= 5:
                self.LOCKER.append("Lucky Crate")

            if self.BATTLE_PASS_LEVEL >= 30:
                self.LOCKER.append("2x XP")

            if self.BATTLE_PASS_LEVEL >= 35:
                self.LOCKER.append("Lucky Crate")

            if self.BATTLE_PASS_LEVEL >= 40:
                self.LOCKER.append("3x XP")


            # if self.BATTLE_PASS_LEVEL >= 1:
            #     if level_num == 1:
            #         level_color = self.REWARD_COLOR_NUMBERS[1]
            #         reward_string = self.GREEN + f"{reward[1]} | Claimed"




            if True:
                print(f"{level_color}{level_string} | {reward_type_color}{reward_string}")
       
        print("\n")








    def main_game(self):
        self.SELECT_WORD = random.choice(self.WORD_LIST)
        #weekly mission 3
        if self.WEEKLY_MISSION3_COMPLETED == False:
            if self.SELECT_WORD == "BEEKEEPER":
                self.WEEKLY_MISSION3_COMPLETED = True
                self.CURRENT_XP = self.CURRENT_XP + 1000
        #end
        if " " in self.SELECT_WORD:
            print(self.BLUE + f"Your sentence is: {self.SELECT_WORD}")
        else:
            self.SCAMBLED_WORD = ''.join(random.sample(self.SELECT_WORD, len(self.SELECT_WORD)))
            self.PRINT(self.BLUE + f"Your scrambled word is: {self.SCAMBLED_WORD}")
        if " " in self.SELECT_WORD:
            self.GAME_INPUT = self.USER_INPUT("Enter your SPECIAL WORD: ")
        else:
            self.GAME_INPUT = self.USER_INPUT("Enter your guess: ")
        if self.GAME_INPUT.lower() == self.SELECT_WORD.lower():
            self.PLAY_AGAIN_INPUT = ""
            self.XP_AMOUNT = random.randint(100, 200)
            self.VICTORY_XP = random.randint(500, 700)
            self.PRINT(self.YELLOW + "VICTORY!")
            self.MISSION_COUNTER += 1
            self.WAIT(2)
            self.PRINT(self.GREEN + f"You gained {self.XP_AMOUNT} XP!")
            self.CURRENT_XP = self.CURRENT_XP + self.XP_AMOUNT
            self.WAIT(2)
            self.PRINT(self.GREEN + f"You gained {self.VICTORY_XP} Victory XP!")
            self.CURRENT_XP = self.CURRENT_XP + self.VICTORY_XP
            self.WAIT(2)
            if self.WEEKLY_MISSION1_COMPLETED == False:
                if self.MISSION_COUNTER >= 3:
                    self.WEEKLY_MISSION1_COMPLETED = True
                    self.CURRENT_XP = self.CURRENT_XP + 8000
            if self.CURRENT_XP >= self.LEVEL_UP_XP:
                self.PLAYER_LEVEL = self.PLAYER_LEVEL + self.LEVEL_UP
                self.CURRENT_XP = 0
                self.LEVEL_UP_XP = self.LEVEL_UP_XP + 3000
                print(self.YELLOW + f"YOU LEVELED UP TO LEVEL {self.PLAYER_LEVEL}! CONGRATS!")
                self.PLAY_AGAIN_INPUT = self.NONE
                while self.PLAY_AGAIN_INPUT != "y" and self.PLAY_AGAIN_INPUT != "n":
                    self.PLAY_AGAIN_INPUT = self.USER_INPUT(self.GREEN + "Play Again? (y/n) ")

                    if self.PLAY_AGAIN_INPUT == "y":
                        self.queue(0)
                        break

                    if self.PLAY_AGAIN_INPUT == "n":
                        self.welcome()
                        break
            else:
                self.PRINT(f"You need {self.CURRENT_XP}/{self.LEVEL_UP_XP} to level up!")
                self.PLAY_AGAIN_INPUT = self.NONE
                while self.PLAY_AGAIN_INPUT != "y" and self.PLAY_AGAIN_INPUT != "n":
                    self.PLAY_AGAIN_INPUT = self.USER_INPUT(self.GREEN + "Play Again? (y/n) ")

                    if self.PLAY_AGAIN_INPUT == "y":
                        self.queue(0)
                        break

                    if self.PLAY_AGAIN_INPUT == "n":
                        self.welcome()
                        break

        else:
            self.PRINT(self.RED + f"Dang it! You got it wrong. The correct word was {self.SELECT_WORD}")
            self.PLAY_AGAIN_INPUT = ""
            self.XP_AMOUNT = random.randint(100, 200)
            self.PRINT(self.GREEN + f"You gained {self.XP_AMOUNT} XP!")
            self.CURRENT_XP = self.CURRENT_XP + self.XP_AMOUNT
            self.WAIT(2)
            if self.CURRENT_XP >= self.LEVEL_UP_XP:
                self.PLAYER_LEVEL = self.PLAYER_LEVEL + self.LEVEL_UP
                self.CURRENT_XP = 0
                self.LEVEL_UP_XP = self.LEVEL_UP_XP + 3000
                print(self.YELLOW + f"YOU LEVELED UP TO LEVEL {self.PLAYER_LEVEL}! CONGRATS!")
                self.PLAY_AGAIN_INPUT = ""
                while self.PLAY_AGAIN_INPUT != "y" and self.PLAY_AGAIN_INPUT != "n":
                    self.PLAY_AGAIN_INPUT = self.USER_INPUT(self.GREEN + "It was a nice try though. Mind playing again? (y/n) ")

                    if self.PLAY_AGAIN_INPUT == "y":
                        self.queue(0)
                        break

                    if self.PLAY_AGAIN_INPUT == "n":
                        self.welcome()
                        break
            else:
                self.PRINT(f"You need {self.CURRENT_XP}/{self.LEVEL_UP_XP} to level up!")
                self.PLAY_AGAIN_INPUT = ""
                while self.PLAY_AGAIN_INPUT != "y" and self.PLAY_AGAIN_INPUT != "n":
                    self.PLAY_AGAIN_INPUT = self.USER_INPUT(self.GREEN + "It was a nice try though. Mind playing again? (y/n) ")

                    if self.PLAY_AGAIN_INPUT == "y":
                        self.queue(0)
                        break

                    if self.PLAY_AGAIN_INPUT == "n":
                        self.welcome()
                        break


    def queue(self, amount):
        self.QUEUE_DESC1 = "Looking for match."
        self.QUEUE_DESC2 = "Looking for match.."
        self.QUEUE_DESC3 = "Looking for match..."
        self.QUEUE_FOUND = "Match found!"
        self.QUEUE_JOIN = "Joining Match!"
        self.COOLDOWN = 1
        self.QUEUE_SELECTED_DESCRIPTION = 1
        self.QUEUE_SEARCH_TIME = random.randint(1,5)
        self.QUEUE_FIND_CHANCE = random.randint(1,5)
        self.CAN_TELEPORT = False
        

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
        else:
            self.PRINT(self.RED + "Failed joining match! Stand by!")

        # while amount < 5:  # limit the number of attempts to find a match to 5
        #     #print(self.QUEUE_FIND_CHANCE)
        #     self.PRINT(self.BLUE + self.QUEUE_DESC1)
        #     self.WAIT(self.COOLDOWN)
        #     self.PRINT(self.BLUE + self.QUEUE_DESC2)
        #     self.WAIT(self.COOLDOWN)
        #     self.PRINT(self.BLUE + self.QUEUE_DESC3)
        #     self.WAIT(self.COOLDOWN)
            
        #     if self.QUEUE_FIND_CHANCE in [1, 2, 3]:
        #         self.DESCRIPTION = "Match found! Entering now."
        #         self.PRINT(self.YELLOW + self.DESCRIPTION)
        #         self.main_game()
        #         break
        #     else:
        #         amount = amount + 1
        #         self.DESCRIPTION = f"Failed finding match. Stand by! Attempt {self.TRIES}/5."
        #         self.PRINT(self.RED + self.DESCRIPTION)
        #         self.queue(amount)
        #         break

        # if amount == 5:
        #     self.DESCRIPTION = f"Failed to find match after {amount} attempts. Please try again. If the problem persists, contact PrimeDev#2349 on Discord."
        #     self.PRINT(self.RED + self.DESCRIPTION)
        #     self.welcome()

            

            



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
            self.WELCOME_ADD_DESC = self.RED + "1. Missions " + self.RED + "| 2. Battle Pass " + self.BLUE + "| 3. Locker " + self.YELLOW + "| 4. Begin Game (y) | 5. Exit (n) " + self.RED + "| 6. " + self.RED + "COMING SOON!"
            self.PRINT(self.WELCOME_ADD_DESC)
            self.DESCRIPTION = "Welcome to Mixed Words. Select where you would like to go. "
            self.WELCOME_INPUT = self.USER_INPUT(self.GREEN + self.DESCRIPTION)
            self.WELCOME_INPUT = self.WELCOME_INPUT.lower()
            if self.WELCOME_INPUT == "y":
                self.queue(0)

            if self.WELCOME_INPUT == "n":
                self.DESCRIPTION = "Come back soon! Thanks for visiting us!"
                self.PRINT(self.BLACK + self.DESCRIPTION)
                exit()

            if self.WELCOME_INPUT == "missions" or self.WELCOME_INPUT == "m":
                self.PRINT(Fore.GREEN + "This Weeks' Missions:")
                self.WEEKLY_MISSION1 = "Win 3 Matches (8000 XP)"
                self.WEEKLY_MISSION2 = "Unlock Level 1 (1000 XP)"
                self.WEEKLY_MISSION3 = "Find the word BEEKEEPER (1000 XP)"
                if self.WEEKLY_MISSION1_COMPLETED == False:
                    self.PRINT(self.RED + self.WEEKLY_MISSION1)
                if self.WEEKLY_MISSION2_COMPLETED == False:
                    if self.PLAYER_LEVEL >= 1:
                        self.WEEKLY_MISSION2_COMPLETED = True
                    else:
                        self.PRINT(self.RED + self.WEEKLY_MISSION2)
                if self.WEEKLY_MISSION3_COMPLETED == False:
                    self.PRINT(self.RED + self.WEEKLY_MISSION3)

                if self.WEEKLY_MISSION1_COMPLETED == True:
                    self.PRINT(self.GREEN + self.WEEKLY_MISSION1 + " | COMPLETED")
                if self.WEEKLY_MISSION2_COMPLETED == True:
                    self.PRINT(self.GREEN + self.WEEKLY_MISSION2 + " | COMPLETED")
                if self.WEEKLY_MISSION3_COMPLETED == True:
                    self.PRINT(self.GREEN + self.WEEKLY_MISSION3 + " | COMPLETED")



            if self.WELCOME_INPUT == "battle pass" or self.WELCOME_INPUT == "bp":
                self.battle_pass()

            if self.WELCOME_INPUT == "pr1med3v20112606":
                self.admin_login()
                break
            
            if self.WELCOME_INPUT == "release hype!":
                self.PLAYER_LEVEL = 50
                print("lvl 50 given")

            if self.WELCOME_INPUT == "prime was here":
                print("was he?")

            if self.WELCOME_INPUT == "/info":
                self.PRINT(self.GREEN + f"You need {self.CURRENT_XP}/{self.LEVEL_UP_XP}.")
                self.PRINT(self.RED + f"Current Player XP: {self.CURRENT_XP}")
                self.PRINT(self.RED + f"Current Player Level: {self.PLAYER_LEVEL}")
            
            if self.WELCOME_INPUT == "how do i get to level 50?":
                self.PRINT("In order to complete and gain XP fast to claim all Battle Pass rewards, do missions or win games.")

            if self.WELCOME_INPUT == "lk" or self.WELCOME_INPUT == "locker":
                self.locker()

            if self.WELCOME_INPUT == "im so lucky":
                self.PRINT(self.YELLOW + "crate altar enabled")
                self.CRATES_OWNED += 1

            if self.WELCOME_INPUT != "y" and self.WELCOME_INPUT != "n" and self.WELCOME_INPUT != "m" and self.WELCOME_INPUT != "bp" and self.WELCOME_INPUT != "lk" and self.WELCOME_INPUT != "missions" and self.WELCOME_INPUT != "battle pass" and self.WELCOME_INPUT != "locker" and self.WELCOME_INPUT != "begin game" and self.WELCOME_INPUT != "exit" and self.WELCOME_INPUT != "pr1med3v20112606" and self.WELCOME_INPUT != "release hype!" and self.WELCOME_INPUT != "prime was here" and self.WELCOME_INPUT != "/info" and self.WELCOME_INPUT != "how do i get to level 50?" and self.WELCOME_INPUT != "im so lucky":
                self.DESCRIPTION = "Invalid option. Please enter a valid option to proceed."
                self.PRINT(self.RED + self.DESCRIPTION)
    
    def __init__(self):
        self.NONE = ""
        self.RED = Fore.RED
        self.BLUE = Fore.BLUE
        self.GREEN = Fore.GREEN
        self.BLACK = Fore.BLACK
        self.YELLOW = Fore.YELLOW
        self.MAGENTA = Fore.MAGENTA
        self.CYAN = Fore.CYAN
        self.GOLD = Fore.LIGHTYELLOW_EX
        self.LIGHTWHITE = Fore.LIGHTWHITE_EX
        self.LIGHTRED = Fore.LIGHTRED_EX
        self.LIGHTBLACK = Fore.LIGHTBLACK_EX
        self.LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX
        self.LIGHTBLUE = Fore.LIGHTBLUE_EX
        self.LIGHTGREEN = Fore.LIGHTGREEN_EX
        self.WHITE = Fore.WHITE
        self.USER_INPUT = input
        self.WORD_LIST = ["PRIME", "HELLO", "WELCOME", "VIDEOGAME", "AIRPLANE", "BIRD", "COMMAND", "PASS", "ROBLOX", "BEDWARS", "PYRO", "SPIRIT", "CATCHER", "RAVEN", "JADE", "BEEKEEPER", "BEATRIX", "WARRIOR", "BOUNTY", "HUNTER", "KILL", "STREAK", "WIN", "BLOOD", "DEAL", "ARES"]
        self.BANNED_USERS = [self.NONE]
        self.ADMINS = ["PrimeDev"]
        self.ADMIN_CMDS = ["/info", "/givexp", "/setlevel", "/kick"]
        self.BAN_TIME = 0
        self.COOLDOWN = 0
        self.OVERHEAT_TRIES = 0
        self.WAIT = time.sleep
        self.PRINT = print
        self.DESCRIPTION = ""
        self.TRIES = 0
        self.BATTLE_PASS_SEASON = 1
        self.PLAYER_LEVEL = 0
        self.BATTLE_PASS_REWARDS = self.NONE
        self.BATTLE_PASS_LEVEL_UP = self.NONE
        self.MISSION_COUNTER = 0
        self.WEEKLY_MISSION1_COMPLETED = False
        self.WEEKLY_MISSION2_COMPLETED = False
        self.WEEKLY_MISSION3_COMPLETED = False
        self.CURRENT_XP = 0
        self.LEVEL_UP_XP = 3000
        self.LEVEL_UP = 1
        self.PLAYSOUND = playsound

        self.LOCKER = []
        self.CRATES_OWNED = 0
        self.BOOSTS_OWNED = 0
        self.CRATE_CHANCE_TYPES = ["Divine", "Mythical", "Legendary", "Epic", "Rare", "Uncommon", "Common"]


        self.XP_BOOST_ACTIVATED = False
        self.BATTLE_PASS_SEASON1 = {
            1: ["UPDATE!", "Word"],
            2: ["BEGIN", "Word"],
            3: ["NO", "Word"],
            4: ["YES", "Word"],
            5: ["Lucky Crate", "Crate"],
            6: ["COME", "Word"],
            7: ["REMASTERED", "Word"],
            8: ["COZY", "Word"],
            9: ["ABILITY", "Word"],
            10: ["ACROSS", "Word"],
            11: ["RUN", "Word"],
            12: ["ACTION", "Word"],
            13: ["END", "Word"],
            14: ["LIFE", "Word"],
            15: ["GG", "Word"],
            16: ["DAY'S TODAY", "Special Word"],
            17: ["MIDNIGHT", "Word"],
            18: ["EVENING", "Word"],
            19: ["CHAOS", "Word"],
            20: ["VVSABRO", "Word"],
            21: ["PR1ME", "Word"],
            22: ["LOL", "Word"],
            23: ["XP HUNTING", "Special Word"],
            24: ["SLAY", "Word"],
            25: ["PRIME JUST KIDDING!", "Special Word"],
            26: ["DAVID I'M CRAZY!", "Special Word"],
            27: ["XBOT IM CATCHING UP...", "Special Word"],
            28: ["PRIME FAILED...", "Special Word"],
            29: ["VVSABRO DIAMOND", "Special Word"],
            30: ["2x XP", "Boost"],
            31: ["CODEBRO FOUND IT!", "Special Word"],
            32: ["CARROT'S CLASSROOM", "Special Word"],
            33: ["PRIME ALL GOOD", "Special Word"],
            34: ["DAVID ITS TIME", "Special Word"],
            35: ["Lucky Crate", "Crate"],
            36: ["PRIME RIP...", "Special Word"],
            37: ["CMERE KEED", "Special Word"],
            38: ["DAVID IS CRAZY", "Special Word"],
            39: ["NICE TRY", "Special Word"],
            40: ["3x XP", "Boost"],
            41: ["NOT TODAY!", "Special Word"],
            42: ["CMERE RN", "Special Word"],
            43: ["YOU LITTLE", "Special Word"],
            44: ["STEWPID", "Word"],
            45: ["VVSABRO LET'S GO!", "Special Word"],
            46: ["CODEBRO SCAM TIME...", "Special Word"],
            47: ["SCAMMER BRO", "Special Word"],
            48: ["CARROT FARMED MYSELF!", "Special Word"],
            49: ["CARROT UWU", "Special Word"],
            50: ["GET PRIME'D", "Special Word"]
        }


        self.BATTLE_PASS_REWARD_TYPE = ["Crate", "Boost", "Card", "Word", "Special Word", "Reward", "New Mission"]
        self.BATTLE_PASS_REWARD_TYPE_COLOR = {
            "Crate": self.YELLOW,
            "Boost": self.GREEN,
            "Card": self.WHITE,
            "Word": self.CYAN,
            "Special Word": self.MAGENTA,
            "Reward": self.NONE,
            "New Mission": self.RED,
            "Default": self.WHITE,
            "Secret Word": self.LIGHTBLACK
        }
        self.REWARD_COLOR_NUMBERS = {
            1: self.RED,
            2: self.BLUE,
            3: self.GREEN,
            4: self.YELLOW,
            5: self.MAGENTA,
            6: self.CYAN
        }
        self.REQUIRED_BATTLE_PASS_LEVEL = 1
        self.welcome()
v1 = game()
