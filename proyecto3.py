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
#crea el titulo de ingresar dinero(español e ingles)
tituloe_inserte = Label(principal,text = 'Por favor inserte su dinero',font= ('Times New Roman',13),bg= 'black',fg= 'white')
tituloi_inserte = Label(principal,text = 'Please insert your money',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
#titulo de dinero ingresado(español e ingles)
tituloe_dinero = Label(principal,text = 'Dinero ingresado',font= ('Times New Roman',13),bg= 'black',fg= 'white')
tituloi_dinero = Label(principal,text = 'Money entered',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
#titulo de dinero faltante(español e ingles)
tituloe_dinerof = Label(principal,text = 'Dinero faltante',font= ('Times New Roman',13),bg= 'black',fg= 'white')
tituloi_dinerof = Label(principal,text = 'Dinero missing',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
#titulo de imprimiendo tiquete(español e ingles)
tituloe_imprimiendo = Label(principal,text = 'Imprimiendo \n su \n tiquete',font= ('Times New Roman',25),bg= 'black',fg= 'white')
tituloi_imprimiendo = Label(principal,text = 'Printing \nyour \nticket',font= ('Times New Roman',22),bg= 'black',fg= 'light blue')
#titulo de tome su tiquete(español e ingles)
tituloe_tome= Label(principal,text = 'Por favor \n tome  su \n tiquete',font= ('Times New Roman',25),bg= 'black',fg= 'white')
tituloi_tome = Label(principal,text = 'please take \n it your \n ticket',font= ('Times New Roman',22),bg= 'black',fg= 'light blue')
#titulo de desea hacerlo otra vez(español e ingles)
tituloe_vuelto= Label(principal,text = 'Por favor \n tome  su \n vuelto',font= ('Times New Roman',25),bg= 'black',fg= 'white')
tituloi_vuelto = Label(principal,text = 'please take \n it your \n turned',font= ('Times New Roman',22),bg= 'black',fg= 'light blue')

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
#variable para crear el canvas
canvas = 0

#E:-
#S:guarda(elimina el canvas) el tiquete
#R:-
def guardar():
    canvas.place_forget()
    boleto_guardar.place_forget()
#boton de guardar boleto
boleto_guardar = Button(principal, text = 'Guadar',command = guardar)

#E:-
#S:vuelve al primer menu
#R:-



#E:-
#S:enseña el tiquete al usuario
#R:-
def tomar():
    tituloe_tome.place_forget()
    tituloi_tome.place_forget()
    boleto.place_forget()
    tituloe_vuelto.place(x= 170,y=200)
    tituloi_vuelto.place(x= 170,y=350)
    global canvas
    canvas = Canvas(principal , width= 400, height = 200, bg = "white")
    resultado = Label(canvas,text = 'TE AMO MI VIDA',font= ('Times New Roman',17),bg= 'white',fg= 'black')
    resultado.place(x=100,y=100)
    canvas.place(x=100, y=200)
    boleto_guardar.place(x=400,y=400)
    

#boton del tomar el boleto
boleto = Button(principal, image=boleto21,command = tomar)
#hilo
def imprimir1():
    return imprimir1_aux(animacion)

def imprimir1_aux(lista):
    if lista[1:] == []:
        img.place_forget()
        boleto.place(x= 425,y=177)
        tituloe_imprimiendo.place_forget()
        tituloi_imprimiendo.place_forget()
        tituloe_tome.place(x= 200,y=200)
        tituloi_tome.place(x= 200,y=350)
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
        segunda =[tituloe_inserte.place_forget(),tituloi_inserte.place_forget(),tituloe_dinero.place_forget(),tituloi_dinero.place_forget(),tituloe_dinerof.place_forget(),
                  tituloi_dinerof.place_forget(),titulo_contador.place_forget(),titulo_contadorf.place_forget(),fle.place_forget()]
        tituloe_imprimiendo.place(x= 180,y=200)
        tituloi_imprimiendo.place(x= 220,y=350)
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
        segunda =[tituloe_inserte.place_forget(),tituloi_inserte.place_forget(),tituloe_dinero.place_forget(),tituloi_dinero.place_forget(),tituloe_dinerof.place_forget(),
                  tituloi_dinerof.place_forget(),titulo_contador.place_forget(),titulo_contadorf.place_forget(),fle.place_forget()]
        tituloe_imprimiendo.place(x= 180,y=200)
        tituloi_imprimiendo.place(x= 220,y=350)
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
        segunda =[tituloe_inserte.place_forget(),tituloi_inserte.place_forget(),tituloe_dinero.place_forget(),tituloi_dinero.place_forget(),tituloe_dinerof.place_forget(),
                  tituloi_dinerof.place_forget(),titulo_contador.place_forget(),titulo_contadorf.place_forget(),fle.place_forget()]
        tituloe_imprimiendo.place(x= 180,y=200)
        tituloi_imprimiendo.place(x= 220,y=350)
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



#E:-
#S:menu de consejos
#R:-
def selecciono_consejo():
    #quita las coasas del primer menu
    primera = [titulo_bienvenidoe.place_forget(),titulo_bienvenidoi.place_forget(),consejo.place_forget(),dicho.place_forget(),Chistes.place_forget(),
               pe_consejo.place_forget(),pi_consejo.place_forget(),pe_dicho.place_forget(),pi_dicho.place_forget(),pe_Chistes.place_forget(),pi_Chistes.place_forget()]
    global monedas_faltantes
    monedas_faltantes = 20
    titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
    segundap = [titulo_contador,titulo_contadorf,tituloe_inserte.place(x=150,y=200),tituloi_inserte.place(x=150,y=220),tituloe_dinerof.place(x=280,y=410),
                tituloi_dinerof.place(x=280,y=430),tituloe_dinero.place(x=150,y=410),tituloi_dinero.place(x=150,y=430),titulo_contador.place(x=150,y=450),
                titulo_contadorf.place(x=280,y=450),fle.place(x=270,y =280)]
     
    colones()
#E:-
#S:menu de consejos
#R:-
def selecciono_dicho():
    #quita las coasas del primer menu
    primera = [titulo_bienvenidoe.place_forget(),titulo_bienvenidoi.place_forget(),consejo.place_forget(),dicho.place_forget(),Chistes.place_forget(),
               pe_consejo.place_forget(),pi_consejo.place_forget(),pe_dicho.place_forget(),pi_dicho.place_forget(),pe_Chistes.place_forget(),pi_Chistes.place_forget()]
    global monedas_faltantes
    monedas_faltantes = 100
    titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
    segundap = [titulo_contador,titulo_contadorf,tituloe_inserte.place(x=150,y=200),tituloi_inserte.place(x=150,y=220),tituloe_dinerof.place(x=280,y=410),
                tituloi_dinerof.place(x=280,y=430),tituloe_dinero.place(x=150,y=410),tituloi_dinero.place(x=150,y=430),titulo_contador.place(x=150,y=450),
                titulo_contadorf.place(x=280,y=450),fle.place(x=270,y =280)]
    colones()
#E:-
#S:menu de consejos
#R:-
def selecciono_chiste():
    #quita las coasas del primer menu
    primera = [titulo_bienvenidoe.place_forget(),titulo_bienvenidoi.place_forget(),consejo.place_forget(),dicho.place_forget(),Chistes.place_forget(),
               pe_consejo.place_forget(),pi_consejo.place_forget(),pe_dicho.place_forget(),pi_dicho.place_forget(),pe_Chistes.place_forget(),pi_Chistes.place_forget()]
    global monedas_faltantes
    monedas_faltantes = 150
    titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
    segundap = [titulo_contador,titulo_contadorf,tituloe_inserte.place(x=150,y=200),tituloi_inserte.place(x=150,y=220),tituloe_dinerof.place(x=280,y=410),
                tituloi_dinerof.place(x=280,y=430),tituloe_dinero.place(x=150,y=410),tituloi_dinero.place(x=150,y=430),titulo_contador.place(x=150,y=450),
                titulo_contadorf.place(x=280,y=450),fle.place(x=270,y =280)]
    colones()

#titulos bienevenido (español e ingles)
titulo_bienvenidoe = Label(principal,text = 'Bienvenido ¿Que desea obtener?',font= ('Times New Roman',13),bg= 'black',fg= 'white')
titulo_bienvenidoe.place(x=150,y=200)
titulo_bienvenidoi = Label(principal,text = 'Welcome ¿What do you want to get?',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
titulo_bienvenidoi.place(x=160,y=220)




#boton para consejo
consejo= Button(principal,text= '  Consejo \n (Advice)',command= selecciono_consejo)
consejo.place(x= 150,y=300)
#precio del consejo (español e ingles)
pe_consejo = Label(principal,text = 'Precio: ₡20 ',font= ('Times New Roman',9),bg= 'black',fg= 'white')
pe_consejo.place(x=150,y=343)
pi_consejo = Label(principal,text = 'Price: ₡20 ',font= ('Times New Roman',9),bg= 'black',fg= 'light blue')
pi_consejo.place(x=150,y=362)

#boton para dicho
dicho= Button(principal,text= '  Dicho \n (Saying)',command= selecciono_dicho)
dicho.place(x= 300,y=300)
#precio del dicho (español e ingles)
pe_dicho = Label(principal,text = 'Precio: ₡100 ',font= ('Times New Roman',9),bg= 'black',fg= 'white')
pe_dicho.place(x=300,y=343)
pi_dicho = Label(principal,text = 'Price: ₡100 ',font= ('Times New Roman',9),bg= 'black',fg= 'light blue')
pi_dicho.place(x=300,y=362)
#boton para Chistes
Chistes= Button(principal,text= '  Chistes \n (Jokes)',command= selecciono_chiste)
Chistes.place(x= 220,y=380)

#precio del Chistes (español e ingles)
pe_Chistes = Label(principal,text = 'Precio: ₡150 ',font= ('Times New Roman',9),bg= 'black',fg= 'white')
pe_Chistes.place(x=220,y=423)
pi_Chistes = Label(principal,text = 'Price: ₡150 ',font= ('Times New Roman',9),bg= 'black',fg= 'light blue')
pi_Chistes.place(x=220,y=442)


 

#tamaño de la ventana
principal.geometry('600x700+400+0')
principal.mainloop()
