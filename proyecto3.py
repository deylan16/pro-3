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
arventa11 = open('contadores/venta11.txt','r')
conventa11=int(arventa11.read())
arventa11.close()
venta11 = conventa11
arventa12 = open('contadores/venta12.txt','r')
conventa12=int(arventa12.read())
arventa12.close()
venta12=conventa12
arventa13 = open('contadores/venta13.txt','r')
conventa13=int(arventa13.read())
arventa13.close()
venta13=conventa13
arventa14 = open('contadores/venta14.txt','r')
conventa14=int(arventa14.read())
arventa14.close()
venta14=conventa14
arventa15 = open('contadores/venta15.txt','r')
conventa15=int(arventa15.read())
arventa15.close()
venta15=conventa15
arventa16 = open('contadores/venta16.txt','r')
conventa16=int(arventa16.read())
arventa16.close()
venta16=conventa16
arventa17 = open('contadores/venta17.txt','r')
conventa17=int(arventa17.read())
arventa17.close()
venta17=conventa17
arventa18 = open('contadores/venta18.txt','r')
conventa18=int(arventa18.read())
arventa18.close()
venta18=conventa18
arventa19 = open('contadores/venta19.txt','r')
conventa19=int(arventa19.read())
arventa19.close()
venta19=conventa19
arventa110 = open('contadores/venta110.txt','r')
conventa110=int(arventa110.read())
arventa110.close()
venta110=conventa110
arventa111 = open('contadores/venta111.txt','r')
conventa111=int(arventa111.read())
arventa111.close()
venta111=conventa111
arventa112 = open('contadores/venta112.txt','r')
conventa112=int(arventa112.read())
arventa112.close()
venta112=conventa112
arventa113 = open('contadores/venta113.txt','r')
conventa113=int(arventa113.read())
arventa113.close()
venta113=conventa113
arventa114 = open('contadores/venta114.txt','r')
conventa114=int(arventa114.read())
arventa114.close()
venta114=conventa114
arventa115 = open('contadores/venta115.txt','r')
conventa115=int(arventa115.read())
arventa115.close()
venta115=conventa115
arventa116 = open('contadores/venta116.txt','r')
conventa116=int(arventa116.read())
arventa116.close()
venta116=conventa116
arventa21 = open('contadores/venta21.txt','r')
conventa21=int(arventa21.read())
arventa21.close()
venta21=conventa21
arventa22 = open('contadores/venta22.txt','r')
conventa22=int(arventa22.read())
arventa22.close()
venta22=conventa22
arventa23 = open('contadores/venta23.txt','r')
conventa23=int(arventa23.read())
arventa23.close()
venta23=conventa23
arventa24 = open('contadores/venta24.txt','r')
conventa24=int(arventa24.read())
arventa24.close()
venta24=conventa24
arventa25 = open('contadores/venta25.txt','r')
conventa25=int(arventa25.read())
arventa25.close()
venta25=conventa25
arventa26 = open('contadores/venta26.txt','r')
conventa26=int(arventa26.read())
arventa26.close()
venta26=conventa26
arventa27 = open('contadores/venta27.txt','r')
conventa27=int(arventa27.read())
arventa27.close()
venta27=conventa27
arventa28 = open('contadores/venta28.txt','r')
conventa28=int(arventa28.read())
arventa28.close()
venta28=conventa28
arventa29 = open('contadores/venta29.txt','r')
conventa29=int(arventa29.read())
arventa29.close()
venta29=conventa29
arventa210 = open('contadores/venta210.txt','r')
conventa210=int(arventa210.read())
arventa210.close()
venta210=conventa210
arventa211 = open('contadores/venta211.txt','r')
conventa211=int(arventa211.read())
arventa211.close()
venta211=conventa211
arventa212 = open('contadores/venta212.txt','r')
conventa212=int(arventa212.read())
arventa212.close()
venta212=conventa212
arventa213 = open('contadores/venta213.txt','r')
conventa213=int(arventa213.read())
arventa213.close()
venta213=conventa213
arventa214 = open('contadores/venta214.txt','r')
conventa214=int(arventa214.read())
arventa214.close()
venta214=conventa214
arventa215 = open('contadores/venta21.txt','r')
conventa215=int(arventa215.read())
arventa215.close()
venta215=conventa215
arventa216 = open('contadores/venta216.txt','r')
conventa216=int(arventa216.read())
arventa216.close()
venta216=conventa216
arventa217 = open('contadores/venta217.txt','r')
conventa217=int(arventa217.read())
arventa217.close()
venta217=conventa217
arventa31 = open('contadores/venta31.txt','r')
conventa31=int(arventa31.read())
arventa31.close()
venta31=conventa31
arventa32 = open('contadores/venta32.txt','r')
conventa32=int(arventa32.read())
arventa32.close()
venta32=conventa32
arventa33 = open('contadores/venta33.txt','r')
conventa33=int(arventa33.read())
arventa33.close()
venta33=conventa33
arventa34 = open('contadores/venta34.txt','r')
conventa34=int(arventa34.read())
arventa34.close()
venta34=conventa34
arventa35 = open('contadores/venta35.txt','r')
conventa35=int(arventa35.read())
arventa35.close()
venta35=conventa35
arventa36 = open('contadores/venta36.txt','r')
conventa36=int(arventa36.read())
arventa36.close()
venta36=conventa36
arventa37 = open('contadores/venta37.txt','r')
conventa37=int(arventa37.read())
arventa37.close()
venta37=conventa37
arventa38 = open('contadores/venta38.txt','r')
conventa38=int(arventa38.read())
arventa38.close()
venta38=conventa38
arventa39 = open('contadores/venta39.txt','r')
conventa39=int(arventa39.read())
arventa39.close()
venta39=conventa39
arventa310 = open('contadores/venta310.txt','r')
conventa310=int(arventa310.read())
arventa310.close()
venta310=conventa310
arventa311 = open('contadores/venta311.txt','r')
conventa311=int(arventa311.read())
arventa311.close()
venta311=conventa311
arventa312 = open('contadores/venta312.txt','r')
conventa312=int(arventa312.read())
arventa312.close()
venta312=conventa312
arventa313 = open('contadores/venta313.txt','r')
conventa313=int(arventa313.read())
arventa313.close()
venta313=conventa313
arventa314 = open('contadores/venta314.txt','r')
conventa314=int(arventa314.read())
arventa314.close()
venta314=conventa314
arventa315 = open('contadores/venta315.txt','r')
conventa315=int(arventa315.read())
arventa315.close()
venta315=conventa315
arventa316 = open('contadores/venta316.txt','r')
conventa316=int(arventa316.read())
arventa316.close()
venta316=conventa316
arventa317 = open('contadores/venta317.txt','r')
conventa317=int(arventa317.read())
arventa317.close()
venta317=conventa317
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
#obtine lo que esta excrito en el txt ventas

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
    archivol = open('ventas.txt','r')
    contenido1=archivol.read()
    contenido = None
    if contenido1[0] != '0':
        contenido = contenido1[:-82]
    if contenido1[0] == '0':
        contenido = contenido1
    num = int(contenido[0])+1
    numt = open('contadores/numero transaccion.txt','r')
    numtr=int(numt.read())
    numt.close()
    
    global tiqueteale
    tiqueteale.set_fecha(strftime("%d/%m/%y"))
    tiqueteale.set_hora(strftime("%H:%M:%S")[:5])
    
    tiqueteale.set_numero_transaccion(numtr)
    vuel =abs(monedas_faltantes)
    tiqueteale.set_vuelto(vuel)
    tiqueteale.set_pago(monedas_ingresadas)
    tablaventas=tiqueteale.get_datos()
    archivov = open('ventas.txt','w')
    archivov.write(str(num)) 
    archivov.write(contenido[1:] + '\n')
    archivov.close()
    archivov = open('ventas.txt','a')
    archivov.write('%s'%tablaventas+'\n')
    archivov.write('----------------------------------------------------------------------------------')
    archivov.close()
    num2 = int(contenido[0])+1
    numt2 = open('contadores/numero transaccion.txt','w')
    numt2.write(str(numtr+1))
    numt2.close()
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
                arventa11 = open('contadores/venta11.txt','w')
                arventa11.write(str(venta11))
                arventa11.close()
            if tiqueteale.get_codigo() == 2:
                venta12+=1
                arventa12 = open('contadores/venta12.txt','w')
                arventa12.write(str(venta12))
                arventa12.close()
            if tiqueteale.get_codigo() == 3:
                venta13+=1
                arventa13 = open('contadores/venta13.txt','w')
                arventa13.write(str(venta13))
                arventa13.close()
            if tiqueteale.get_codigo() == 4:
                venta14+=1
                arventa14 = open('contadores/venta14.txt','w')
                arventa14.write(str(venta14))
                arventa14.close()
            if tiqueteale.get_codigo() == 5:
                venta15+=1
                arventa15 = open('contadores/venta15.txt','w')
                arventa15.write(str(venta15))
                arventa15.close()
            if tiqueteale.get_codigo() == 6:
                venta16+=1
                arventa16 = open('contadores/venta16.txt','w')
                arventa16.write(str(venta16))
                arventa16.close()
            if tiqueteale.get_codigo() == 7:
                venta17+=1
                arventa17 = open('contadores/venta17.txt','w')
                arventa17.write(str(venta17))
                arventa17.close()
            if tiqueteale.get_codigo() == 8:
                venta18+=1
                arventa18 = open('contadores/venta18.txt','w')
                arventa18.write(str(venta18))
                arventa18.close()
            if tiqueteale.get_codigo() == 9:
                venta19+=1
                arventa19 = open('contadores/venta19.txt','w')
                arventa19.write(str(venta19))
                arventa19.close()
            if tiqueteale.get_codigo() == 10:
                venta110+=1
                arventa110 = open('contadores/venta110.txt','w')
                arventa110.write(str(venta110))
                arventa110.close()
            if tiqueteale.get_codigo() == 11:
                venta111+=1
                arventa111 = open('contadores/venta111.txt','w')
                arventa111.write(str(venta111))
                arventa111.close()
            if tiqueteale.get_codigo() == 12:
                venta112+=1
                arventa112 = open('contadores/venta112.txt','w')
                arventa112.write(str(venta112))
                arventa112.close()
            if tiqueteale.get_codigo() == 13:
                venta113+=1
                arventa113 = open('contadores/venta113.txt','w')
                arventa113.write(str(venta113))
                arventa113.close()
            if tiqueteale.get_codigo() == 14:
                venta114+=1
                arventa114 = open('contadores/venta114.txt','w')
                arventa114.write(str(venta114))
                arventa114.close()
            if tiqueteale.get_codigo() == 15:
                venta115+=1
                arventa115 = open('contadores/venta115.txt','w')
                arventa115.write(str(venta115))
                arventa115.close()
            if tiqueteale.get_codigo() == 16:
                venta116+=1
                arventa116 = open('contadores/venta116.txt','w')
                arventa116.write(str(venta116))
                arventa116.close()
        if tipo == 2:
            tiqueteale = random.choice(dichos)
            monedas_faltantes =tiqueteale.get_precio()
            if tiqueteale.get_codigo() == 1:
                venta21+=1
                arventa21 = open('contadores/venta21.txt','w')
                arventa21.write(str(venta21))
                arventa21.close()
            if tiqueteale.get_codigo() == 2:
                venta22+=1
                arventa22 = open('contadores/venta22.txt','w')
                arventa22.write(str(venta22))
                arventa22.close()
            if tiqueteale.get_codigo() == 3:
                venta23+=1
                arventa23 = open('contadores/venta23.txt','w')
                arventa23.write(str(venta23))
                arventa23.close()
            if tiqueteale.get_codigo() == 4:
                venta24+=1
                arventa24 = open('contadores/venta24.txt','w')
                arventa24.write(str(venta24))
                arventa24.close()
            if tiqueteale.get_codigo() == 5:
                venta25+=1
                arventa25 = open('contadores/venta25.txt','w')
                arventa25.write(str(venta25))
                arventa25.close()
            if tiqueteale.get_codigo() == 6:
                venta26+=1
                arventa26 = open('contadores/venta26.txt','w')
                arventa26.write(str(venta26))
                arventa26.close()
            if tiqueteale.get_codigo() == 7:
                venta27+=1
                arventa27 = open('contadores/venta27.txt','w')
                arventa27.write(str(venta27))
                arventa27.close()
            if tiqueteale.get_codigo() == 8:
                venta28+=1
                arventa28 = open('contadores/venta28.txt','w')
                arventa28.write(str(venta28))
                arventa28.close()
            if tiqueteale.get_codigo() == 9:
                venta29+=1
                arventa29 = open('contadores/venta29.txt','w')
                arventa29.write(str(venta29))
                arventa29.close()
            if tiqueteale.get_codigo() == 10:
                venta210+=1
                arventa210 = open('contadores/venta210.txt','w')
                arventa210.write(str(venta210))
                arventa210.close()
            if tiqueteale.get_codigo() == 11:
                venta211+=1
                arventa211 = open('contadores/venta211.txt','w')
                arventa211.write(str(venta211))
                arventa211.close()
            if tiqueteale.get_codigo() == 12:
                venta212+=1
                arventa212 = open('contadores/venta212.txt','w')
                arventa212.write(str(venta212))
                arventa212.close()
            if tiqueteale.get_codigo() == 13:
                venta213+=1
                arventa213 = open('contadores/venta213.txt','w')
                arventa213.write(str(venta213))
                arventa213.close()
            if tiqueteale.get_codigo() == 14:
                venta214+=1
                arventa214 = open('contadores/venta214.txt','w')
                arventa214.write(str(venta214))
                arventa214.close()
            if tiqueteale.get_codigo() == 15:
                venta215+=1
                arventa215 = open('contadores/venta215.txt','w')
                arventa215.write(str(venta215))
                arventa215.close()
            if tiqueteale.get_codigo() == 16:
                venta216+=1
                arventa216 = open('contadores/venta216.txt','w')
                arventa216.write(str(venta21))
                arventa216.close()
            if tiqueteale.get_codigo() == 17:
                venta217+=1
                arventa217 = open('contadores/venta217.txt','w')
                arventa217.write(str(venta217))
                arventa217.close()
        if tipo == 3:
            tiqueteale = random.choice(chistes)
            monedas_faltantes = tiqueteale.get_precio()
            if tiqueteale.get_codigo() == 1:
                venta31+=1
                arventa31 = open('contadores/venta31.txt','w')
                arventa31.write(str(venta31))
                arventa31.close()
            if tiqueteale.get_codigo() == 2:
                venta32+=1
                arventa32 = open('contadores/venta32.txt','w')
                arventa32.write(str(venta32))
                arventa32.close()
            if tiqueteale.get_codigo() == 3:
                venta33+=1
                arventa33 = open('contadores/venta33.txt','w')
                arventa33.write(str(venta33))
                arventa33.close()
            if tiqueteale.get_codigo() == 4:
                venta34+=1
                arventa34 = open('contadores/venta34.txt','w')
                arventa34.write(str(venta34))
                arventa34.close()
            if tiqueteale.get_codigo() == 5:
                venta35+=1
                arventa35 = open('contadores/venta35.txt','w')
                arventa35.write(str(venta35))
                arventa35.close()
            if tiqueteale.get_codigo() == 6:
                venta36+=1
                arventa36 = open('contadores/venta36.txt','w')
                arventa36.write(str(venta36))
                arventa36.close()
            if tiqueteale.get_codigo() == 7:
                arventa37 = open('contadores/venta37.txt','w')
                arventa37.write(str(venta37))
                arventa37.close()
            if tiqueteale.get_codigo() == 8:
                venta38+=1
                arventa38 = open('contadores/venta38.txt','w')
                arventa38.write(str(venta38))
                arventa38.close()
            if tiqueteale.get_codigo() == 9:
                venta39+=1
                arventa39 = open('contadores/venta39.txt','w')
                arventa39.write(str(venta39))
                arventa39.close()
            if tiqueteale.get_codigo() == 10:
                venta310+=1
                arventa310 = open('contadores/venta310.txt','w')
                arventa310.write(str(venta310))
                arventa310.close()
            if tiqueteale.get_codigo() == 11:
                venta311+=1
                arventa311 = open('contadores/venta311.txt','w')
                arventa311.write(str(venta311))
                arventa311.close()
            if tiqueteale.get_codigo() == 12:
                venta312+=1
                arventa312 = open('contadores/venta312.txt','w')
                arventa312.write(str(venta312))
                arventa312.close()
            if tiqueteale.get_codigo() == 13:
                venta313+=1
                arventa313 = open('contadores/venta313.txt','w')
                arventa313.write(str(venta313))
                arventa313.close()
            if tiqueteale.get_codigo() == 14:
                venta314+=1
                arventa314 = open('contadores/venta314.txt','w')
                arventa314.write(str(venta314))
                arventa314.close()
            if tiqueteale.get_codigo() == 15:
                venta315+=1
                arventa315 = open('contadores/venta315.txt','w')
                arventa315.write(str(venta315))
                arventa315.close()
            if tiqueteale.get_codigo() == 16:
                venta316+=1
                arventa316 = open('contadores/venta316.txt','w')
                arventa316.write(str(venta316))
                arventa316.close()
            if tiqueteale.get_codigo() == 17:
                venta317+=1
                arventa317 = open('contadores/venta317.txt','w')
                arventa317.write(str(venta317))
                arventa317.close()
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
        archivor = open('resumen ventas.txt','w')
        archivor.write('----------------------------------------------------------------------------\n')
        archivor.write('Tipo    Código  Mensaje                       Mensajes vendidos   Monto Ventas\n')
        archivor.write('----------------------------------------------------------------------------\n')
        archivor.write('1       1       Lo que los demas piensen de           %s'%venta11+'                %s'%(venta11*consejo1.get_precio())+'\n')
        archivor.write('1       2       No pierdas tu preciado                %s'%venta12+'                %s'%(venta12*consejo2.get_precio())+'\n')
        archivor.write('1       3       Sueña mas cuando                      %s'%venta13+'                %s'%(venta13*consejo3.get_precio())+'\n')
        archivor.write('1       4       No tienes que gana                    %s'%venta14+'                %s'%(venta14*consejo4.get_precio())+'\n')
        archivor.write('1       5       No compares tu vida                   %s'%venta15+'                %s'%(venta15*consejo5.get_precio())+'\n')
        archivor.write('1       6       La vida es demasiado corta            %s'%venta16+'                %s'%(venta16*consejo6.get_precio())+'\n')
        archivor.write('1       7       Nadie mas está al                     %s'%venta17+'                %s'%(venta17*consejo7.get_precio())+'\n')
        archivor.write('1       8       Ríe y sonríe más a                    %s'%venta18+'                %s'%(venta18*consejo8.get_precio())+'\n')
        archivor.write('1       9       Duerme 8 horas al dia                 %s'%venta19+'                %s'%(venta19*consejo9.get_precio())+'\n')
        archivor.write('1       10      Toma agua                             %s'%venta110+'                %s'%(venta110*consejo10.get_precio())+'\n')
        archivor.write('1       11      Olvida los problemas                  %s'%venta111+'                %s'%(venta111*consejo11.get_precio())+'\n')
        archivor.write('1       12      Cualquiera que sea                    %s'%venta112+'                %s'%(venta112*consejo12.get_precio())+'\n')
        archivor.write('1       13      No importa cómo                       %s'%venta113+'                %s'%(venta113*consejo13.get_precio())+'\n')
        archivor.write('1       14      Sé agradecido                         %s'%venta114+'                %s'%(venta114*consejo14.get_precio())+'\n')
        archivor.write('1       15      No hagas siempre                      %s'%venta115+'                %s'%(venta115*consejo15.get_precio())+'\n')
        archivor.write('1       16      Vive el hoy                           %s'%venta116+'                %s'%(venta116*consejo16.get_precio())+'\n')
        archivor.write('2       1       No hay mal que por bien no            %s'%venta21+'                %s'%(venta21*dicho1.get_precio())+'\n')
        archivor.write('2       2       Quien duerme mucho, poco              %s'%venta22+'                %s'%(venta22*dicho2.get_precio())+'\n')
        archivor.write('2       3       De tal palo tal astilla               %s'%venta23+'                %s'%(venta23*dicho3.get_precio())+'\n')
        archivor.write('2       4       No hay peor ciego que el              %s'%venta24+'                %s'%(venta24*dicho4.get_precio())+'\n')
        archivor.write('2       5       El que no corre, vuela                %s'%venta25+'                %s'%(venta25*dicho5.get_precio())+'\n')
        archivor.write('2       6       Nadie sabe lo que tiene               %s'%venta26+'                %s'%(venta26*dicho6.get_precio())+'\n')
        archivor.write('2       7       Al mal tiempo buena cara              %s'%venta27+'                %s'%(venta27*dicho7.get_precio())+'\n')
        archivor.write('2       8       A buen entendedor pocas               %s'%venta28+'                %s'%(venta28*dicho8.get_precio())+'\n')
        archivor.write('2       9       A caballo regalado no se              %s'%venta29+'                %s'%(venta29*dicho9.get_precio())+'\n')
        archivor.write('2       10      Barriga llena, corazón                %s'%venta210+'                %s'%(venta210*dicho10.get_precio())+'\n')
        archivor.write('2       11      Más vale estar solo que mal           %s'%venta211+'                %s'%(venta211*dicho11.get_precio())+'\n')
        archivor.write('2       12      El que busca encuentra                %s'%venta212+'                %s'%(venta212*dicho12.get_precio())+'\n')
        archivor.write('2       13      Dime con quién andas                  %s'%venta213+'                %s'%(venta213*dicho13.get_precio())+'\n')
        archivor.write('2       14      Haz bien y no mires a quien           %s'%venta214+'                %s'%(venta214*dicho14.get_precio())+'\n')
        archivor.write('2       15      La esperanza es lo último             %s'%venta215+'                %s'%(venta215*dicho15.get_precio())+'\n')
        archivor.write('2       16      Lo prometido es deuda                 %s'%venta216+'                %s'%(venta216*dicho16.get_precio())+'\n')
        archivor.write('2       17      La pereza es la madre de              %s'%venta217+'                %s'%(venta217*dicho17.get_precio())+'\n')
        archivor.write('3       1       -¡Estás obsesionado con la            %s'%venta31+'                %s'%(venta31*chiste1.get_precio())+'\n')
        archivor.write('3       2       -¿Por qué estás hablando              %s'%venta32+'                %s'%(venta32*chiste2.get_precio())+'\n')
        archivor.write('3       3       — Buenos días, me gustaría            %s'%venta33+'                %s'%(venta33*chiste3.get_precio())+'\n')
        archivor.write('3       4       — ¡Camarero! Este filete              %s'%venta34+'                %s'%(venta34*chiste4.get_precio())+'\n')
        archivor.write('3       5       — Abuelo, ¿por qué estás              %s'%venta35+'                %s'%(venta35*chiste5.get_precio())+'\n')
        archivor.write('3       6       — ¿Para que va una caja               %s'%venta36+'                %s'%(venta36*chiste6.get_precio())+'\n')
        archivor.write('3       7       — ¿Por qué se suicidó el              %s'%venta37+'                %s'%(venta37*chiste7.get_precio())+'\n')
        archivor.write('3       8       — ¿Qué le dice un huevo               %s'%venta38+'                %s'%(venta38*chiste8.get_precio())+'\n')
        archivor.write('3       9       — ¿Qué le dice un espagueti           %s'%venta39+'                %s'%(venta39*chiste9.get_precio())+'\n')
        archivor.write('3       10      — ¿Qué le dice un grano de            %s'%venta310+'                %s'%(venta310*chiste10.get_precio())+'\n')
        archivor.write('3       11      —¿Qué le dice un árbol a otro         %s'%venta311+'                %s'%(venta311*chiste11.get_precio())+'\n')
        archivor.write('3       12      — ¿Cómo se llama el primo             %s'%venta312+'                %s'%(venta312*chiste12.get_precio())+'\n')
        archivor.write('3       13      — Soy celíaca.                        %s'%venta313+'                %s'%(venta313*chiste13.get_precio())+'\n')
        archivor.write('3       14      — ¿Sabes por qué no se                %s'%venta314+'                %s'%(venta314*chiste14.get_precio())+'\n')
        archivor.write('3       15      — ¿Por qué el mar no se seca?         %s'%venta315+'                %s'%(venta315*chiste15.get_precio())+'\n')
        archivor.write('3       16      — ¿De qué se quejan siempre           %s'%venta316+'                %s'%(venta316*chiste16.get_precio())+'\n')
        archivor.write('3       17      — Mamá, en el cole me llaman          %s'%venta317+'                %s'%(venta317*chiste17.get_precio())+'\n')
        archivor.write('----------------------------------------------------------------------------\n')
        archivor.close()
         
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
    archivov = open('ventas.txt','w')
    archivov.write('0--------------------------------------------------------------------------------- \n Numero Transaccion    Fecha     Hora   Tipo   Codigo   Monto   Pago  Vuelto \n----------------------------------------------------------------------------------')
    archivov.close()
    archivov = open('resumen ventas.txt','w')
    archivov.write('----------------------------------------------------------------------------\n'+
                   'Tipo    Código  Mensaje                       Mensajes vendidos   Monto Ventas\n'+
                   '----------------------------------------------------------------------------\n'+
                   '1       1       Lo que los demas piensen de           0                0\n'+
                   '1       2       No pierdas tu preciado                0                0\n'+
                   '1       3       Sueña mas cuando                      0                0\n'+
                   '1       4       No tienes que gana                    0                0\n'+
                   '1       5       No compares tu vida                   0                0\n'+
                   '1       6       La vida es demasiado corta            0                0\n'+
                   '1       7       Nadie mas está al                     0                0\n'+
                   '1       8       Ríe y sonríe más a                    0                0\n'+
                   '1       9       Duerme 8 horas al dia                 0                0\n'+
                   '1       10      Toma agua                             0                0\n'+
                   '1       11      Olvida los problemas                  0                0\n'+
                   '1       12      Cualquiera que sea                    0                0\n'+
                   '1       13      No importa cómo                       0                0\n'+
                   '1       14      Sé agradecido                         0                0\n'+
                   '1       15      No hagas siempre                      0                0\n'+
                   '1       16      Vive el hoy                           0                0\n'+
                   '2       1       No hay mal que por bien no            0                0\n'+
                   '2       2       Quien duerme mucho, poco              0                0\n'+
                   '2       3       De tal palo tal astilla               0                0\n'+
                   '2       4       No hay peor ciego que el              0                0\n'+
                   '2       5       El que no corre, vuela                0                0\n'+
                   '2       6       Nadie sabe lo que tiene               0                0\n'+
                   '2       7       Al mal tiempo buena cara              0                0\n'+
                   '2       8       A buen entendedor pocas               0                0\n'+
                   '2       9       A caballo regalado no se              0                0\n'+
                   '2       10      Barriga llena, corazón                0                0\n'+
                   '2       11      Más vale estar solo que mal           0                0\n'+
                   '2       12      El que busca encuentra                0                0\n'+
                   '2       13      Dime con quién andas                  0                0\n'+
                   '2       14      Haz bien y no mires a quien           0                0\n'+
                   '2       15      La esperanza es lo último             0                0\n'+
                   '2       16      Lo prometido es deuda                 0                0\n'+
                   '2       17      La pereza es la madre de              0                0\n'+
                   '3       1       -¡Estás obsesionado con la            0                0\n'+
                   '3       2       -¿Por qué estás hablando              0                0\n'+
                   '3       3       — Buenos días, me gustaría            0                0\n'+
                   '3       4       — ¡Camarero! Este filete              0                0\n'+
                   '3       5       — Abuelo, ¿por qué estás              0                0\n'+
                   '3       6       — ¿Para que va una caja               0                0\n'+
                   '3       7       — ¿Por qué se suicidó el              0                0\n'+
                   '3       8       — ¿Qué le dice un huevo               0                0\n'+
                   '3       9       — ¿Qué le dice un espagueti           0                0\n'+
                   '3       10      — ¿Qué le dice un grano de            0                0\n'+
                   '3       11      —¿Qué le dice un árbol a otro         0                0\n'+
                   '3       12      — ¿Cómo se llama el primo             0                0\n'+
                   '3       13      — Soy celíaca.                        0                0\n'+
                   '3       14      — ¿Sabes por qué no se                0                0\n'+
                   '3       15      — ¿Por qué el mar no se seca?         0                0\n'+
                   '3       16      — ¿De qué se quejan siempre           0                0\n'+
                   '3       17      — Mamá, en el cole me llaman          0                0\n'+
                   '----------------------------------------------------------------------------')
    archivov.close()
    arventa10 = open('contadores/venta10.txt','w')
    arventa10.write(str(0))
    arventa10.close()
    arventa11 = open('contadores/venta11.txt','w')
    arventa11.write(str(0))
    arventa11.close()
    arventa12 = open('contadores/venta12.txt','w')
    arventa12.write(str(0))
    arventa12.close()
    arventa13 = open('contadores/venta13.txt','w')
    arventa13.write(str(0))
    arventa13.close()
    arventa14 = open('contadores/venta14.txt','w')
    arventa14.write(str(0))
    arventa14.close()
    arventa15 = open('contadores/venta15.txt','w')
    arventa15.write(str(0))
    arventa15.close()
    arventa16 = open('contadores/venta16.txt','w')
    arventa16.write(str(0))
    arventa16.close()
    arventa17 = open('contadores/venta16.txt','w')
    arventa17.write(str(0))
    arventa17.close()
    arventa18 = open('contadores/venta18.txt','w')
    arventa18.write(str(0))
    arventa18.close()
    arventa19 = open('contadores/venta19.txt','w')
    arventa19.write(str(0))
    arventa19.close()
    arventa110 = open('contadores/venta110.txt','w')
    arventa110.write(str(0))
    arventa110.close()
    arventa111 = open('contadores/venta111.txt','w')
    arventa111.write(str(0))
    arventa111.close()
    arventa112 = open('contadores/venta112.txt','w')
    arventa112.write(str(0))
    arventa112.close()
    arventa113 = open('contadores/venta113.txt','w')
    arventa113.write(str(0))
    arventa113.close()
    arventa114 = open('contadores/venta114.txt','w')
    arventa114.write(str(0))
    arventa114.close()
    arventa115 = open('contadores/venta115.txt','w')
    arventa115.write(str(0))
    arventa115.close()
    arventa116 = open('contadores/venta116.txt','w')
    arventa116.write(str(0))
    arventa116.close()
    arventa21 = open('contadores/venta21.txt','w')
    arventa21.write(str(0))
    arventa21.close()
    arventa22 = open('contadores/venta22.txt','w')
    arventa22.write(str(0))
    arventa22.close()
    arventa23 = open('contadores/venta23.txt','w')
    arventa23.write(str(0))
    arventa23.close()
    arventa24 = open('contadores/venta24.txt','w')
    arventa24.write(str(0))
    arventa24.close()
    arventa25 = open('contadores/venta25.txt','w')
    arventa25.write(str(0))
    arventa25.close()
    arventa26 = open('contadores/venta26.txt','w')
    arventa26.write(str(0))
    arventa26.close()
    arventa27 = open('contadores/venta27.txt','w')
    arventa27.write(str(0))
    arventa27.close()
    arventa28 = open('contadores/venta28.txt','w')
    arventa28.write(str(0))
    arventa28.close()
    arventa29 = open('contadores/venta29.txt','w')
    arventa29.write(str(0))
    arventa29.close()
    arventa210 = open('contadores/venta210.txt','w')
    arventa210.write(str(0))
    arventa210.close()
    arventa211 = open('contadores/venta211.txt','w')
    arventa211.write(str(0))
    arventa211.close()
    arventa212 = open('contadores/venta212.txt','w')
    arventa212.write(str(0))
    arventa212.close()
    arventa213 = open('contadores/venta213.txt','w')
    arventa213.write(str(0))
    arventa213.close()
    arventa214 = open('contadores/venta214.txt','w')
    arventa214.write(str(0))
    arventa214.close()
    arventa215 = open('contadores/venta215.txt','w')
    arventa215.write(str(0))
    arventa215.close()
    arventa216 = open('contadores/venta216.txt','w')
    arventa216.write(str(0))
    arventa216.close()
    arventa217 = open('contadores/venta217.txt','w')
    arventa217.write(str(0))
    arventa217.close()
    arventa31 = open('contadores/venta31.txt','w')
    arventa31.write(str(0))
    arventa31.close()
    arventa32 = open('contadores/venta32.txt','w')
    arventa32.write(str(0))
    arventa32.close()
    arventa33 = open('contadores/venta33.txt','w')
    arventa33.write(str(0))
    arventa33.close()
    arventa34 = open('contadores/venta34.txt','w')
    arventa34.write(str(0))
    arventa34.close()
    arventa35 = open('contadores/venta35.txt','w')
    arventa35.write(str(0))
    arventa35.close()
    arventa36 = open('contadores/venta36.txt','w')
    arventa36.write(str(0))
    arventa36.close()
    arventa37 = open('contadores/venta37.txt','w')
    arventa37.write(str(0))
    arventa37.close()
    arventa38 = open('contadores/venta38.txt','w')
    arventa38.write(str(0))
    arventa38.close()
    arventa39 = open('contadores/venta39.txt','w')
    arventa39.write(str(0))
    arventa39.close()
    arventa310 = open('contadores/venta310.txt','w')
    arventa310.write(str(0))
    arventa310.close()
    arventa311 = open('contadores/venta311.txt','w')
    arventa311.write(str(0))
    arventa311.close()
    arventa312 = open('contadores/venta312.txt','w')
    arventa312.write(str(0))
    arventa312.close()
    arventa313 = open('contadores/venta313.txt','w')
    arventa313.write(str(0))
    arventa313.close()
    arventa314 = open('contadores/venta314.txt','w')
    arventa314.write(str(0))
    arventa314.close()
    arventa315 = open('contadores/venta315.txt','w')
    arventa315.write(str(0))
    arventa315.close()
    arventa316 = open('contadores/venta316.txt','w')
    arventa316.write(str(0))
    arventa316.close()
    arventa317 = open('contadores/venta317.txt','w')
    arventa317.write(str(0))
    arventa317.close()
    numt2 = open('contadores/numero transaccion.txt','w')
    numt2.write(str(0))
    numt2.close()
    
#variable del canvas con el resumen de ventas
canvas2 = 0
#guarda el canvas del resumen
def guardar_resumenf(guardar_resumen,canvas2):
    canvas2.place_forget()
    guardar_resumen.place_forget()


#abre el resumen
def resumen1():
    archivor = open('resumen ventas.txt','r')
    contenidore=archivor.read()
    
    canvas2 = Canvas(principal , width= 300, height = 680, bg = "white")
    resumen_ventas1 = Label(canvas2,text = contenidore,font= ('Times New Roman',7),bg= 'white',fg= 'black')
    resumen_ventas1.place(x=0,y=0)
    canvas2.place(x=0, y=0)
    guardar_resumen= Button(principal, text = 'cerrar',command =  lambda: guardar_resumenf(guardar_resumen,canvas2))
    guardar_resumen.place(x=350, y=0)
    

#boton de reset
reset= Button(principal,text= ' Reset', command = reset)
##boton apagar
apagar= Button(principal,text= ' Apagar/Turn off',command = cerrar)
##boton resumen de ventas
Resumen= Button(principal,text= ' Resumen de ventas/Sales summary',command = resumen1)
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
    global monedas_ingresadas
    if bandera_regresar == True:
        bandera_regresar = False
        bandera_admi = True
        bandera = True
        monedas_ingresadas = 0
        titulo_contadorf.configure(text= '₡' + str(monedas_faltantes))
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
