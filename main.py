import tkinter as tk
from tkinter import ttk
from models import config
from tkinter import messagebox

class DartScoreGUI:
    def __init__(self):
        self.current_player = 0
        self.players = []
        self.game_types = [501, 301, 201]
        self.row = 0
        self.create_widgets()
        self.players = config.Players(root)
        self.player_scores = config.PlayerScores(game_type=self.selected_game_type_score)

    def create_widgets(self):

        """ Game Type Menu """
        game_type_label = ttk.Label(root, text="Game Type:")
        game_type_label.grid(row=0, column=0, sticky=tk.E)

        self.game_type_menu = ttk.Combobox(root, values=["501", "301", "201"])
        self.game_type_menu.grid(row=0, column=1, padx=5, pady=5)
        self.game_type_menu.current(0)
        self.game_type_menu.bind("<<ComboboxSelected>>", self.update_game_type)

        """ Player Option Menu """
        player_selection_label = ttk.Label(root, text="Players:")
        player_selection_label.grid(row=1, column=0, sticky=tk.E)

        self.player_selection_menu = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6"], state="readonly")
        self.player_selection_menu.grid(row=1, column=1, padx=8, pady=7)
        self.player_selection_menu.current(0)
        self.player_selection_menu.bind("<<ComboboxSelected>>", self.update_num_players)

        """ START GAME BUTTON """
        self.start_game_button = ttk.Button(root, text="START", command=self.start_button)
        self.start_game_button.grid(row=self.row + 8, column=1, padx=8, pady=8)

        """ CONFIG """
        self.player_label = []
        self.player_entry = []
        self.player_names = [str]

        self.throws = 0
        self.selected_game_type_score = int(501)
        self.current_score = 501

    """ UPDATE THE NUMBER OF SELECTED PLAYERS """

    def update_num_players(self, event=None):
        self.num_players = int(self.player_selection_menu.get())
        self.show_player_inputs()

    """ UPDATE THE GAME TYPE """

    def update_game_type(self, event=None):
        self.selected_game_type_score = int(self.game_type_menu.get())
        print("")
    """ PLAYER TEXT FIELDS """

    def show_player_inputs(self):
        for entry in self.player_entry:
            entry.destroy()
            for label in self.player_label:
                label.destroy()

        self.player_label.clear()
        self.player_entry.clear()
        self.player_names.clear()

        # Add new player input fields
        for i in range(self.num_players):
            label = tk.Label(root, text=f"Player {i + 1}: ")
            label.grid(row=i + 2, column=0, padx=5, pady=5)
            self.player_label.append(label)

            if i == 0:
                entry = tk.Entry(root, width=15, textvariable=self.players.player_one_name)
                entry.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry)
                self.player_names.append(self.players.player_one_name.get())

            elif i == 1:
                entry2 = tk.Entry(root, width=15, textvariable=self.players.player_two_name)
                entry2.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry2)
                self.player_names.append(self.players.player_two_name.get())

            elif i == 2:
                entry3 = tk.Entry(root, width=15, textvariable=self.players.player_three_name)
                entry3.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry3)
                self.player_names.append(self.players.player_three_name.get())

            elif i == 3:
                entry4 = tk.Entry(root, width=15, textvariable=self.players.player_four_name)
                entry4.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry4)
                self.player_names.append(self.players.player_four_name.get())

            elif i == 4:
                entry5 = tk.Entry(root, width=15, textvariable=self.players.player_five_name)
                entry5.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry5)
                self.player_names.append(self.players.player_five_name.get())

            elif i == 5:
                entry5 = tk.Entry(root, width=15, textvariable=self.players.player_six_name)
                entry5.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry5)
                self.player_names.append(self.players.player_six_name.get())

            elif i == 6:
                entry6 = tk.Entry(root, width=15, textvariable=self.players.player_seven_name)
                entry6.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry6)
                self.player_names.append(self.players.player_seven_name.get())

            elif i == 7:
                entry7 = tk.Entry(root, width=15, textvariable=self.players.player_eight_name)
                entry7.grid(row=i + 2, column=1, padx=5, pady=5)
                self.player_entry.append(entry7)
                self.player_names.append(self.players.player_eight_name.get())

            self.row = i

    """ START BUTTON FUNCTION """

    def start_button(self):
        self.update_num_players()
        new_window = tk.Tk()
        new_window.title = "PLAYING"
        self.dart_input_widget(window=new_window)
        new_window.geometry("700x300")
        for player_name in self.player_names:
            print(player_name.count)

            # Add new player input fields
        for i, item in enumerate(self.player_names):
            label = tk.Label(new_window, text=f"Player {i}: {item}")
            label.grid(row=0, column=i + 3, padx=9, pady=9)
            print(item.count)
        new_window.mainloop()

    """ DART INPUT VALUES """
    def dart_input_widget(self, window=tk.Tk()):
        self.score_entry = tk.Entry(window, width=10)
        self.score_entry.grid(row=1, column=0)

        self.multiplier_label = tk.Label(window, text="Multiplier:")
        self.multiplier_label.grid(row=1, column=2)

        self.multiplier_var = tk.StringVar(value="Single")
        self.multiplier_menu = tk.OptionMenu(window, self.multiplier_var, "Single", "Double", "Triple")
        self.multiplier_menu.grid(row=2, column=2)

        # create buttons
        self.score_button = tk.Button(window, text="Calculate Score", command=self.calculate_score)
        self.score_button.grid(row=2, column=0)

        self.reset_button = tk.Button(window, text="Reset", command=self.reset_score)
        self.reset_button.grid(row=3, column=0)

        self.current_score_label = tk.Label(window, text=f"THE CURRENT SCORE IS: {self.current_score}")
        self.current_score_label.grid(row=4, column=0, pady=10)

        # Create a label to display the current player's turn
        self.player_turn_label = tk.Label(window, text=f"Player {self.current_player}'s turn")
        self.player_turn_label.grid(row=5, column=0)

    """ CALCULATE THE SCORE """

    def calculate_score(self, player_score: int = 501) -> int:

        try:
            player_score = int(self.score_entry.get())
            multiplier = self.multiplier_var.get()
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return 0

        if self.throws >= 3:
            self.throws = 0
            self.current_player = (self.current_player + 1) % self.num_players
            self.calculate_score_for_player()
            self.player_turn_label.config(text=f"Player {self.current_player + 1}´s turn.")

        if multiplier == "Double":
            player_score *= 2
        elif multiplier == "Triple":
            player_score *= 3

        if player_score > self.current_score:
            tk.messagebox.showerror("Invalid Score", "The score entered is greater than the current score.")
            return 0
        elif player_score == self.current_score:
            tk.messagebox.showinfo("Game Over", "Congratulations, you win!")
            self.reset_score()
        else:
            self.current_score -= player_score
            self.current_score_label.config(text=f"{self.current_score}")

        self.throws += 1
        return self.current_score

    """ RESET SCORE """

    def reset_score(self):
        self.current_score = self.selected_game_type_score
        self.current_score_label.config(text=f"{self.selected_game_type_score}")
        self.current_player = 0

    """ CALCULATE SCORE FOR EVERY PLAYER """
    def calculate_score_for_player(self):
        current_score_player_one = self.calculate_score(player_score=self.player_scores.player_one_score)
        current_score_player_two = self.calculate_score(player_score=self.player_scores.player_two_score)

        if self.current_player == 0:
            self.player_scores.player_one_score = current_score_player_one
            print("two")
            print(current_score_player_one)
        elif self.current_player == 1:
            self.player_scores.player_two_score = current_score_player_two
            print("two")
            print(current_score_player_two)



root = tk.Tk()
app = DartScoreGUI()
root.mainloop()
