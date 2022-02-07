from tkinter import*
from PIL import Image, ImageTk
#print('myname is Robo and I will help you calculate bind yields')
#coupon=float(input('What is the par value of the coupon?:'))
#interest_rate=float(input('What is the coupon interest rate?:'))
#market_price=float(input('What is the market price of the coupon?:'))


Font_tuple = ("Helvetica 10 italic")

fim=Tk()



#C = Canvas(fim, bg="#08dcfc", height=1000, width=300)
fim.geometry("350x250")
fim.resizable(0,0)
fim.iconbitmap('C:/Users/Kelvin/Desktop/python/finance.ico')
fim.title('Current Yield Calculator')
load= Image.open("/Users/Kelvin/Desktop/python/fim.png")



render = ImageTk.PhotoImage(load)
image = Label(fim, image=render)
image.place(x=1, y=1)



greet=Label(fim, text=" My name is Robo and I will help you calculate bond yields    ", font=Font_tuple,bg='#b7f7f7')
greet.place(x=2, y=1)
name=Label(fim, text="Par Value:", font=Font_tuple, bg='#b7f7f7')
name.place(x=30, y=30)
val=Entry(fim,bg='#08fcd8')
val.place(x=120,y =30)
intr=Label(fim, text='Interest rate:', font=Font_tuple, bg='#b7f7f7')
intr.place(x=30, y=60)
interest=Entry(fim, bg='#08fcd8')
interest.place(x=120,y=60)

price=Label(fim, text='Market price', font=Font_tuple,bg='#b7f7f7')
price.place(x=30, y=90)
priceentry=Entry(fim, bg='#08fcd8')
priceentry.place(x=120,y=90)

# appylying the formula where: iY=C/P but C=interest*coupon
def calculate():
    interest_rate=float(interest.get())
    par_value=float(val.get())
    C=interest_rate*par_value
    P=float(priceentry.get())
    coupon_yield=float(C/P)
    Iyield.config(text=coupon_yield)

calc=Button(fim, text='Calculate',command=calculate)
calc.place(x=150, y= 120)
Iyield=Label(fim,text="",font=Font_tuple, bg='#b7f7f7')
Iyield.place(x=120, y=150)


resized= load.resize((5,5), Image.ANTIALIAS)
#C.pack(fill='both',expand=True)

#magins left
margL=Label(fim, text='',height=100, bg='green')
margL.place(x=0, y=0)

#magins right
margL=Label(fim, text='',height=100, bg='blue')
margL.place(x=345, y=0)


fim.mainloop()


