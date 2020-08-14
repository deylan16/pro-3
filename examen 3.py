#atributos:nom, valor
#metodos:get_valor,get_nom
class Nodo:
    def __init__(self,nom, valor):
        self.next = None
        self.nom = nom
        self.nota = valor
    def get_nota(self):
        return self.nota
    def get_nom(self):
        return self.nom

#atributos:head,largo
#metodos:appe,printL,promedio,largo
class Lista:
    def __init__(self):
        self.head = None
        self.largo = 0
    #E:nom,valor
    #S:nuevo nodo en la lista
    #R:string y nomero entero
    def appe(self,nom, valor):
        if isinstance(nom,str) and isinstance(valor, int):
            self.largo += 1
            if self.head == None :
                self.head = Nodo(nom,valor)
            else:
                tmp = self.head
                while tmp.next != None :
                    tmp = tmp.next
                tmp.next = Nodo(nom,valor)
        else:
            return 'Datos incorrectos'
    #E:vacio
    #S:nodos en forma de lista
    #R:vacio
    def printL(self):
        Nodo = self.head
        cuenta = 0
        todo = '['
        while Nodo != None:
            cuenta += 1
            todo += Nodo.get_nom () +':'+ str(Nodo.get_nota())
            if cuenta < self.largo:
                todo += ','
            Nodo = Nodo.next
        todo +=']'
        print(todo)

    #E:vacio
    #S:promedio de las notas
    #R:vacio
    def promedio(self):
        nodo = self.head
        prome = 0
        while nodo != None:
            prome += nodo.get_nota()
            nodo = nodo.next
        print('Promedio de las notas:'+ str(prome/self.largo))
    #E:vacio
    #S:nodos en forma de lista
    #R:vacio
    def borra(self, estudiante): 
        if self.head == None:
            print("Lista vacia")
        elif isinstance(estudiante,str):
            if self.head.get_nom() == estudiante:
                self.head = self.head.next
                self.largo -= 1
            else:
                esta = False
                tmp = self.head
                while tmp.next != None:
                    if tmp.next.get_nom() == estudiante:
                        tmp.next = tmp.next.next
                        self.largo -= 1
                        esta = True
                        break
                    else:
                        tmp = tmp.next
                if esta == False:
                    return "Elemento no existe"
        else:
            print('Datos incorectos')


class Estudiante:
    def __init__(self,nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet
        self.lista_de_cursos = None

    def get_carnet(self):
        return self.carnet
    def get_nombre(self):
        return self.nombre
    def get_cursos(self):
        return self.lista_de_cursos

    def agregar_curso(codigo, semestre, año, nota):
        check = False
        for i in self.lista_de_cursos:
            if self.lista_de_cursos[i][0] == codigo:
                if self.lista_de_cursos[i][1] == semestre and self.lista_de_cursos[i][2] == año:
                    check = True
                    break
        if check:
            print("Curso ya fue llevado en tiempo en tiempo indicado")
        else:
            self.lista_de_cursos.append([codigo, semestre, año, nota])
    def mostrar(self):
        print("carnet: ", self.carnet, "\n", "nombre: ", self.nombre)
        if self.lista_de_cursos == None:
            pass
        else:
            for i in self.lista_de_cursos:
                print("curso: ", self.lista_de_cursos[i])



def promedio(carnet, lista):
    check = False
    for estudiante in lista:
        if estudiante.carnet == carnet:
            check = True
            estudiante.mostrar()
            break
    if not check:
        print("estudiante no existe")



