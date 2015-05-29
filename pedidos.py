import datetime
class Pedido:
 estados=['enviado','aceptado','cancelado','terminado','pagado']
 def __init__(self,dic):
  self.LQY=dic.get('LQY')
  self.fechaReserva=dic.get('fechaReserva')
  self.descripsion=dic['descripsion']
  self.fechaEmision=datetime.datetime.now()
  self.estado='enviado'