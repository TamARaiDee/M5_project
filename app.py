from cProfile import label
from tkinter import *
from tkinter import Frame, Label, filedialog, Text
from PIL import Image, ImageTk
import os
import shutil

#create program with Tk function name root
root = Tk()

#name program
root.title("App No.1")

#window screen w x h
root.geometry("500x500")

#Add photo to frame and copy file to selected folder 
def Addphoto():

    #search file derectory
    filedirectory= filedialog.askopenfilename(initialdir="/", title="Select File",
              filetypes=(("all file", "*.*"), ("image", "*.jpg")))
    
    #print file directory in command line
    print(filedirectory)

    #copy file from filedirectory to /home/tatr/Project......
    shutil.copy(filedirectory, r'C:\Users\OWNER\Desktop\WORK\M5 proj\known.jpg' )
    cimg = r'C:\Users\OWNER\Desktop\WORK\M5 proj\known.jpg'

    #add text
    label_t = Label(frame, text = "You choose this photo?")
    label_t.pack()
    label_t2 = Label(frame, text = "If you want this photo to be data base click 'yes' button to select your folder for use this program")
    label_t2.pack()

    #show photo
    #watch in /home/tatar/Project/medel1/photo_test.py
    image = Image.open(cimg)
    zoom = 0.2
    pixels_x, pixels_y = tuple([int(zoom*x)for x in image.size])

    img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
    label = Label(frame, image=img)
    label.image = img
    label.pack()

    recive_face_button.pack_forget()
    cancel_img_button.pack()
    yes_button.pack()

#change image function
def cancel_img():

    #remove file at cimg
    cimg = r'C:\Users\OWNER\Desktop\WORK\M5 proj\known.jpg'
    os.remove(cimg)
    cancel_img_button.pack_forget()
    recive_face_button.pack()
    yes_button.pack_forget()

#Select folder function
def select_folder():
    global open_file
    open_file = filedialog.askdirectory() # Returns opened path as str
    cancel_img_button.pack_forget()
    yes_button.pack_forget()
    folder = Label(frame, text=open_file)
    folder.pack()
    yes_button.pack_forget()
    cancel_img_button.pack_forget()
    
#Destry frame
def destroy_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    print("frame has destroy")

#creat frame
frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#creat button
recive_face_button = Button(root, text="Choose photo", command=Addphoto)
recive_face_button.pack()

#change image Button
cancel_img_button = Button(root, text="Cancel", command=lambda:[destroy_frame(), cancel_img()]) 
cancel_img_button.pack_forget()

#yes button
yes_button = Button(root, text="yes", command=lambda:[destroy_frame(), select_folder()] )
yes_button.pack_forget()

#loop program always lowest
root.mainloop()
