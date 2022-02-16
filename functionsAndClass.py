

from random import choice
from data import input_description
import os


class Player:
    def __init__(self):
        self.PT = 0
        self.LS = 0
    
    def get_name(self):
        return self.name
    
    def get_pt(self):
        return self.PT
    
    def get_ls(self):
        return self.LS
    
    def get_player_infos(self):
        return f"{self.get_name()} have [{self.get_pt()}] points and [{self.get_ls()}] lose parts !"


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.PT += 5
        self.name = name
    
    def choice_obj(self,fourniture):
        print(input_description)
        user_choice = input()
        if user_choice not in fourniture and user_choice != 'q':
            return self.choice_obj(fourniture)
        return user_choice
    

class ProgramPlayer(Player):
    def __init__(self,name):
        super().__init__()
        self.name = name

        self.track_utils = {
        's':'r',
        'r':'r',
        'p':'s'
        }
    
    def choice_obj(self,fourniture,lines):
        if len(lines) >= 2:
            #Start the tracking
            print('Tracking...')
            phrase = "".join(lines).replace("\n","")
            ch_old = frequence(phrase)
            return self.track_utils[ch_old]
        else:
            return self.choice_random_obj(fourniture)
    
    def choice_random_obj(self,fourn):
        return choice(fourn)


def file_empty(_file,ch):
    f = open(_file,"w")
    f.write(ch)
    f.close()

def frequence(chaine):
    string_length = len(chaine)
    string = chaine.lower()
    string_ = set(chaine)
    table = list()
    for lettre in string_:
        letter_number = string.count(lettre)
        table.append((letter_number/string_length,lettre))
    m = max(table)
    n = m[1]
    return n

def create_file_if_not_exists(file_name):
    if not os.path.exists(file_name):
        file = open(file_name,"w")
        file.close()