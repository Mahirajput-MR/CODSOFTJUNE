import tkinter as tk
import random


choices = ['rock', 'paper', 'scissors']
emoji_map = {
    'rock': '🪨 Rock',
    'paper': '📄 Paper',
    'scissors': '✂️ Scissors'
}



def decide_winner(player, computer):
    if player == computer:
        return "🤝 It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
            (player == 'scissors' and computer == 'paper') or \
            (player == 'paper' and computer == 'rock'):
        return "🎉 You won!"
    else:
        return "💻 Computer won!"



def play(player_choice):
    computer_choice = random.choice(choices)


    player_label.config(text=f"You chose: {emoji_map[player_choice]}")
    computer_label.config(text=f"Computer chose: {emoji_map[computer_choice]}")


    result = decide_winner(player_choice, computer_choice)
    result_label.config(text=result)



root = tk.Tk()
root.title("Rock Paper Scissors Game 🎮")
root.geometry("450x450")
root.config(bg="#f4f4f4")


title = tk.Label(root, text="Rock 🪨  Paper 📄  Scissors ✂️", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
title.pack(pady=20)


player_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f4f4f4")
player_label.pack(pady=10)

computer_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f4f4f4")
computer_label.pack(pady=10)


result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="#333", bg="#f4f4f4")
result_label.pack(pady=20)


button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=20)

tk.Button(button_frame, text="🪨 Rock", width=12, font=("Helvetica", 12), command=lambda: play('rock')).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10)
tk.Button(button_frame, text="📄 Paper", width=12, font=("Helvetica", 12), command=lambda: play('paper')).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=10)
tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Helvetica", 12), command=lambda: play('scissors')).grid(
    row=0, column=2, padx=10)


exit_btn = tk.Button(root, text="Exit ❌", command=root.quit, bg="#ff4d4d", fg="white", font=("Helvetica", 12))
exit_btn.pack(pady=20)


root.mainloop()
