import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")
    
root = tk.Tk()
root.title("Tkinter Template App")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

root.mainloop()