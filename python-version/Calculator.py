import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current = screen.get()
        screen.set(current + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

screen = tk.StringVar()
screen.set("")

entry = tk.Entry(root, textvar=screen, font='lucida 20 bold', bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP)
    for char in row:
        btn = tk.Button(frame, text=char, font='lucida 15 bold', padx=20, pady=10)
        btn.pack(side=tk.LEFT, padx=10, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
