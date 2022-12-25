import random as rd


class Game:
    """This is where the logic of the game is done"""
    def __init__(self):
        
        self.cpu_choices_list = ["Rock", "Paper", "Scissors"]
        

    def cpu_choice_func(self, cpu) -> str:
        """Returns cpu choices in string type"""
        return self.cpu_choices_list[cpu]


    def game_outcome(self, player, cpu) -> str:
        """Returns the outcome of the round"""
        outcomes = [
            ["Draw.", "You Lose.", "You Win!"],
            ["You Win!", "Draw.", "You Lose."],
            ["You Lose.", "You Win!", "Draw."]
            ]

        return outcomes[player][cpu]