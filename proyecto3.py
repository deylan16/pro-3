from tkinter import *
from tkinter import ttk
from threading import Thread
from time import *


#define la ventana principal
principal = Tk()
principal.title('principal')
principal.configure(bg= 'white')

#fondo de la ventana
fondo = PhotoImage(file = "fondo_español.png")
fon = Label(principal,image = fondo,bg = 'black')
fon.place(x=0,y =0)
#pone la flevha de las monedas
flecha = PhotoImage(file = "fecha.png")
fle = Label(principal,image = flecha,bg = 'black')

#variable para abrir la billetera
m_colones =0
#monedas faltantes
monedas_faltantes = 200
#monedas ingresadas
monedas_ingresadas = 0
#contador de monedas ingresadas
titulo_contador = Label(principal,text = '₡' + str(monedas_ingresadas),font= ('Times New Roman',13),bg= 'black',fg= 'white')
#contador de monedas faltante
titulo_contadorf = Label(principal,text = '₡' + str(monedas_faltantes),font= ('Times New Roman',13),bg= 'black',fg= 'white')
#crea el titulo de ingresar dinero
titulo_inserte = Label(principal,text = 'Por favor inserte su dinero',font= ('Times New Roman',13),bg= 'black',fg= 'white')
#titulo de dinero ingresado
titulo_dinero = Label(principal,text = 'Dinero ingresado',font= ('Times New Roman',13),bg= 'black',fg= 'white')
#titulo de dinero faltante
titulo_dinerof = Label(principal,text = 'Dinero faltante',font= ('Times New Roman',13),bg= 'black',fg= 'white')
#titulo de imprimiendo tiquete
titulo_imprimiendo = Label(principal,text = 'Imprimiendo \n su \n tiquete',font= ('Times New Roman',25),bg= 'black',fg= 'white')
#titulo de tome su tiquete
titulo_tome= Label(principal,text = 'Por favor \n tome \n su \n tiquete',font= ('Times New Roman',25),bg= 'black',fg= 'white')

#imagnes de la impresion del boleto
boleto1 = PhotoImage(file = '1.png')
img = Label(principal,image = boleto1)
boleto2 = PhotoImage(file = '2.png')
boleto3 = PhotoImage(file = '3.png')
boleto4 = PhotoImage(file = '4.png')
boleto5 = PhotoImage(file = '5.png')
boleto6 = PhotoImage(file = '6.png')
boleto7 = PhotoImage(file = '7.png')
boleto8 = PhotoImage(file = '8.png')
boleto9 = PhotoImage(file = '9.png')
boleto10 = PhotoImage(file = '10.png')
boleto11 = PhotoImage(file = '11.png')
boleto12 = PhotoImage(file = '12.png')
boleto13 = PhotoImage(file = '13.png')
boleto14 = PhotoImage(file = '14.png')
boleto15 = PhotoImage(file = '15.png')
boleto16 = PhotoImage(file = '16.png')
boleto17 = PhotoImage(file = '17.png')
boleto18 = PhotoImage(file = '18.png')
boleto19 = PhotoImage(file = '19.png')
boleto20 = PhotoImage(file = '20.png')
boleto21 = PhotoImage(file = '21.png')





#lista con las imagenes de impresion del boleto
animacion = [boleto1,boleto2,boleto3,boleto4,boleto5,boleto6,boleto7,boleto8,boleto9,boleto10,boleto11,boleto12,boleto13,boleto14,boleto15,boleto16,boleto17,boleto18,boleto19,boleto20,boleto21,boleto21]
############################
#funcion para tomar el boletp
def tomar():
    boleto.place_forget()
    canvas = Canvas(principal , width= 400, height = 200, bg = "white")
    resultado = Label(canvas,text = 'TE AMO MI VIDA',font= ('Times New Roman',17),bg= 'white',fg= 'black')
    resultado.place(x=100,y=100)
    canvas.place(x=100, y=200)

#boton del boleto
boleto = Button(principal, image=boleto21,command = tomar)
#hilo
def imprimir1():
    return imprimir1_aux(animacion)

def imprimir1_aux(lista):
    if lista[1:] == []:
        img.place_forget()
        boleto.place(x= 425,y=177)
        titulo_imprimiendo.place_forget()
        titulo_tome.place(x=180,y=230)
        return lista[0]
    
    else:
        img.configure(image =lista[0])
        sleep(0.5)
        return imprimir1_aux(lista[1:])
def hilo1():
    t1 = Thread(target = imprimir1, args=())
    t1.start()

#E:numero de moneda que va ingresar
#S:contador de monedas ingresadas suma 25,resta 25 a monedas faltantes
#R:-
def suma_25():
    global monedas_ingresadas
    monedas_ingresadas += 25
    titulo_contador.configure(text= '₡' + str(monedas_ingresadas))
    global monedas_faltantes
    monedas_faltantes -= 25
    titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
    if monedas_faltantes <= 0:
        global m_colones
        m_colones.destroy()
        img.place(x=425,y = 177)
        titulo_inserte.place_forget()
        titulo_dinero.place_forget()
        titulo_dinerof.place_forget()
        titulo_contador.place_forget()
        titulo_contadorf.place_forget()
        fle.place_forget()
        titulo_imprimiendo.place(x= 180,y=250)
        hilo1()

#E:-
#S:contador de monedas ingresadas suma 50,resta 50 a monedas faltantes
#R:-
def suma_50():
    global monedas_ingresadas
    monedas_ingresadas += 50
    titulo_contador.configure(text= '₡' + str(monedas_ingresadas))
    global monedas_faltantes
    monedas_faltantes -= 50
    titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
    if monedas_faltantes <= 0:
        global m_colones
        m_colones.destroy()
        img.place(x=425,y = 177)
        titulo_inserte.place_forget()
        titulo_dinero.place_forget()
        titulo_dinerof.place_forget()
        titulo_contador.place_forget()
        titulo_contadorf.place_forget()
        fle.place_forget()
        titulo_imprimiendo.place(x= 180,y=250)
        hilo1()


#E:-
#S:contador de monedas ingresadas suma 100,resta 100 a monedas faltantes
#R:-
def suma_100():
    global monedas_ingresadas
    monedas_ingresadas += 100
    titulo_contador.configure(text= '₡' + str(monedas_ingresadas))
    global monedas_faltantes
    monedas_faltantes -= 100
    titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
    if monedas_faltantes <= 0:
        global m_colones
        m_colones.destroy()
        img.place(x=425,y = 177)
        titulo_inserte.place_forget()
        titulo_dinero.place_forget()
        titulo_dinerof.place_forget()
        titulo_contador.place_forget()
        titulo_contadorf.place_forget()
        fle.place_forget()
        titulo_imprimiendo.place(x= 180,y=250)
        hilo1()

        


#muetra la ventana con las monedas para ingresar
def colones():
    global m_colones
    m_colones = Toplevel()
    m_colones.title('billetera')
    m_colones.configure(bg= 'white')
    #imagen de la moneda 25
    m_25 = PhotoImage(file = "25.png")
    mo_25 = Label(m_colones,image = m_25,bg="white")
    mo_25.place(x=0,y =0)
    #boton de la moneda de 25
    Boton_25 = Button(m_colones,text= 'Insertar moneda',command = suma_25)
    Boton_25.place(x= 0,y=120)
    #imagen de la moneda 50
    m_50 = PhotoImage(file = "50.png")
    mo_50 = Label(m_colones,image = m_50,bg="white")
    mo_50.place(x=0,y =160)
    #boton de la moneda de 50
    Boton_50 = Button(m_colones,text= 'Insertar moneda',command = suma_50)
    Boton_50.place(x= 0,y=280)
    #imagen de la moneda 100
    m_100 = PhotoImage(file = "100.png")
    mo_100 = Label(m_colones,image = m_100,bg="white")
    mo_100.place(x=0,y =320)
    #boton de la moneda de 100
    Boton_100= Button(m_colones,text= 'Insertar moneda',command = suma_100)
    Boton_100.place(x= 0,y=440)
    
    m_colones.geometry('50x500+290+0')
    m_colones.mainloop()



#abre la maquina en español
def selecciono_español():
    #quita las coasas del primer menu
    titulo_español.place_forget()
    español.place_forget()
    titulo_ingles.place_forget()
    ingles.place_forget()
    titulo_inserte.place(x=150,y=200)
    fle.place(x=270,y =280)
    titulo_dinero.place(x=150,y=430)
    #pone contdor de monedas ingresadas 
    titulo_contador.place(x=150,y=450)
    
    titulo_dinerof.place(x=280,y=430)
    #pone contdor de monedas faltantes 
    titulo_contadorf.place(x=280,y=450)
    colones()

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
