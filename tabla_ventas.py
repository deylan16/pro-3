
class tabla_ventas():
    def __init__(self,numero_transaccion,fecha,hora,tipo,codigo_mensaje,monto,pago,vuelto):
        self.numero_transaccion = numero_transaccion
        self.fecha = fecha
        self.hora = hora
        self.tipo = tipo
        self.codigo_mensaje = codigo_mensaje
        self.monto = monto
        self.pago = pago
        self.vuelto = vuelto
    def set_fecha(self,fecha):
        self.fecha = fecha
    def set_hora(self,hora):
        self.hora = hora
    def set_tipo(self,tipo):
        self.tipo = tipo
    def set_monto(self,monto):
        self.monto = monto
    def set_pago(self,pago):
        self.pago = pago
    def set_vuelto(self,vuelto):
        self.vuelto = vuelto
    def set_numero_transaccion(self,numero_transaccion):
        self.numero_transaccion = numero_transaccion
        
    def get_datos(self):
        resultado = str(self.numero_transaccion)+"       "+ str(self.fecha)+"          "+ str(self.hora)+"                  "+ str(self.tipo)+"                  "+ str(self.codigo_mensaje)+"                  "+ str(self.monto)+"                  "+ str(self.pago)+"                  "+ str(self.vuelto)
        print(resultado)
        

nuevo = tabla_ventas(0,0,0,0,0,0,0,0)
