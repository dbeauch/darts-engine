import tkinter as tk
from crick_game import *
from functools import partial

window = tk.Tk()
window.columnconfigure([0, 2], minsize=250)
window.rowconfigure([0, 6], minsize=100)

throw_15 = partial(throw, "15")
throw_16 = partial(throw, "16")
throw_17 = partial(throw, "17")
throw_18 = partial(throw, "18")
throw_19 = partial(throw, "19")
throw_20 = partial(throw, "20")
throw_25 = partial(throw, "25")

button15 = tk.Button(text="15", width=10, command=throw_15)
button15.grid(row=0, column=0, sticky="s")

button16 = tk.Button(text="16", width=10, command=throw_16)
button16.grid(row=1, column=0, sticky="n")

button17 = tk.Button(text="17", width=10, command=throw_17)
button17.grid(row=2, column=0, sticky="n")

button18 = tk.Button(text="18", width=10, command=throw_18)
button18.grid(row=3, column=0, sticky="n")

button19 = tk.Button(text="19", width=10, command=throw_19)
button19.grid(row=4, column=0, sticky="n")

button20 = tk.Button(text="20", width=10, command=throw_20)
button20.grid(row=5, column=0, sticky="n")

button25 = tk.Button(text="Bullseye", width=10, command=throw_25)
button25.grid(row=6, column=0, sticky="n")

for i in range(0, 7):
    label = tk.Label(textvariable=boardState1[i])
    if i == 0:
        label.grid(row=i, column=1, sticky="s")
    else:
        label.grid(row=i, column=1, sticky="n")

for i in range(0, 7):
    label = tk.Label(textvariable=boardState2[i])
    if i == 0:
        label.grid(row=i, column=2, sticky="s")
    else:
        label.grid(row=i, column=2, sticky="n")



window.mainloop()