import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16))
        self.label.pack(pady=20)

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack()

        self.rock_button = tk.Button(self.choices_frame, text="Rock", command=lambda: self.play("rock"), height=2, width=10)
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.choices_frame, text="Paper", command=lambda: self.play("paper"), height=2, width=10)
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.choices_frame, text="Scissors", command=lambda: self.play("scissors"), height=2, width=10)
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(root, text="Score -> You: 0, Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=20)

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.get_winner(user_choice, computer_choice)
        self.result_label.config(text=f"Computer chose: {computer_choice}. {result}")
        self.score_label.config(text=f"Score -> You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()