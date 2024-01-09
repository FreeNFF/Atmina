from tkinter import* #importē tkinter
from PIL import ImageTk, Image
import random
from tkinter import messagebox

#ielādēt pillow, lai varētu ielikt bildes: pip install pillow

gameWindow=Tk()
gameWindow.title("Atmiņas spēle")

#######################################################################################################
count=0
correctAnswers=0
answers=[]
answer_dict={}#kas ir piespiests, salīdzinās ar attēliem no saraksta

#########################################################################################################

myImg1=ImageTk.PhotoImage(Image.open("1.jpg").resize((200,200)))
myImg2=ImageTk.PhotoImage(Image.open("2.jpg").resize((200,200)))
myImg3=ImageTk.PhotoImage(Image.open("3.png").resize((200,200)))
myImg4=ImageTk.PhotoImage(Image.open("4.png").resize((200,200)))
myImg5=ImageTk.PhotoImage(Image.open("5.jpg").resize((200,200)))
myImg6=ImageTk.PhotoImage(Image.open("6.png").resize((200,200)))



#Fona attēls:
bgImg=ImageTk.PhotoImage(Image.open("7.jpg").resize((360,250)))#attēlu saspiešanas metode

##############################################################################################################3

ImageList=[myImg1, myImg1, myImg2, myImg2, myImg3, myImg3, myImg4, myImg4, myImg5, myImg5, myImg6, myImg6]

random.shuffle(ImageList) #attēli jāsajauc(attēli tiek sajaukti nejaušā secībā)

###################################################################################################################

def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict,winner
    if btn["image"] == "pyimage7" and count<2:#pēc sistēmas nosauc šādi'
        btn["image"]=ImageList[number]
        count+=1#viena rūtiņa atklāta
        answers.append(number)#pievieno pie atbildēm
        answer_dict[btn]=ImageList[number]
    if len(answers)==2:#ja atvērtas divas kartītes
        if ImageList[answers[0]]==ImageList[answers[1]]:#salīdzina attēlus, kas saglabāts vārdņīcā ar attēlu sarakstā
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswers+=2
            if correctAnswers==2:
                messagebox.showinfo("Vienādi attēli", "Esi uzminējis")
                correctAnswers=0
            if correctAnswers==6:
                messagebox.showinfo("Vienādi attēli","Tu uzvarēji! Vai vēlies spēlēt vēreiz?")
        else:
            messagebox.showinfo("Vienādi attēli","Neuzminēji")
            for key in answer_dict:
                key["image"]="pyimage7"
        count=0
        answers=[]
        answer_dict={}
    return

##########################################################################################################

btn0=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn0,0))#sāk no 0, jo saistās ar saraksta elementu indeksāciju
btn1=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn9,9))
btn10=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn10,10))
btn11=Button(width=200,height=200,image=bgImg, command=lambda:btnClick(btn11,11))

##########################################################################################################



##########################################################################################################

btn0.grid(row=0,column=0)
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=0,column=3)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=1,column=3)
btn8.grid(row=2,column=0)
btn9.grid(row=2,column=1)
btn10.grid(row=2,column=2)
btn11.grid(row=2,column=3)


gameWindow.mainloop()