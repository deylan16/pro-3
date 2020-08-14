from tkinter import *
from tkinter import ttk
from threading import Thread
from time import *
from tkinter import messagebox
from random import *
import random
from tabla_ventas import *

#define la ventana principal
principal = Tk()
principal.title('Advice Machine')
principal.configure(bg= 'white')

#fondo de la ventana
fondo = PhotoImage(file = "fondo_español.png")
fon = Label(principal,image = fondo,bg = 'black')
fon.place(x=0,y =0)
#pone la flevha de las monedas
flecha = PhotoImage(file = "flecha.png")
fle = Label(principal,image = flecha,bg = 'black')
#variable par ausar el boton regresar
bandera_regresar = False
#varaiable para no poder volver a usar admi
bandera_admi = True
#variable tiquete
tiqueteale=0
#variable que cuenta cuantas monedas de vuelto hay
cuenta = 0
#variable para abrir la billetera
m_colones =0
#variables de ventas
venta11 = 0
venta12=0
venta13=0
venta14=0
venta15=0
venta16=0
venta17=0
venta18=0
venta19=0
venta110=0
venta111=0
venta112=0
venta113=0
venta114=0
venta115=0
venta116=0
venta21 = 0
venta22=0
venta23=0
venta24=0
venta25=0
venta26=0
venta27=0
venta28=0
venta29=0
venta210=0
venta211=0
venta212=0
venta213=0
venta214=0
venta215=0
venta216=0
venta217=0
venta31 = 0
venta32=0
venta33=0
venta34=0
venta35=0
venta36=0
venta37=0
venta38=0
venta39=0
venta310=0
venta311=0
venta312=0
venta313=0
venta314=0
venta315=0
venta316=0
venta317=0
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
#titulo de digite la contraseña
titulo_contraseñae = Label(principal,text = 'Por favor digite si contaseña',font= ('Times New Roman',13),bg= 'black',fg= 'white')
titulo_contraseñai = Label(principal,text = 'Please enter your password',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
#titulo de bienvenido al admi
titulo_admie = Label(principal,text = 'Bienvenido Admi',font= ('Times New Roman',13),bg= 'black',fg= 'white')
titulo_admii = Label(principal,text = 'Welcome Admi',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
#titulo de gracias y si desea hacerlo otra vez
titulo_graciase= Label(principal,text = 'Muchas Gracias \n si desea comprar \n otro  \n oprima regresar',font= ('Times New Roman',21),bg= 'black',fg= 'white')
titulo_graciasi = Label(principal,text = 'Thank you very \n much if you want \nto buy another \n  press return',font= ('Times New Roman',18),bg= 'black',fg= 'light blue')



#imagnes de la impresion del boleto
boleto1 = PhotoImage(file = 'a_tiquete/1.png')
img = Label(principal,image = boleto1)
boleto2 = PhotoImage(file = 'a_tiquete/2.png')
boleto3 = PhotoImage(file = 'a_tiquete/3.png')
boleto4 = PhotoImage(file = 'a_tiquete/4.png')
boleto5 = PhotoImage(file = 'a_tiquete/5.png')
boleto6 = PhotoImage(file = 'a_tiquete/6.png')
boleto7 = PhotoImage(file = 'a_tiquete/7.png')
boleto8 = PhotoImage(file = 'a_tiquete/8.png')
boleto9 = PhotoImage(file = 'a_tiquete/9.png')
boleto10 = PhotoImage(file = 'a_tiquete/10.png')
boleto11 = PhotoImage(file = 'a_tiquete/11.png')
boleto12 = PhotoImage(file = 'a_tiquete/12.png')
boleto13 = PhotoImage(file = 'a_tiquete/13.png')
boleto14 = PhotoImage(file = 'a_tiquete/14.png')
boleto15 = PhotoImage(file = 'a_tiquete/15.png')
boleto16 = PhotoImage(file = 'a_tiquete/16.png')
boleto17 = PhotoImage(file = 'a_tiquete/17.png')
boleto18 = PhotoImage(file = 'a_tiquete/18.png')
boleto19 = PhotoImage(file = 'a_tiquete/19.png')
boleto20 = PhotoImage(file = 'a_tiquete/20.png')
boleto21 = PhotoImage(file = 'a_tiquete/21.png')





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
#animacion del vuelto
#imagenes del 5
vuelto5 = PhotoImage(file = "5/vuelto5.png")
vuelto51 = PhotoImage(file = "5/vuelto51.png")
vuelto52 = PhotoImage(file = "5/vuelto52.png")
vuelto53 = PhotoImage(file = "5/vuelto53.png")
vuelto54 = PhotoImage(file = "5/vuelto54.png")
vuelto55 = PhotoImage(file = "5/vuelto55.png")
vuelt5 = Label(principal,image = vuelto5,bg ="#555869")
animacion5= [vuelto55,vuelto54,vuelto53,vuelto52,vuelto51,vuelto5,vuelto5]
#imagenes del 10
vuelto10 = PhotoImage(file = "10/vuelto10.png")
vuelto101 = PhotoImage(file = "10/vuelto101.png")
vuelto102 = PhotoImage(file = "10/vuelto102.png")
vuelto103 = PhotoImage(file = "10/vuelto103.png")
vuelto104 = PhotoImage(file = "10/vuelto104.png")
vuelto105 = PhotoImage(file = "10/vuelto105.png")
vuelt10 = Label(principal,image = vuelto10,bg ="#555869")
animacion10= [vuelto105,vuelto104,vuelto103,vuelto102,vuelto101,vuelto10,vuelto10]
#imagenes del 25
vuelto25 = PhotoImage(file = "25/vuelto25.png")
vuelto251 = PhotoImage(file = "25/vuelto251.png")
vuelto252 = PhotoImage(file = "25/vuelto252.png")
vuelto253 = PhotoImage(file = "25/vuelto253.png")
vuelto254 = PhotoImage(file = "25/vuelto254.png")
vuelto255 = PhotoImage(file = "25/vuelto255.png")
vuelt25 = Label(principal,image = vuelto25,bg ="#555869")
animacion25 = [vuelto255,vuelto254,vuelto253,vuelto252,vuelto251,vuelto25,vuelto25]
#imagenes 50
vuelto50 = PhotoImage(file = "50/vuelto50.png")
vuelto501 = PhotoImage(file = "50/vuelto501.png")
vuelto502 = PhotoImage(file = "50/vuelto502.png")
vuelto503 = PhotoImage(file = "50/vuelto503.png")
vuelto504 = PhotoImage(file = "50/vuelto504.png")
vuelto505 = PhotoImage(file = "50/vuelto505.png")
vuelt50 = Label(principal,image = vuelto50,bg ="#555869")
animacion50 = [vuelto505,vuelto504,vuelto503,vuelto502,vuelto501,vuelto50,vuelto50]
#animacion del 100
vuelto100 = PhotoImage(file = "100/vuelto100.png")
vuelto1001 = PhotoImage(file = "100/vuelto1001.png")
vuelto1002 = PhotoImage(file = "100/vuelto1002.png")
vuelto1003 = PhotoImage(file = "100/vuelto1003.png")
vuelto1004 = PhotoImage(file = "100/vuelto1004.png")
vuelto1005 = PhotoImage(file = "100/vuelto1005.png")
vuelt100 = Label(principal,image = vuelto100,bg ="#555869")
animacion100= [vuelto1005,vuelto1004,vuelto1003,vuelto1002,vuelto1001,vuelto100,vuelto100]
#E:-
#S: variable menos 1 
#R:-
def recoger_m(boton):
        global cuenta
        boton.place_forget()
        cuenta -= 1
        if cuenta ==0:
            global bandera_regresar
            tituloe_vuelto.place_forget()
            tituloi_vuelto.place_forget()
            bandera_regresar = True
            titulo_graciase.place(x= 150,y=190)
            titulo_graciasi.place(x= 150,y=350)


            
#E:lista con imagnes,cordenadas en y en las que va a empezar,cordenadas en x,coordenadas en y hasta la que va a llegar, objero que se va a omer
#S:animacion del vuelto
#R:-
def animacionV(lista,suma,x,y,objeto):
    if suma > y:
        objeto.place_forget()
        global cuenta
        cuenta += 1
        moneda= Button(principal,image = lista[0],bg ="#555869",command =lambda: recoger_m(moneda))
        moneda.place(x= x,y=y)
        return lista[0]
    elif lista[1:] == []:
        suma += 10
        objeto.place(x=x,y=suma)
        sleep(0.1)
        return animacionV(lista,suma,x,y,objeto)
    
    else:
        objeto.configure(image =lista[0])
        sleep(0.1)
        return animacionV(lista[1:],suma,x,y,objeto)
 
#E:-
#S:llama a moneda para dar el vuelto
#R:-
def vuelto():
    vuel =abs(monedas_faltantes)
    tiqueteale.set_vuelto(vuel)
    tiqueteale.set_pago(monedas_ingresadas)
    return vuelto_aux(vuel)
def vuelto_aux(vuelto):
    if vuelto == 0:
        global bandera_regresar
        global cuenta
        bandera_regresar = True
        if cuenta == 0:
            tituloe_vuelto.place_forget()
            tituloi_vuelto.place_forget()
            titulo_graciase.place(x= 150,y=190)
            titulo_graciasi.place(x= 150,y=350)
        
        return 0
    elif vuelto >= 100:
        vuelt100.place(x=140,y =557)
        animacionV(animacion100,557,140,557,vuelt100)
        return vuelto_aux(vuelto-100)
    elif vuelto >= 50:
        vuelt50.place(x=200,y =557)
        animacionV(animacion50,557,200,607,vuelt50)
        return vuelto_aux(vuelto-50)
    elif vuelto >= 25:
        vuelt25.place(x=140,y =557)
        animacionV(animacion25,557,140,607,vuelt25)
        return vuelto_aux(vuelto-25)
    elif vuelto >= 10:
        vuelt10.place(x=200,y =557)
        animacionV(animacion10,557,200,557,vuelt10)
        return vuelto_aux(vuelto-10)
    else:
        vuelt5.place(x=140,y =557)
        animacionV(animacion5,557,140,557,vuelt5)
        return vuelto_aux(vuelto-5)
def hilo2():
    t2 = Thread(target = vuelto, args=())
    t2.start()
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
    resultado = Label(canvas,text = tiqueteale.get_mensaje(),font= ('Times New Roman',13),bg= 'white',fg= 'black')
    resultado.place(x=10,y=50)
    canvas.place(x=100, y=200)
    boleto_guardar.place(x=400,y=400)
    hilo2()


#boton del tomar el boleto
boleto = Button(principal, image=boleto21,command = tomar)
#animacion de la impresion del boleto
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
    global tiqueteale
    tiqueteale.set_fecha(strftime("%d/%m/%y"))
    tiqueteale.set_hora(strftime("%H:%M:%S")[:5])
    tiqueteale.set_numero_transaccion(1)
    tablaventas=tiqueteale.get_datos()
    archivov = open('ventas.txt','w')
    archivov.write('----------------------------------------------------------------------------------\n')
    archivov.write('Numero Transaccion    Fecha     Hora   Tipo   Codigo   Monto   Pago  Vuelto\n')
    archivov.write('----------------------------------------------------------------------------------\n')
    archivov.close()
    archivov = open('ventas.txt','a')
    archivov.write('%s'%tablaventas+'\n')
    archivov.write('----------------------------------------------------------------------------------\n')
    archivov.close()
    t1 = Thread(target = imprimir1, args=())
    t1.start()


#E:coordena en x en la que empieza,corrdenada en x hasta la que llega,objeto que se va a mover
#S:animacion de que entra una moneda
def animacionE(suma,x,objeto):
    if suma < x:
        return objeto.place_forget()
    else:
        suma -= 10
        objeto.place(x=suma,y=270)
        sleep(0.1)
        return animacionE(suma,x,objeto)


#E:numero de moneda que va ingresar
#S:contador de monedas ingresadas suma la moneda dada,resta la monedada a monedas faltantes
#R:-
def entra_moneda(num):
    if num == 5:
        m_5 = PhotoImage(file = "5/vuelto5.png")
        M_5 = Label(principal,image = m_5)
        M_5.place(x=650,y=270)
        animacionE(650,450,M_5)
    if num == 10:
        m_10 = PhotoImage(file = "10/vuelto10.png")
        M_10 = Label(principal,image = m_10)
        M_10.place(x=650,y=270)
        animacionE(650,450,M_10)
    if num == 25:
        m_25 = PhotoImage(file = "25/vuelto25.png")
        M_25 = Label(principal,image = m_25)
        M_25.place(x=650,y=270)
        animacionE(650,450,M_25)
    if num == 50:
        m_50 = PhotoImage(file = "50/vuelto50.png")
        M_50 = Label(principal,image = m_50)
        M_50.place(x=650,y=270)
        animacionE(650,450,M_50)
    if num == 100:
        m_100 = PhotoImage(file = "100/vuelto100.png")
        M_100 = Label(principal,image = m_100)
        M_100.place(x=650,y=270)
        animacionE(650,450,M_100)
        
    global monedas_ingresadas
    monedas_ingresadas += num
    titulo_contador.configure(text= '₡' + str(monedas_ingresadas))
    global monedas_faltantes
    monedas_faltantes -= num
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

        
def hilo3(num):
    t3 = Thread(target = entra_moneda, args=(num,))
    t3.start()

#muetra la ventana con las monedas para ingresar
def colones():
    global m_colones
    m_colones = Toplevel()
    m_colones.title('billetera')
    m_colones.configure(bg= 'white')
    #imagen de la moneda 5
    m_5 = PhotoImage(file = "5/m5.png")
    #boton de la moneda de 5
    Boton_5 = Button(m_colones,image = m_5,command =lambda: hilo3(5))
    Boton_5.place(x= 0,y=0)
    #imagen de la moneda 10
    m_10 = PhotoImage(file = "10/m10.png")
    #boton de la moneda de 10
    Boton_10 = Button(m_colones,image = m_10,command =lambda: hilo3(10))
    Boton_10.place(x= 0,y=120)
    #imagen de la moneda 25
    m_25 = PhotoImage(file = "25/25.png")
    #boton de la moneda de 25
    Boton_25 = Button(m_colones,image = m_25,command =lambda: hilo3(25))
    Boton_25.place(x= 0,y=240)
    #imagen de la moneda 50
    m_50 = PhotoImage(file = "50/50.png")
    #boton de la moneda de 50
    Boton_50 = Button(m_colones,image = m_50,command =lambda: hilo3(50))
    Boton_50.place(x= 0,y=380)
    #imagen de la moneda 100
    m_100 = PhotoImage(file = "100/100.png")
    #boton de la moneda de 100
    Boton_100= Button(m_colones,image = m_100,command =lambda: hilo3(100))
    Boton_100.place(x= 0,y=500)
    
    m_colones.geometry('50x650+290+0')
    m_colones.mainloop()

#variable para no usar lo botones
bandera =  True
#E:-
#S:presenta la pantalla de cobro
#R:-
def cobro(tipo):
    global bandera
    global bandera_admi
    bandera_admi = False
    if bandera == True:
        bandera = False
        #quita las coasas del primer menu
        primera = [titulo_bienvenidoe.place_forget(),titulo_bienvenidoi.place_forget()]
        global monedas_faltantes
        global nuevo
        global tiqueteale
        global venta11,venta12,venta13,venta14,venta15,venta16,venta17,venta18,venta19,venta110,venta111,venta112,venta113,venta114,venta115,venta116,venta21,venta22,venta23,venta24,venta25,venta26,venta27,venta28,venta29,venta210,venta211,venta212,venta213,venta214,venta215,venta216,venta217,venta31,venta32,venta33,venta34,venta35,venta36,venta37,venta38,venta39,venta310,venta311,venta312,venta313,venta314,venta315,venta316,venta317
        if tipo == 1:
            tiqueteale = random.choice(consejos)
            monedas_faltantes = tiqueteale.get_precio()
            tiqueteale.set_monto(monedas_faltantes)
            if tiqueteale.get_codigo() == 1:
                venta11+=1
            if tiqueteale.get_codigo() == 2:
                venta12+=1
            if tiqueteale.get_codigo() == 3:
                venta13+=1
            if tiqueteale.get_codigo() == 4:
                venta14+=1
            if tiqueteale.get_codigo() == 5:
                venta15+=1
            if tiqueteale.get_codigo() == 6:
                venta16+=1
            if tiqueteale.get_codigo() == 7:
                venta17+=1
            if tiqueteale.get_codigo() == 8:
                venta18+=1
            if tiqueteale.get_codigo() == 9:
                venta19+=1
            if tiqueteale.get_codigo() == 10:
                venta110+=1
            if tiqueteale.get_codigo() == 11:
                venta111+=1
            if tiqueteale.get_codigo() == 12:
                venta112+=1
            if tiqueteale.get_codigo() == 13:
                venta113+=1
            if tiqueteale.get_codigo() == 14:
                venta114+=1
            if tiqueteale.get_codigo() == 15:
                venta115+=1
            if tiqueteale.get_codigo() == 16:
                venta116+=1
        if tipo == 2:
            tiqueteale = random.choice(dichos)
            monedas_faltantes =tiqueteale.get_precio()
            if tiqueteale.get_codigo() == 1:
                venta21+=1
            if tiqueteale.get_codigo() == 2:
                venta22+=1
            if tiqueteale.get_codigo() == 3:
                venta23+=1
            if tiqueteale.get_codigo() == 4:
                venta24+=1
            if tiqueteale.get_codigo() == 5:
                venta25+=1
            if tiqueteale.get_codigo() == 6:
                venta26+=1
            if tiqueteale.get_codigo() == 7:
                venta27+=1
            if tiqueteale.get_codigo() == 8:
                venta28+=1
            if tiqueteale.get_codigo() == 9:
                venta29+=1
            if tiqueteale.get_codigo() == 10:
                venta210+=1
            if tiqueteale.get_codigo() == 11:
                venta211+=1
            if tiqueteale.get_codigo() == 12:
                venta212+=1
            if tiqueteale.get_codigo() == 13:
                venta213+=1
            if tiqueteale.get_codigo() == 14:
                venta214+=1
            if tiqueteale.get_codigo() == 15:
                venta215+=1
            if tiqueteale.get_codigo() == 16:
                venta216+=1
            if tiqueteale.get_codigo() == 17:
                venta217+=1
        if tipo == 3:
            tiqueteale = random.choice(chistes)
            monedas_faltantes = tiqueteale.get_precio()
            if tiqueteale.get_codigo() == 1:
                venta31+=1
            if tiqueteale.get_codigo() == 2:
                venta32+=1
            if tiqueteale.get_codigo() == 3:
                venta33+=1
            if tiqueteale.get_codigo() == 4:
                venta34+=1
            if tiqueteale.get_codigo() == 5:
                venta35+=1
            if tiqueteale.get_codigo() == 6:
                venta36+=1
            if tiqueteale.get_codigo() == 7:
                venta37+=1
            if tiqueteale.get_codigo() == 8:
                venta38+=1
            if tiqueteale.get_codigo() == 9:
                venta39+=1
            if tiqueteale.get_codigo() == 10:
                venta310+=1
            if tiqueteale.get_codigo() == 11:
                venta311+=1
            if tiqueteale.get_codigo() == 12:
                venta312+=1
            if tiqueteale.get_codigo() == 13:
                venta313+=1
            if tiqueteale.get_codigo() == 14:
                venta314+=1
            if tiqueteale.get_codigo() == 15:
                venta315+=1
            if tiqueteale.get_codigo() == 16:
                venta316+=1
            if tiqueteale.get_codigo() == 17:
                venta317+=1
        titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
        segundap = [titulo_contador,titulo_contadorf,tituloe_inserte.place(x=150,y=200),tituloi_inserte.place(x=150,y=220),tituloe_dinerof.place(x=280,y=410),
                    tituloi_dinerof.place(x=280,y=430),tituloe_dinero.place(x=150,y=410),tituloi_dinero.place(x=150,y=430),titulo_contador.place(x=150,y=450),
                    titulo_contadorf.place(x=280,y=450),fle.place(x=270,y =280)]
        archivo = open('mensajes.txt','w')
        archivo.write('----------------------------------------------------------------------------\n')
        archivo.write('Tipo    Código  Mensaje                          Precio    Ventas\n')
        archivo.write('----------------------------------------------------------------------------\n')
        archivo.write('1       1       Lo que los demas piensen de      20        %s'%venta11+'\n')
        archivo.write('1       2       No pierdas tu preciado           50        %s'%venta12+'\n')
        archivo.write('1       3       Sueña mas cuando                 50        %s'%venta13+'\n')
        archivo.write('1       4       No tienes que gana               20        %s'%venta14+'\n')
        archivo.write('1       5       No compares tu vida              75        %s'%venta15+'\n')
        archivo.write('1       6       La vida es demasiado corta       100       %s'%venta16+'\n')
        archivo.write('1       7       Nadie mas está al                25        %s'%venta17+'\n')
        archivo.write('1       8       Ríe y sonríe más a               20        %s'%venta18+'\n')
        archivo.write('1       9       Duerme 8 horas al dia            100       %s'%venta19+'\n')
        archivo.write('1       10      Toma agua                        200       %s'%venta110+'\n')
        archivo.write('1       11      Olvida los problemas             150       %s'%venta111+'\n')
        archivo.write('1       12      Cualquiera que sea               75        %s'%venta112+'\n')
        archivo.write('1       13      No importa cómo                  125       %s'%venta113+'\n')
        archivo.write('1       14      Sé agradecido                    120       %s'%venta114+'\n')
        archivo.write('1       15      No hagas siempre                 140       %s'%venta115+'\n')
        archivo.write('1       16      Vive el hoy                      20        %s'%venta116+'\n')
        archivo.write('2       1       No hay mal que por bien no       20        %s'%venta21+'\n')
        archivo.write('2       2       Quien duerme mucho, poco         40        %s'%venta22+'\n')
        archivo.write('2       3       De tal palo tal astilla          60        %s'%venta23+'\n')
        archivo.write('2       4       No hay peor ciego que el         75        %s'%venta24+'\n')
        archivo.write('2       5       El que no corre, vuela           45        %s'%venta25+'\n')
        archivo.write('2       6       Nadie sabe lo que tiene          100       %s'%venta26+'\n')
        archivo.write('2       7       Al mal tiempo buena cara         20        %s'%venta27+'\n')
        archivo.write('2       8       A buen entendedor pocas          80        %s'%venta28+'\n')
        archivo.write('2       9       A caballo regalado no se         55        %s'%venta29+'\n')
        archivo.write('2       10      Barriga llena, corazón           45        %s'%venta210+'\n')
        archivo.write('2       11      Más vale estar solo que mal      85        %s'%venta211+'\n')
        archivo.write('2       12      El que busca encuentra           105       %s'%venta212+'\n')
        archivo.write('2       13      Dime con quién andas             35        %s'%venta213+'\n')
        archivo.write('2       14      Haz bien y no mires a quien      55        %s'%venta214+'\n')
        archivo.write('2       15      La esperanza es lo último        60        %s'%venta215+'\n')
        archivo.write('2       16      Lo prometido es deuda            40        %s'%venta216+'\n')
        archivo.write('2       17      La pereza es la madre de         20        %s'%venta217+'\n')
        archivo.write('3       1       -¡Estás obsesionado con la       200       %s'%venta31+'\n')
        archivo.write('3       2       -¿Por qué estás hablando         140       %s'%venta32+'\n')
        archivo.write('3       3       — Buenos días, me gustaría       300       %s'%venta33+'\n')
        archivo.write('3       4       — ¡Camarero! Este filete         140       %s'%venta34+'\n')
        archivo.write('3       5       — Abuelo, ¿por qué estás         200       %s'%venta35+'\n')
        archivo.write('3       6       — ¿Para que va una caja          300       %s'%venta36+'\n')
        archivo.write('3       7       — ¿Por qué se suicidó el         250       %s'%venta37+'\n')
        archivo.write('3       8       — ¿Qué le dice un huevo          300       %s'%venta38+'\n')
        archivo.write('3       9       — ¿Qué le dice un espagueti      130       %s'%venta39+'\n')
        archivo.write('3       10      — ¿Qué le dice un grano de       170       %s'%venta310+'\n')
        archivo.write('3       11      —¿Qué le dice un árbol a otro    180       %s'%venta311+'\n')
        archivo.write('3       12      — ¿Cómo se llama el primo        150       %s'%venta312+'\n')
        archivo.write('3       13      — Soy celíaca.                   240       %s'%venta313+'\n')
        archivo.write('3       14      — ¿Sabes por qué no se           280       %s'%venta314+'\n')
        archivo.write('3       15      — ¿Por qué el mar no se seca?    210       %s'%venta315+'\n')
        archivo.write('3       16      — ¿De qué se quejan siempre      65        %s'%venta316+'\n')
        archivo.write('3       17      — Mamá, en el cole me llaman     20        %s'%venta317+'\n')
        archivo.write('----------------------------------------------------------------------------\n')
        archivo.close()
         
        colones()

#E:-
#S:cierra el programa
#R:-
def cerrar():
    principal.destroy()
#boton para verificar la contrase
Aceptar= Button(principal,text= ' Aceptar/Accept',command=  lambda: verifica(contraseña.get()))

#funcion reset
def reset():
    archivo = open('mensajes.txt','w')
    archivo.write('----------------------------------------------------------------------------\n')
    archivo.write('Tipo    Código  Mensaje                          Precio    Ventas\n')
    archivo.write('----------------------------------------------------------------------------\n')
    archivo.write('1       1       Lo que los demas piensen de      20        %s'%0+'\n')
    archivo.write('1       2       No pierdas tu preciado           50        %s'%0+'\n')
    archivo.write('1       3       Sueña mas cuando                 50        %s'%0+'\n')
    archivo.write('1       4       No tienes que gana               20        %s'%0+'\n')
    archivo.write('1       5       No compares tu vida              75        %s'%0+'\n')
    archivo.write('1       6       La vida es demasiado corta       100       %s'%0+'\n')
    archivo.write('1       7       Nadie mas está al                25        %s'%0+'\n')
    archivo.write('1       8       Ríe y sonríe más a               20        %s'%0+'\n')
    archivo.write('1       9       Duerme 8 horas al dia            100       %s'%0+'\n')
    archivo.write('1       10      Toma agua                        200       %s'%0+'\n')
    archivo.write('1       11      Olvida los problemas             150       %s'%0+'\n')
    archivo.write('1       12      Cualquiera que sea               75        %s'%0+'\n')
    archivo.write('1       13      No importa cómo                  125       %s'%0+'\n')
    archivo.write('1       14      Sé agradecido                    120       %s'%0+'\n')
    archivo.write('1       15      No hagas siempre                 140       %s'%0+'\n')
    archivo.write('1       16      Vive el hoy                      20        %s'%0+'\n')
    archivo.write('2       1       No hay mal que por bien no       20        %s'%0+'\n')
    archivo.write('2       2       Quien duerme mucho, poco         40        %s'%0+'\n')
    archivo.write('2       3       De tal palo tal astilla          60        %s'%0+'\n')
    archivo.write('2       4       No hay peor ciego que el         75        %s'%0+'\n')
    archivo.write('2       5       El que no corre, vuela           45        %s'%0+'\n')
    archivo.write('2       6       Nadie sabe lo que tiene          100       %s'%0+'\n')
    archivo.write('2       7       Al mal tiempo buena cara         20        %s'%0+'\n')
    archivo.write('2       8       A buen entendedor pocas          80        %s'%0+'\n')
    archivo.write('2       9       A caballo regalado no se         55        %s'%0+'\n')
    archivo.write('2       10      Barriga llena, corazón           45        %s'%0+'\n')
    archivo.write('2       11      Más vale estar solo que mal      85        %s'%0+'\n')
    archivo.write('2       12      El que busca encuentra           105       %s'%0+'\n')
    archivo.write('2       13      Dime con quién andas             35        %s'%0+'\n')
    archivo.write('2       14      Haz bien y no mires a quien      55        %s'%0+'\n')
    archivo.write('2       15      La esperanza es lo último        60        %s'%0+'\n')
    archivo.write('2       16      Lo prometido es deuda            40        %s'%0+'\n')
    archivo.write('2       17      La pereza es la madre de         20        %s'%0+'\n')
    archivo.write('3       1       -¡Estás obsesionado con la       200       %s'%0+'\n')
    archivo.write('3       2       -¿Por qué estás hablando         140       %s'%0+'\n')
    archivo.write('3       3       — Buenos días, me gustaría       300       %s'%0+'\n')
    archivo.write('3       4       — ¡Camarero! Este filete         140       %s'%0+'\n')
    archivo.write('3       5       — Abuelo, ¿por qué estás         200       %s'%0+'\n')
    archivo.write('3       6       — ¿Para que va una caja          300       %s'%0+'\n')
    archivo.write('3       7       — ¿Por qué se suicidó el         250       %s'%0+'\n')
    archivo.write('3       8       — ¿Qué le dice un huevo          300       %s'%0+'\n')
    archivo.write('3       9       — ¿Qué le dice un espagueti      130       %s'%0+'\n')
    archivo.write('3       10      — ¿Qué le dice un grano de       170       %s'%0+'\n')
    archivo.write('3       11      —¿Qué le dice un árbol a otro    180       %s'%0+'\n')
    archivo.write('3       12      — ¿Cómo se llama el primo        150       %s'%0+'\n')
    archivo.write('3       13      — Soy celíaca.                   240       %s'%0+'\n')
    archivo.write('3       14      — ¿Sabes por qué no se           280       %s'%0+'\n')
    archivo.write('3       15      — ¿Por qué el mar no se seca?    210       %s'%0+'\n')
    archivo.write('3       16      — ¿De qué se quejan siempre      65        %s'%0+'\n')
    archivo.write('3       17      — Mamá, en el cole me llaman     20        %s'%0+'\n')
    archivo.write('----------------------------------------------------------------------------\n')
    archivo.close()
 

#boton de reset
reset= Button(principal,text= ' Reset', command = reset)
##boton apagar
apagar= Button(principal,text= ' Apagar/Turn off',command = cerrar)
##boton resumen de ventas
Resumen= Button(principal,text= ' Resumen de ventas/Sales summary')
#entry para ingresar la contrase
contraseña = Entry(principal, show="*", width=30)
    


#E:dato que se ingreso en el entry
#S:menu de admi
#R:-
def verifica(contraseñ):
    if contraseñ == 'jeff eres lo mejor':
        contraseña.place_forget()
        Aceptar.place_forget()
        titulo_contraseñae.place_forget()
        titulo_contraseñai.place_forget()
        reset.place(x=160,y=260)
        apagar.place(x=160,y=300)
        Resumen.place(x=160,y=340)
        titulo_admie.place(x=150,y=200)
        titulo_admii.place(x=150,y=220)
        
    else:
        messagebox.showerror('X', 'contraseña incorrecta \n Incorrect password')


#E:-
#S:abre el menu de admi
#R:-
def menu_admi():
    global bandera_admi
    global bandera_regresar
    bandera_regresar = True
    
    if bandera_admi == True:
        global bandera
        bandera = False
        bandera_admi = False
        primera = [titulo_bienvenidoe.place_forget(),titulo_bienvenidoi.place_forget()]
        titulo_contraseñae.place(x=150,y=200)
        titulo_contraseñai.place(x=160,y=220)
        contraseña.place(x=160,y=240)
        contraseña.delete(0, END)
        
        Aceptar.place(x= 160,y=260)
        

#titulos bienevenido (español e ingles)
titulo_bienvenidoe = Label(principal,text = 'Bienvenido ¿Que desea obtener?',font= ('Times New Roman',13),bg= 'black',fg= 'white')
titulo_bienvenidoe.place(x=150,y=200)
titulo_bienvenidoi = Label(principal,text = 'Welcome ¿What do you want to get?',font= ('Times New Roman',10),bg= 'black',fg= 'light blue')
titulo_bienvenidoi.place(x=160,y=220)


#E:-
#S:regresa al primer menu
#R:-
def regresa():
    global bandera_regresar
    global bandera_admi
    global bandera
    if bandera_regresar == True:
        bandera_regresar = False
        bandera_admi = True
        bandera = True
        titulo_bienvenidoi.place(x=160,y=220)
        titulo_bienvenidoe.place(x=150,y=200)
        titulo_contraseñae.place_forget()
        titulo_contraseñai.place_forget()
        contraseña.place_forget()
        Aceptar.place_forget()
        reset.place_forget()
        apagar.place_forget()
        Resumen.place_forget()
        titulo_admie.place_forget()
        titulo_admii.place_forget()
        titulo_graciase.place_forget()
        titulo_graciasi.place_forget()
    
    


#boton para consejo
consejo= Button(principal,text= '  Consejo \n (Advice)',command=  lambda: cobro(1))
consejo.place(x= 420,y=500)
#boton para dicho
dicho= Button(principal,text= '  Dicho \n (Saying)',command= lambda: cobro(2))
dicho.place(x= 300,y=500)
#boton para Chistes
Chistes= Button(principal,text= '  Chistes \n (Jokes)',command= lambda: cobro(3))
Chistes.place(x= 360,y=500)
#boton para admi
admi= Button(principal,text= 'Admi',command = menu_admi)
admi.place(x= 140,y=125)
#boton para regresar
principio= Button(principal,text= 'Regresar',command = regresa)
principio.place(x= 440,y=620)



#tamaño de la ventana
principal.geometry('600x700+400+0')
principal.mainloop()
