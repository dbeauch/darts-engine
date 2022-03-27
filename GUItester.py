import tkinter as tk
from crick_game import states, boardState1, boardState2

window = tk.Tk()
window.columnconfigure([0, 2], minsize=250)
window.rowconfigure([0, 6], minsize=100)

button15 = tk.Button(text="15", width=10)
button15.grid(row=0, column=0, sticky="s")

button16 = tk.Button(text="16", width=10)
button16.grid(row=1, column=0, sticky="n")

button17 = tk.Button(text="17", width=10)
button17.grid(row=2, column=0, sticky="n")

button18 = tk.Button(text="18", width=10)
button18.grid(row=3, column=0, sticky="n")

button19 = tk.Button(text="19", width=10)
button19.grid(row=4, column=0, sticky="n")

button20 = tk.Button(text="20", width=10)
button20.grid(row=5, column=0, sticky="n")

button25 = tk.Button(text="Bullseye", width=10)
button25.grid(row=6, column=0, sticky="n")

for i in range(0, 7):
    label = tk.Label(text=boardState1[i])
    if i == 0:
        label.grid(row=i, column=1, sticky="s")
    else:
        label.grid(row=i, column=1, sticky="n")

for i in range(0, 7):
    label = tk.Label(text=boardState2[i])
    if i == 0:
        label.grid(row=i, column=2, sticky="s")
    else:
        label.grid(row=i, column=2, sticky="n")


window.mainloop()