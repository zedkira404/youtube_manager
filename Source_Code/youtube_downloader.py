from pytube import YouTube
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
import threading

root = tk.Tk()
root.resizable(0, 0)
#root.geometry('360x280+200+200')
root.title("YouTube Downloader")
#root.configure(background='#414042')#939598 #BC0022

def settings():
    messagebox.showerror("ZedKira" ,"Not done yet !!")

w = Menu(root)
help = Menu(w, tearoff=0)
help.add_command(label="Show Use",command=settings)
help.add_command(label="more info",command=settings)
w.add_cascade(label="Help", menu=help)

w.add_command(label="Edit",command=settings)
w.add_command(label="Exit",command=root.destroy)

#img = ImageTk.PhotoImage(Image.open("Capture2_ytb.png"))
#img_label = tk.Label(root, image = img)
#img_label.grid(row=1, column=1, padx = 10)


path_txt = StringVar()
path_txt.set("")

url_txt = StringVar() #used to edit  widget's text
url_txt.set("")

path_save = ""
video_link = ""

def entry():
    cnd1 = str(path_txt.get())
    cnd2 = str(url_txt.get())
    if cnd1 == "" or cnd2 == "":
        messagebox.showerror("Youtube", "Please , put a valid path and link!!")
    else:
        global path_save
        global video_link
        path_save = str(path_txt.get())
        video_link = str(url_txt.get())
        path_txt.set("Done!!")
        url_txt.set("Click the download button below!!")


def download():
    try:
        YouTube(video_link).streams.first().download(path_save)
        path_txt.set("")
        url_txt.set("")
        root.destroy()
        messagebox.showinfo("Youtube", "Download Finished Successfully!!")

    except Exception as ex:
        path_txt.set("")
        url_txt.set("")
        messagebox.showerror("Error", ex)
        messagebox.showerror("Error", "Check your connection!!")
        root.destroy()

def show_progress():
    path_txt.set("Downloading...")
    url_txt.set("Downloading...")

def my_thread():
    thread = threading.Thread(target=download)
    thread.start()
    show_progress()


frame = LabelFrame(root, text = "Video information")
frame.grid(row=1, column=0, padx=20, pady=20)

lbl1 = tk.Label(frame,text="Enter a Path to save" , foreground="#414042" )
lbl1.pack()

path_entry1 = Entry(frame,textvariable=path_txt,width=50)
path_entry1.pack()
path_entry1.focus()

lbl = tk.Label(frame,text="Enter a URL" , foreground="#414042")
lbl.pack()

url_entry = ttk.Entry(frame,textvariable=url_txt,width=50)
url_entry.pack()

bt2 = tk.Button(frame, text='Enter',width=10, height=1,cursor="hand2",borderwidth=5,command=entry,foreground="#414042")
bt2.pack()

bt1 = tk.Button(root, text='Download',width=10, height=1 ,cursor="hand2",borderwidth=5,command=my_thread,foreground="#414042")
bt1.grid(row=2, column=0, padx=5, pady=10)


root.config(menu=w)
root.mainloop()


#C:\Users\zedkira\Desktop\videos
#https://youtu.be/GYuelKjcyPs
