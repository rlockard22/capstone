from fileinput import filename
from http import client
from importlib.resources import path
from operator import truediv
from tkinter.filedialog import askopenfilename
from matplotlib import image
from matplotlib.pyplot import text
from paramiko import SSHClient
import paramiko
import os
import sqlite3
from tkinter import *

my_text = ''

def select_image_event():
    filename = askopenfilename()
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="ssh.pythonanywhere.com", username="rlockard", password="Baseball2@")
    sftp = ssh.open_sftp()
    sftp.chdir(path="/home/rlockard/mysite/static")
    remote_name = artwork_entry_return.get()
    remote_name = remote_name + '.jpg'
    image_name.set(filename)
    sftp.put(localpath=filename, remotepath=remote_name)
    
def select_mp3_event():
    filename = askopenfilename()
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="ssh.pythonanywhere.com", username="rlockard", password="Baseball2@")
    sftp = ssh.open_sftp()
    sftp.chdir(path="/home/rlockard/mysite/static")
    remote_name = artwork_entry_return.get()
    remote_name = remote_name + '.mp3'
    mp3_name.set(filename)
    sftp.put(localpath=filename, remotepath=remote_name)
    
def select_txt_event():
    filename = askopenfilename()
    f = open(filename)
    text = f.read()
    temp = open("temp.txt", "w+")
    temp.write(text)
    temp.close()
    description_entry_return.set(filename)
    f.close()
    
    
    print(text)
    
    
def select_db_event():
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="ssh.pythonanywhere.com", username="rlockard", password="Baseball2@")
    
    sftp = ssh.open_sftp()
    sftp.get(remotepath='master.db', localpath='master.db')
    db_connection = sqlite3.connect('master.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    name = artwork_entry_return.get()
    artist = artist_entry_return.get()
    date = date_entry_return.get()
    f = open('temp.txt')
    text = f.read()
    description = text
    image_name = name + '.jpg'
    mp3_name = name + '.mp3'
    
    sql = "INSERT INTO eskenazi (name, artist, date, description, image_file_name, audio) VALUES (?, ?, ?, ?, ?, ?)"
    db_cursor.execute(sql, (name, artist, date, description, image_name, mp3_name))
    db_connection.commit()
    db_connection.close()
    
    sftp.put(localpath='master.db', remotepath='master.db')
    sftp.close()
    
    

root = Tk()
root.title('Python Database Interface')
root.geometry("1000x1000")
#my_canvas = Canvas(root, width=950, height=950)
#my_canvas.pack(fill="both", expand=True)
artwork_entry_return = StringVar()
artwork_entry_return.set('')
artwork_label = Label(root, text="Artwork Name").grid(column=0,row=0, pady=5)
artwork_entry = Entry(root, textvariable=artwork_entry_return).grid(column=1,row=0, pady=5)

artist_entry_return = StringVar()
artist_entry_return.set('')
artist_label = Label(root, text="Artist Name").grid(column=0,row=1, pady=5)
artist_entry = Entry(root, textvariable=artist_entry_return).grid(column=1,row=1, pady=5)

date_entry_return = StringVar()
date_entry_return.set('')
date_label = Label(root, text="Date").grid(column=0,row=2, pady=5)
date_entry = Entry(root, textvariable=date_entry_return).grid(column=1,row=2, pady=5)

description_entry_return = StringVar()
description_entry_return.set('')
description_label = Label(root, text="Description").grid(column=0,row=3, pady=5)
description_button = Button(root, text="Upload .txt Here", command=select_txt_event).grid(column=1, row=3, pady=5)
description_file_label = Label(root, textvariable=description_entry_return).grid(column=2, row=3, pady=5)

image_name = StringVar()
image_name.set('')
image_label = Label(root, text="Select Image Uploade File").grid(column=0, row=4, pady=5)
image_button = Button(root, text="Upload .jpg Here", command=select_image_event).grid(column=1, row=4, pady=5)
image_name_label = Label(root, textvariable=image_name).grid(column=2, row=4, pady=5)

mp3_name = StringVar()
mp3_name.set('')
mp3_label = Label(root, text="Select MP3 Upload File").grid(column=0, row=5, pady=5)
mp3_button = Button(root, text="Upload .mp3 Here", command=select_mp3_event).grid(column=1, row=5, pady=5)
mp3_name_label = Label(root, textvariable=mp3_name).grid(column=2, row=5, pady=5)


export_button = Button(root, text="EXPORT TO DATABASE", command=select_db_event).grid(column=1, row=6)






root.mainloop()


#ssh = SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname="ssh.pythonanywhere.com", username="rlockard", password="Baseball2@")
#current = os.getcwd()
#image_path = current + '\static\homage_to_the_square.jpg'
#sftp = ssh.open_sftp()
#sftp.get(remotepath='master.db', localpath='master.db')
#db_connection = sqlite3.connect('master.db', check_same_thread=False)
#db_cursor = db_connection.cursor()
#my_text = "hello"
#sql = "INSERT INTO eskenazi (location, name, artist, description) VALUES (?, ?, ?, ?)"
#db_cursor.execute(sql, ('Modern Art', 'The Studio', 'Pablo Picasso', my_text))
#db_connection.commit()
#db_connection.close()
#sftp.chdir(path="/home/rlockard/mysite/static")
#sftp.put(localpath=image_path, remotepath='it_uploaded.jpg')
#sftp.put(localpath='master.db', remotepath='master.db')
#sftp.close()
