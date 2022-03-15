from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("CIT youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
# The label widget is used to display text that the user cannot modify
# Root is the name of the window variable we created at the top of the document
# Text is what will be displayed in the title of the label
# font sets what type of font will be written
# pack() organizes the widget in the window

# Create a field or textbox so the user can enter the link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)


# link is a string type variable that stores the YouTube link that the user enters
# Entry() widget is used when we want to create an input using tkinter
# width just sets the width of the widget
# textVariable is used to retrieve the value of current text variable to the entry of the widget
# place() is used to place items in a certain position using x and y coordinates

# Create Function to start downloading
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
# url variable takes the link using the get function and converts it into a string
# the video variable is downloaded in the first present stram of that video
# video download() method downloads the video


# Creates the button widget
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'black', fg = 'white', padx = 2, command = Downloader).place(x=180 ,y = 150)
# text - which we display on the label
# font in which the text is written
# bg sets the background color
# command is used to call function

root.mainloop() # The method used to executes when we want to run the program
