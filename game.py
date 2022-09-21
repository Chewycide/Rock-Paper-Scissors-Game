import random as rd

class Game:

    def __init__(self):
        
        self.cpu_choices_list = ["Rock", "Paper", "Scissors"]
        # self.cpu_choice = rd.randint(0, 2)
        # self.cpu_choice_func(self.cpu_choice)
        # self.game_outcome(self.choice, self.cpu_choice)
        

    def cpu_choice_func(self, cpu):

        return self.cpu_choices_list[cpu]


    def game_outcome(self, player, cpu):

        outcomes = [
            ["Draw.", "You Lose.", "You Win!"],
            ["You Win!", "Draw.", "You Lose."],
            ["You Lose.", "You Win!", "Draw."]
            ]

        return outcomes[player][cpu]