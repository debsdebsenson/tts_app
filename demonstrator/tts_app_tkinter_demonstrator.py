import tkinter as tk
from tkinter import scrolledtext
import subprocess


# Set paths
def get_paths():
    model_dir = 'tts_models/de/thorsten/tacotron2-DDC'
    out_dir = 'output.wav'
    vlc_player_path = "vlc"  # Replace with your actual path
    return [model_dir, vlc_player_path, out_dir]


def open_vlc():
    # Use subprocess to run the command to open VLC and play the .wav file
    paths = get_paths()
    subprocess.run([paths[1], paths[2]])


def run_conversion(text):
    paths = get_paths()
    model_dir, out_dir = paths[0], paths[2]

    # Execute the command line command using subprocess
    subprocess.run(['tts', '--model_name', model_dir, '--out_path', out_dir, '--text', text])


def take_input(input_text_field):
    input_txt = input_text_field.get("1.0", "end-1c")
    run_conversion(input_txt)
    open_vlc()


def create_text_field(root):
    # Create a text field for the user to enter text and add it to the window
    text_field_label = tk.Label(text="Insert the text you want to listen to")
    text_field = scrolledtext.ScrolledText(root, height=25, width=70, bg="light blue")
    text_field.grid(row=1, column=0)
    text_field_label.grid(row=0, column=0)

    return text_field


def create_buttons(root, text_field):

    # Add an Exit button
    exit_button = tk.Button(root, text="Exit", command=lambda: root.quit())
    exit_button.grid(row=3, column=0, padx=100)

    # Create a button to open another program and att it to the window
    run_button = tk.Button(root, text="Convert to audio", command=lambda: take_input(text_field))
    run_button.grid(row=2, column=0, pady=10, padx=100)


def main_build_window():
    # Create the main window and set the size of it
    root = tk.Tk()
    root.geometry("800x800")
    root.title("My little text to speech tool")

    text_field = create_text_field(root)
    create_buttons(root, text_field)

    # Show the window
    root.mainloop()


main_build_window()
