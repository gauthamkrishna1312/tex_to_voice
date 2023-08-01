import pyttsx3
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import shutil
import os

def text_to_speech():
    # Get the text from the entry widget
    text = text_entry.get()

    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.save_to_file(text, 'output.wav')
    engine.runAndWait()

    # Convert WAV to MP3
    sound = AudioSegment.from_wav('output.wav')
    sound.export('output.mp3', format='mp3')

    # Remove the temporary WAV file
    os.remove('output.wav')

    # Open a file dialog to save the MP3 file
    save_file_path = filedialog.asksaveasfilename(defaultextension=".mp3")

    # Move the generated MP3 file to the selected save location
    if save_file_path:
        shutil.move('output.mp3', save_file_path)
        
def play_sound():
    # Get the text from the entry widget
    text = text_entry.get()
    
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Convert text to speech
    engine.say(text)
    
    # Play the speech
    engine.runAndWait()
    

# Create the main window
window = tk.Tk()
window.title("Text-to-Speech")
window.geometry("300x200")

# Create the text entry widget
text_entry = tk.Entry(window, width=30)
text_entry.pack(pady=20)

# Create the button to convert text to speech
convert_button = tk.Button(window, text="Convert and save", command=text_to_speech)
convert_button.pack()

# Create the button to play the voice
convert_button = tk.Button(window, text="Play", command=play_sound)
convert_button.pack()

# Run the main window event loop
window.mainloop()
