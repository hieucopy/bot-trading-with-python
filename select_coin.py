import tkinter as tk
from tkinter.ttk import *

def input():
    window =tk.Tk()
    window.title("input trading app")
    window.geometry("400x300")

    def click():
        global coin 
        coin = combo.get()
        window.destroy()
    
        
    label = tk.Label(window, text="Welcome to My Trading App", font=("Arial", 16))
    label.pack(pady=20)
    button = tk.Button(window, text="Start Trading", width=20, height=2,command=click)
    button.pack()
    label_combo=tk.Label(window, text="select coin you want to trade")
    label_combo.pack()
    combo= Combobox(window, width=20)
    combo['value']=('BTC','ETH','SOL','DOGE','BNB','XRP')
    combo.pack()
    combo.current(0)
    window.mainloop()
    return coin

if __name__ == "__input__":
    input()

