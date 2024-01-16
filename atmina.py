from tkinter import* #importē tkinter
from PIL import ImageTk, Image
import random
from tkinter import messagebox

#ielādēt pillow, lai varētu ielikt bildes: pip install pillow

gameWindow=Tk()
gameWindow.title("Atmiņas spēle")

#######################################################################################################
count=0
winner=0
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
bgImg=ImageTk.PhotoImage(Image.open("7.png").resize((270,260)))#attēlu saspiešanas metode


##############################################################################################################3

ImageList=[myImg1, myImg1, myImg2, myImg2, myImg3, myImg3, myImg4, myImg4, myImg5, myImg5, myImg6, myImg6]

random.shuffle(ImageList) #attēli jāsajauc(attēli tiek sajaukti nejaušā secībā)

######################################################################################################################

def reset():
    global count, correctAnswers, answers, answer_dict, winner
    count=0
    winner=0
    correctAnswers=0
    answers=[]
    answer_dict={}
    btn0.config(state=NORMAL) #pogas stāvoklis izslēgts
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn10.config(state=NORMAL)
    btn11.config(state=NORMAL)

    btn0["image"]="pyimage7" #pogas attēlu maiņa
    btn1["image"]="pyimage7"
    btn2["image"]="pyimage7"
    btn3["image"]="pyimage7"
    btn4["image"]="pyimage7"
    btn5["image"]="pyimage7"
    btn6["image"]="pyimage7"
    btn7["image"]="pyimage7"
    btn8["image"]="pyimage7"
    btn9["image"]="pyimage7"
    btn10["image"]="pyimage7"
    btn11["image"]="pyimage7"

    random.shuffle(ImageList)

    return


###################################################################################################################

def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict, winner
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
                winner+=1
        else:
            messagebox.showinfo("Vienādi attēli","Neuzminēji")
            for key in answer_dict:
                key["image"]="pyimage7"
        count=0
        answers=[]
        answer_dict={}
    if winner==6:#ja ir 6 attēli atminēti, tad parāda, ka esi vinējis
        messagebox.showinfo("Vienādi attēli","Tu uzvarēji! Vai vēlies spēlēt vēlteiz?")
        reset()
    return

############################################################################################################

def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title('Info par programmu')
    jaunsLogs.geometry("680x200")
    jaunsLogs.configure(bg='#ECFFDC')
    apraksts=Label(jaunsLogs,text='Spēles noteikumi', font='Helvica 20 bold ', bg='#ECFFDC')#fonts, izmērs, stils
    apraksts.grid(row=0,column=0)
    apraksts=Label(jaunsLogs,text='Sākot spēli, spēlētājam jāapgriež divas kartiņas vienlaicīgi.', font='Helvica 14', bg='#ECFFDC')#fonts, izmērs, stils
    apraksts.grid(row=1,column=0)
    apraksts=Label(jaunsLogs,text='Ja simboli ir identiski, spēlētājs var minēt nākamos simbolus.', font='Helvica 14', bg='#ECFFDC')#fonts, izmērs, stils
    apraksts.grid(row=2,column=0)
    apraksts=Label(jaunsLogs,text='Ja simboli nav identiski, tās jāapgriež atpakaļ ar seju uz leju un var turpināt minēt.', font='Helvica 14', bg='#ECFFDC')#fonts, izmērs, stils
    apraksts.grid(row=3,column=0)
    apraksts=Label(jaunsLogs,text='Spēlētājs uzvar,. kad visus simbolus ir dabūjis vienādus.', font='Helvica 14', bg='#ECFFDC')#fonts, izmērs, stils
    apraksts.grid(row=4,column=0)
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

#Lielā izvēle
galvenaIzvele=Menu(gameWindow)#izveido galveno izvēli
gameWindow.config(menu=galvenaIzvele)#pievieno galvenajam logam

opcijas=Menu(galvenaIzvele,tearoff=False)#mazā izvēle
galvenaIzvele.add_cascade(label="Opcijas", menu=opcijas)#lejupkrītošais saraksts
galvenaIzvele.add_command(label="Par programmu",command=infoLogs) # pievieno mazajai izvēlnei vēl vienu izvēlni


#Komandas
opcijas.add_command(label="Jauna spēle", command=reset)#pievieno kommandu, priekš atvēršanas jaunajam logam
opcijas.add_command(label="Iziet", command=gameWindow.quit)#iziet no loga

##########################################################################################################

btn0.grid(row=0,column=0)#pogu novietojums
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