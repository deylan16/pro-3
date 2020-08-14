class Tiquete:
    def __init__(self,tipo,codigo,mensaje,precio,ventas):
        self.tipo = tipo
        self.codigo = codigo
        self.mensaje = mensaje
        self.precio = precio
        self.ventas = ventas
    def set_ventas(self, ventas):
        self.ventas = ventas
    def get_precio(self):
        return self.precio
    def get_mensaje(self):
        return self.mensaje
    def get_codigo(self):
        return self.codigo
        
class Tabla(Tiquete):
    def __init__(self,tipo,codigo,mensaje,precio,ventas,numero_transaccion,fecha,hora,monto,pago,vuelto):
        Tiquete.__init__(self,tipo,codigo,mensaje,precio,ventas)
        self.numero_transaccion = numero_transaccion
        self.fecha = fecha
        self.hora = hora
        self.monto = monto
        self.pago = pago
        self.vuelto = vuelto
    def set_fecha(self,fecha):
        self.fecha = fecha
    def set_hora(self,hora):
        self.hora = hora
    def set_monto(self,monto):
        self.monto = monto
    def set_pago(self,pago):
        self.pago = pago
    def set_vuelto(self,vuelto):
        self.vuelto = vuelto
    def set_numero_transaccion(self,numero_transaccion):
        self.numero_transaccion = numero_transaccion
    def get_datos(self):
        resultado = str(self.numero_transaccion)+"       "+ str(self.fecha)+"          "+ str(self.hora)+"                  "+ str(self.tipo)+"                  "+ str(self.codigo)+"                  "+ str(self.monto)+"                  "+ str(self.pago)+"                  "+ str(self.vuelto)
        print(resultado)
        

consejo1 = Tabla(1,1,"Lo que los demas piensen de ti,\n no es tu problema",20,0,0,0,0,0,0,0)
consejo2 = Tabla(1,2,"No pierdas tu preciado tiempo en chismes",50,0,0,0,0,0,0,0)
consejo3 = Tabla(1,3,"Sueña mas cuando estés despierto",50,0,0,0,0,0,0,0)
consejo4 = Tabla(1,4,"No tienes que ganar todas las discusiones.\n Unas veces estarás de acuerdo y otras no",20,0,0,0,0,0,0,0)
consejo5 = Tabla(1,5,"No compares tu vida con la de los demás.\n No tienes idea de como es su día a día",75,0,0,0,0,0,0,0)
consejo6 = Tabla(1,6,"La vida es demasiado corta para estar\n odiando a las personas. Así que deshazte de esos sentimientos negativos",100,0,0,0,0,0,0,0)
consejo7 = Tabla(1,7,"Nadie mas está al cargo de tu felicidad.\n Excepto tú",25,0,0,0,0,0,0,0)
consejo8 = Tabla(1,8,"Ríe y sonríe más a menudo",20,0,0,0,0,0,0,0)
consejo9 = Tabla(1,9,"Duerme 8 horas al dias",100,0,0,0,0,0,0,0)
consejo10 = Tabla(1,10,"Toma agua",200,0,0,0,0,0,0,0)
consejo11 = Tabla(1,11,"Olvida los problemas del pasado.\n No estés recordando a tu compañeros\n por sus errores del pasado",150,0,0,0,0,0,0,0)
consejo12 = Tabla(1,12,"Cualquiera que se la situación -buena o mala-,\n cambiará",75,0,0,0,0,0,0,0)
consejo13 = Tabla(1,13,"No importa cómo te sientas, levántate,\n vístete y sal a la calle",125,0,0,0,0,0,0,0)
consejo14 = Tabla(1,14,"Sé agradecido con lo que tienes",120,0,0,0,0,0,0,0)
consejo15 = Tabla(1,15,"No hagas siempre lo que amas,\n ama siempre lo que haces",140,0,0,0,0,0,0,0)
consejo16 = Tabla(1,16,"Vive el hoy, por que el ayer ya se ha ido,\n y puede que no haya un mañana",20,0,0,0,0,0,0,0)

consejos = [consejo1,consejo2,consejo3,consejo4,consejo5,consejo6,consejo7,consejo8,consejo9,consejo10,consejo11,consejo12,consejo13,consejo14,consejo15,consejo16]

dicho1 = Tabla(2,1,"No hay mal que por bien no venga",20,0,0,0,0,0,0,0)
dicho2 = Tabla(2,2,"Quien duerme mucho, poco aprende",40,0,0,0,0,0,0,0)
dicho3 = Tabla(2,3,"De tal palo tal astilla",60,0,0,0,0,0,0,0)
dicho4 = Tabla(2,4,"No hay peor ciego que el que no quiere ver",75,0,0,0,0,0,0,0)
dicho5 = Tabla(2,5,"El que no corre, vuela",45,0,0,0,0,0,0,0)
dicho6 = Tabla(2,6,"Nadie sabe lo que tiene hasta que lo pierde",100,0,0,0,0,0,0,0)
dicho7 = Tabla(2,7,"Al mal tiempo buena cara",20,0,0,0,0,0,0,0)
dicho8 = Tabla(2,8,"A buen entendedor pocas palabras",80,0,0,0,0,0,0,0)
dicho9 = Tabla(2,9,"A caballo regalado no se le mira el diente",55,0,0,0,0,0,0,0)
dicho10 = Tabla(2,10,"Barriga llena, corazón contento",45,0,0,0,0,0,0,0)
dicho11 = Tabla(2,11,"Más vale estar solo que mal acompañado",85,0,0,0,0,0,0,0)
dicho12 = Tabla(2,12,"El que busca encuentra",105,0,0,0,0,0,0,0)
dicho13 = Tabla(2,13,"Dime con quién andas y te diré quien eres",35,0,0,0,0,0,0,0)
dicho14 = Tabla(2,14,"Haz bien y no mires a quien",55,0,0,0,0,0,0,0)
dicho15 = Tabla(2,15,"La esperanza es lo último que se pierde",60,0,0,0,0,0,0,0)
dicho16 = Tabla(2,16,"Lo prometido es deuda",40,0,0,0,0,0,0,0)
dicho17 = Tabla(2,17,"La pereza es la madre ee todos los vicios",20,0,0,0,0,0,0,0)

dichos = [dicho1,dicho2,dicho3,dicho4,dicho5,dicho6,dicho7,dicho8,dicho9,dicho10,dicho11,dicho12,dicho13,dicho14,dicho15,dicho16,dicho17]

chiste1 = Tabla(3,1,"-¡Estás obsesionado con la comida!\n — No sé a que te refieres croquetamente",200,0,0,0,0,0,0,0)
chiste2 = Tabla(3,2,"-¿Por qué estás hablando con esos zapatos?\n — Porque pone converse",140,0,0,0,0,0,0,0)
chiste3 = Tabla(3,3,"— Buenos días, me gustaría alquilar Batman Eternamente.\n — No es posible, tiene que devolverla mañana",300,0,0,0,0,0,0,0)
chiste4 = Tabla(3,4,"— ¡Camarero! Este filete tiene muchos nervios.\n — Normal, es la primera vez que se lo comen",140,0,0,0,0,0,0,0)
chiste5 = Tabla(3,5,"— Abuelo, ¿por qué estás delante del ordenador con los ojos cerrados?\n — Es que Windows me ha dicho que cierre las pestañas",200,0,0,0,0,0,0,0)
chiste6 = Tabla(3,6,"— ¿Para que va una caja al gimnasio?\n — Para hacerse una caja fuerte",300,0,0,0,0,0,0,0)
chiste7 = Tabla(3,7,"— ¿Por qué se suicidó el libro de matemáticas?\n — Porque tenía muchos problemas",250,0,0,0,0,0,0,0)
chiste8 = Tabla(3,8,"— ¿Qué le dice un huevo a una sartén?\n — Me tienes frito",300,0,0,0,0,0,0,0)
chiste9 = Tabla(3,9,"— ¿Qué le dice un espagueti a otro?\n — ¡El cuerpo me pide salsa?",130,0,0,0,0,0,0,0)
chiste10 = Tabla(3,10,"— ¿Qué le dice un grano de arena a otro en el desierto?\n — Creo que nos siguen",170,0,0,0,0,0,0,0)
chiste11 = Tabla(3,11,"—¿Qué le dice un árbol a otro?\n — ¡Qué pasa tronco!",180,0,0,0,0,0,0,0)
chiste12 = Tabla(3,12,"— ¿Cómo se llama el primo vegano de Bruce Lee?\n — Broco Lee.",150,0,0,0,0,0,0,0)
chiste13 = Tabla(3,13,"— Soy celíaca.\n — Encantado, yo Antoniaco",240,0,0,0,0,0,0,0)
chiste14 = Tabla(3,14,"— ¿Sabes por qué no se puede discutir con un DJ?\n — Porque siempre están cambiando de tema",280,0,0,0,0,0,0,0)
chiste15 = Tabla(3,15,"— ¿Por qué el mar no se seca?\n — Porque no tiene toalla",210,0,0,0,0,0,0,0)
chiste16 = Tabla(3,16,"— ¿De qué se quejan siempre los astronautas?\n — De falta de espacio",65,0,0,0,0,0,0,0)
chiste17 = Tabla(3,17," — Mamá, en el cole me llaman despistado.\n — Niño, que esta no es tu casa",20,0,0,0,0,0,0,0)

chistes = [chiste1,chiste2,chiste3,chiste4,chiste5,chiste6,chiste7,chiste8,chiste9,chiste10,chiste11,chiste12,chiste13,chiste14,chiste15,chiste16,chiste17]

