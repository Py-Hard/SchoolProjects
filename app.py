import tkinter as tk

def open_new_window():
    user_text = entry.get()

    new_window = tk.Toplevel(root)
    new_window.title("Your height:")
    new_window.geometry("250x100")

    label_new = tk.Label(new_window, text=user_text, font=("Arial", 12))
    label_new.pack(pady=20)

root = tk.Tk()
root.title("Height calculator 6700")
root.geometry("300x200")

entry = tk.Entry(root, width=25)
entry.pack(pady=20)

button = tk.Button(root, text="Calculate height", command=open_new_window)
button.pack(pady=10)

root.mainloop()