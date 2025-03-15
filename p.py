import random
import tkinter as tk
# Dictionary mappings for the choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
# Function to handle the game logic
def play_game(youstr):
    # Generate a new choice for the computer each time the game is played
    computer = random.choice([-1, 0, 1])
    you = youDict[youstr]
    # Display choices
    result_text.set(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
    # Determine the outcome and update the result_text
    if computer == you:
        result_text.set(result_text.get() + "\nIt's a draw!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result_text.set(result_text.get() + "\nYou win!")
    else:
        result_text.set(result_text.get() + "\nYou lose!") 
# Create the main Tkinter window
root = tk.Tk()
root.title("Snake-Water-Gun Game")
root.geometry("300x250")

# Display label for the game title
title_label = tk.Label(root, text="Snake-Water-Gun Game", font=("Arial", 14),bg="red")
title_label.pack(pady=100)

# Result display area
result_text = tk.StringVar()# stringVar(variable class) is used to handle strings in tkinter 
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="yellow",justify="center")
result_label.pack(pady=10, fill='x', expand=True)
result_label.pack(pady=10)

# Buttons for choices
snake_button = tk.Button(root, text="Snake", command=lambda: play_game('s'), width=10, font=("Arial", 12))
water_button = tk.Button(root, text="Water", command=lambda: play_game('w'), width=10, font=("Arial", 12))
gun_button = tk.Button(root, text="Gun", command=lambda: play_game('g'), width=10, font=("Arial", 12))

# Pack buttons
snake_button.pack(pady=5)
water_button.pack(pady=5)
gun_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()# making the window appear