import os
import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def choose_music_file():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])

pygame.init()
window = tk.Tk()
window.title("Music Player")

play_button = tk.Button(window, text="Play", command=play_music)
pause_button = tk.Button(window, text="Pause", command=pause_music)
unpause_button = tk.Button(window, text="Unpause", command=unpause_music)
stop_button = tk.Button(window, text="Stop", command=stop_music)
choose_file_button = tk.Button(window, text="Choose File", command=choose_music_file)

play_button.grid(row=0, column=0, padx=10, pady=10)
pause_button.grid(row=0, column=1, padx=10, pady=10)
unpause_button.grid(row=0, column=2, padx=10, pady=10)
stop_button.grid(row=0, column=3, padx=10, pady=10)
choose_file_button.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Global variable to store the selected music file
filename = ""

# Start the main loop
window.mainloop()
