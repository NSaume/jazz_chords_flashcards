import random
from time import sleep

keys = ("c", "d", "e", "f", "g", "a", "b")
maj_min = ("maj", "min")
flat_sharp = ("", "♭", "♯")
mod = ("⁷", "ᵐᵃʲ⁷")

def select_card():
    '''Selects a random key'''
    key = random.choice(keys)
    m_m = random.choice(maj_min)
    f_s = random.choice(flat_sharp)
    key = key + f_s
    if m_m == "maj":
        key = key.capitalize()
        key = key + random.choice(mod)
    else:
        key = key + "m⁷"
    return key

class Setting:
    """Setting class"""
    def __init__(self):
        self.explainer = ""
        self.val = None

    def set_explainer(self, exp_text):
        self.explainer = exp_text

    def get_val(self):
        while True:
            self.val = input(self.explainer)
            if str(self.val) == "exit":
                exit()
            try:
                self.val = float(self.val)
                break
            except:
                print("Please enter a number (integer or float), or type \"exit\" to leave.")

wait = Setting()
wait.set_explainer("Time between flashcards: ")
wait.get_val()

counter = Setting()
counter.set_explainer("Total number of Flashcards: ")
counter.get_val()

n = 0
sleep(wait.val)
while n < counter.val:
    print(select_card())
    n += 1
    sleep(wait.val)

