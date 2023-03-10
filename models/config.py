import tkinter


class Players:

    def __init__(self, root=tkinter.Tk()):
        self.player_one_name = tkinter.StringVar(root)
        self.player_two_name = tkinter.StringVar(root)
        self.player_three_name = tkinter.StringVar(root)
        self.player_four_name = tkinter.StringVar(root)
        self.player_five_name = tkinter.StringVar(root)
        self.player_six_name = tkinter.StringVar(root)
        self.player_seven_name = tkinter.StringVar(root)
        self.player_eight_name = tkinter.StringVar(root)


class Throws:

    def __init__(self):
        self.throw_one = 0


class PlayerScores:

    def __init__(self, game_type: int = 501):
        self.player_one_score = game_type
        self.player_two_score = game_type
        self.player_three_score = game_type
        self.player_four_score = game_type
        self.player_five_score = game_type
        self.player_six_score = game_type
        self.player_seven_score = game_type
        self.player_eight_score = game_type
