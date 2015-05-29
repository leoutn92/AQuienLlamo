from vista import *
import datetime
class VistaCliente(Vista):
<<<<<<< HEAD
  def __init__(self,main,cliente):
   self.main=main
   self.cliente=cliente
   self.menuCliente()
  def menuCliente(self):
   opsiones=['buscar servicios','ver pedidos','lo quiero ya','editar perfil','salir']
   titulo='Menu clientes AQL'
   ops=self.menu(titulo,opsiones)
   if ops=='buscar servicios':
    self.menuServicios()
   elif ops== 'ver pedidos':
    pass
   elif ops== 'lo quiero ya':
    pass
   elif ops== 'editar perfil':
    pass
  def cargarPedido(self):
    dic=dict()
    dic['LQY']=False
    dic['descripsion']=input('Contanos cual es tu problema: ')
    ops=self.ops('Desea que el pedido sea atendido en una fecha determinada: ','si','no')
    if (ops=='si'):
     dic['fechaReserva']=self.cargarFecha()
    return dic  
  def menuServicios(self):     
   ops=self.ops('desea \n c-buscar servicios por categoria \n n-buscar servicios por nombre \n r-ver servicios recientemente solicitados \n v-volver al menu principal \n','c','n','r','v')   
   if ops=='v':
    self.menuCliente()
=======
  def cargarPedido(self):
    dic=dict()
    dic['LQY']=False
    dic['descripsion']=input('Contanos cual es tu problema')
    ops=self.ops('Desea que el pedido sea atendido en una fecha determinada: ','si','no')
    if (ops=='si'):
     mes=int(input('ingrese mes: '))
     dia=int(input('ingrese dia: '))
     anio=int(input('ingrese anio: '))
     hora=int(input('ingrese hora: '))
     dic['fechaReserva']=datetime.datetime(anio,mes,dia,hora)
    return dic  
  def MenuServicios(self):
   ops=self.ops('desea \n c-buscar servicios por categoria \n n-buscar servicios por nombre \n r-ver servicios recientemente solicitados \n v-volver al menu principal \n','c','n','r')
>>>>>>> 373ca46b5dc5b7f82963299abd68f7ce7e9f79a0
   if ops=='c':
    categorias=self.main.verCateServ()
    opsiones=list()
    opsiones.extend(categorias)
    opsiones.append('agregar nueva categoria')
<<<<<<< HEAD
    titulo= 'seleccione una opsion'
    cat=self.menu(titulo,opsiones)
=======
    cat=self.listar('seleccione una opsion',opsiones)
>>>>>>> 373ca46b5dc5b7f82963299abd68f7ce7e9f79a0
    if cat in categorias:
     servicios=self.main.buscarServXCat(cat)
     if servicios==None:
      print('No hay servicios disponibles')
     else:
      print('Seleccione el servicio que mejor se ajuste a sus necesidades')
      j=1
      for i in servicios:
       linea=str(j)+' '
       for x in i:
        linea=linea+x
        linea=linea+': '
        linea=linea+i[x]
        linea=linea+' '
       j=j+1
       print(linea)
      print('%s volver a menu principal de cliente'%j)
<<<<<<< HEAD
=======
      print('Seleccione el servicio que mejor se ajuste a sus necesidades')
>>>>>>> 373ca46b5dc5b7f82963299abd68f7ce7e9f79a0
      ops=int(input())
      while not (ops in range(1,j+1)):
       ops=int(input())
      if ops!=j:
<<<<<<< HEAD
       dicPedido=self.cargarPedido()
       proveedor=servicios[ops-1]['Proveedor']
       self.main.agregarPedido(dicPedido,self.cliente,proveedor,cat)
       print('pedido agregado exitosamente')
       self.menuServicios()     
=======
       dic=self.cargarPedido()
       proveedor=servicios[ops-1]['Proveedor']
>>>>>>> 373ca46b5dc5b7f82963299abd68f7ce7e9f79a0
       