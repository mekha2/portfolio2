import tkinter as tk
#tkinter داله بتساعد عمل واجه التطبيق

from tkinter import messagebox
#messagebox اظهار رساله تنبيه 

import pyttsx3
#تحويل النص لصوت

engine = pyttsx3.init()
#تحويل النص لصوت

engine.setProperty('rate',130)
#سرعه 130 

def play_text():
    text = text_entry.get()
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال نص!")
        #لو المكان اللي بيتكتب فيه مليان ينطق الكلام ده 
        #لو المكان فاضي يحزرك

def exit_app():
    root.destroy()
    #اقفل البرنامج

def set_text():
    text_entry.delete(0, tk.END)
    text_entry.insert(0, "")
    #مسح الكلام من المريع
#ونسيب الخانه فاضيه

def change_speed(value):
    engine.setProperty('rate', int(value))
    #شريط يغير سرعه الصوت

root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x200")
#دي شكل التطبيق كله واللي مكتوب فيه وحجمه

label = tk.Label(root, text="Text to Speech", font=("Arial", 14))
label.pack(pady=10)
#عنوان التطبيق من فوق text to speech

text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)
#المربع اللي بكتب فيه

button_frame=tk.Frame(root)
button_frame.pack(pady=5)
#اطار احط فيه كل الازرار

play_button = tk.Button(button_frame, text="Play", command=play_text, width=10, bg="green")
play_button.pack(side="left",pady=10)
#زرار التشغيل الاخضر

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=10,bg="red")
exit_button.pack(side="left",padx=10)
#زرار الخروج الاحمر

set_button = tk.Button(button_frame, text="Set", command=set_text, width=10,bg="gray")
set_button.pack(side="left",padx=10)
#زرار المسح الرصاصي

root.mainloop()
