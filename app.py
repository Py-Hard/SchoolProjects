import tkinter as tk
import pygame
import os

# Initialize pygame mixer once at the start
pygame.mixer.init()

def open_new_window():
    image_path = os.path.join("media", "ShrimpTrue.png")  
    sound_path = os.path.join("media", "Wheeze.mp3") 

    new_window = tk.Toplevel(root)
    new_window.title("Your Image")
    new_window.geometry("400x400")

    try:
        # Load PNG image with Tkinter's PhotoImage
        photo = tk.PhotoImage(file=image_path)

        # Display the image
        label_new = tk.Label(new_window, image=photo)
        label_new.image = photo  # keep reference
        label_new.pack(pady=20)

        # Play sound using pygame
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

    except Exception as e:
        error_label = tk.Label(new_window, text=f"Error: {e}", fg="red")
        error_label.pack(pady=20)

root = tk.Tk()
root.title("Image & Sound Viewer")
root.geometry("300x200")

button = tk.Button(root, text="Open Media", command=open_new_window)
button.pack(pady=40)

root.mainloop()