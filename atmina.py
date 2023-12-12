from tkinter import* #importē tkinter
from PIL import ImageTk, Image
import random
from tkinter import messagebox

#ielādēt pillow, lai varētu ielikt bildes: pip install pillow

gameWindow=Tk()
gameWindow.title("Atmiņas spēle")

#########################################################################################################

myImg1=ImageTk.PhotoImage(Image.open("1.jpg"))
myImg2=ImageTk.PhotoImage(Image.open("2.jpg"))
myImg3=ImageTk.PhotoImage(Image.open("3.png"))
myImg4=ImageTk.PhotoImage(Image.open("4.png"))
myImg5=ImageTk.PhotoImage(Image.open("5.jpg"))
myImg6=ImageTk.PhotoImage(Image.open("6.png"))



#Fona attēls:
bgImg=ImageTk.PhotoImage(Image.open("7.jpg").resize((200,200)))#attēlu saspiešanas metode

#Attēla izmērs


##########################################################################################################

btn0=Button(width=200,height=200,image=bgImg)#sāk no 0, jo saistās ar saraksta elementu indeksāciju
btn1=Button(width=200,height=200,image=bgImg)
btn2=Button(width=200,height=200,image=bgImg)
btn3=Button(width=200,height=200,image=bgImg)
btn4=Button(width=200,height=200,image=bgImg)
btn5=Button(width=200,height=200,image=bgImg)
btn6=Button(width=200,height=200,image=bgImg)
btn7=Button(width=200,height=200,image=bgImg)
btn8=Button(width=200,height=200,image=bgImg)
btn9=Button(width=200,height=200,image=bgImg)
btn10=Button(width=200,height=200,image=bgImg)
btn11=Button(width=200,height=200,image=bgImg)

##########################################################################################################



##########################################################################################################

btn0.grid(row=0,column=0)
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=1,column=0)
btn4.grid(row=1,column=1)
btn5.grid(row=1,column=2)
btn6.grid(row=2,column=0)
btn7.grid(row=2,column=1)
btn8.grid(row=2,column=2)
btn9.grid(row=3,column=0)
btn10.grid(row=3,column=1)
btn11.grid(row=3,column=2)


gameWindow.mainloop()