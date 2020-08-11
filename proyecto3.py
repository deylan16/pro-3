from tkinter import *
from tkinter import ttk


#define la ventana principal
principal = Tk()
principal.title('principal')
principal.configure(bg= 'white')

#fondo de la ventana
fondo = PhotoImage(file = "fondo_español.png")
fon = Label(principal,image = fondo,bg = 'black')
fon.place(x=0,y =0)
#abre la maquina en español
def selecciono_español():
    titulo_español.place_forget()
    español.place_forget()
    titulo_ingles.place_forget()
    ingles.place_forget()
    

#titulo para sleccionar el idioma en español
titulo_español = Label(principal,text = '¿Desea el idioma en español?',font= ('Times New Roman',13),bg= 'black',fg= 'white')
titulo_español.place(x=150,y=200)
#boton para selccionar español
español = Button(principal,text= 'OPRIMA AQUI',command= selecciono_español)
español.place(x= 220,y=250)

#titulo para sleccionar el idioma en ingles
titulo_ingles = Label(principal,text = '¿You want the language in English?',font= ('Times New Roman',13),bg= 'black',fg= 'white')
titulo_ingles.place(x=135,y=300)

#boton para selccionar INGLES
ingles = Button(principal,text= 'CLICK HERE')
ingles.place(x= 220,y=350)


    

#tamaño de la ventana
principal.geometry('600x700+400+0')
principal.mainloop()
