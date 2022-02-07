from instapy import InstaPy
from tkinter import StringVar
from pyvirtualdisplay import Display
from tkinter import*

#see instapy documentation for more command options
def gui():
    session=InstaPy(username=str(ename.get()),
        password=str(passw1.get()))
    session.login()
    session.follow_by_tags( [str(nametags.get())], amount=int(number.get()))
    
#def name():
    #name1=ename.get()
    
#def passw():
    #passw=passw1.get()
Font_tuple = ("Comic Sans MS", 10, "bold")
fonts=("Courier", 10, "italic")

from PIL import Image, ImageTk


#GUI begins here
root=Tk()
root.iconbitmap('C:/Users/Kelvin/Desktop/python/robot.ico')
root.title('Robo')
root.resizable(0,0)
root.geometry("450x150")
root.configure(bg='#73f5ee')

load= Image.open("/Users/Kelvin/Desktop/python/insta3.png")



render = ImageTk.PhotoImage(load)
image = Label(root, image=render)
image.place(x=1, y=1)


greet=Label(root,borderwidth="2", relief="groove", text='Hello, I am Robo. I am here to help you manage your instagram', font=Font_tuple)
greet.place(x=15, y=1)
name=Label(root, text='Username', font=fonts)
name.place(x=50, y=25)
ename=Entry(root,text='username', bg='#fcf8cf', textvariable=name, font=fonts)
ename.place(x=150, y =28)
pass1=Label(root, text='Password',font=fonts)
pass1.place(x=50, y=50)
passw1=Entry(root,show='*', bg='#fcf8cf', font=fonts)
passw1.place(x=150, y=52)
nametagging=Label(root,text='Tag               ')
nametagging.place(x=50, y=75)
nametags=Entry(root, bg='#fcf8cf', font=fonts)
nametags.place(x=150, y=75)
amount_to_follow=Label(root, text='No. of tags  ')
amount_to_follow.place(x=50, y=98)
number=Entry(root, bg='#fcf8cf', font=fonts)
number.place(x=150, y=98)
run=Button(root, text='Run', command=gui, font=fonts,bg='#0004ff')
run.place(x=180, y=125)

#margins left
dec1=Label(root, text='',bg='red')
dec1.place(x=0,y=0)
dec2=Label(root, text='',bg='red')
dec2.place(x=0,y=20)
dec3=Label(root, text='',bg='red')
dec3.place(x=0,y=30)
dec4=Label(root, text='',bg='red')
dec4.place(x=0,y=40)
dec5=Label(root, text='',bg='red',height=50)
dec5.place(x=0,y=50)

#margins right
decr1=Label(root, text='', bg='yellow',height=100, width=5)
decr1.place(x=445, y=0)


resized= load.resize((5,5), Image.ANTIALIAS)

root.mainloop()

#username=StringVar()
