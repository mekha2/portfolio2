import tkinter as tk
from tkinter import messagebox
import pyttsx3


engine = pyttsx3.init()

engine.setProperty('rate',130)

def play_text():
    text = text_entry.get()
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال نص!")

def exit_app():
    root.destroy()

def set_text():
    text_entry.delete(0, tk.END)
    text_entry.insert(0, "")

def change_speed(value):
    engine.setProperty('rate', int(value))


root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x200")


label = tk.Label(root, text="Text to Speech", font=("Arial", 14))
label.pack(pady=10)


text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)




button_frame=tk.Frame(root)
button_frame.pack(pady=5)


play_button = tk.Button(button_frame, text="Play", command=play_text, width=10, bg="green")
play_button.pack(side="left",pady=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=10,bg="red")
exit_button.pack(side="left",padx=10)

set_button = tk.Button(button_frame, text="Set", command=set_text, width=10,bg="gray")
set_button.pack(side="left",padx=10)


root.mainloop()
