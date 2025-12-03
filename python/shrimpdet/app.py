import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os

pygame.mixer.init()

def open_media_window():
    image_path = os.path.join("media", "ShrimpTrue.png")
    sound_path = os.path.join("media", "Wheeze.mp3")

    new_window = tk.Toplevel(root)
    new_window.title("")

    try:
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)

        label_new = tk.Label(new_window, image=photo)
        label_new.image = photo
        label_new.pack(pady=20)

        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

        new_window.protocol("WM_DELETE_WINDOW", lambda: (pygame.mixer.music.stop(), new_window.destroy()))

    except Exception as e:
        error_label = tk.Label(new_window, text=f"Error: {e}", fg="red")
        error_label.pack(pady=20)
        print(f"Error loading media: {e}")

def ask_if_shrimp():
    prompt_window = tk.Toplevel(root)
    prompt_window.title("Question")
    prompt_window.geometry("300x150")

    label = tk.Label(prompt_window, text="Are you a shrimp?", font=("Arial", 14))
    label.pack(pady=20)

    yes_button = tk.Button(prompt_window, text="Yes", command=lambda: [open_media_window(), prompt_window.destroy()])
    yes_button.pack(side="left", padx=40)

    no_button = tk.Button(prompt_window, text="No", command=prompt_window.destroy)
    no_button.pack(side="right", padx=40)

root = tk.Tk()
root.title("Shrimp detector")
root.geometry("300x200")

start_button = tk.Button(root, text="Start", command=ask_if_shrimp)
start_button.pack(pady=40)

root.mainloop()