from vista import *
import datetime
class VistaCliente(Vista):
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
   if ops=='c':
    categorias=self.main.verCateServ()
    opsiones=list()
    opsiones.extend(categorias)
    opsiones.append('agregar nueva categoria')
    cat=self.listar('seleccione una opsion',opsiones)
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
      print('Seleccione el servicio que mejor se ajuste a sus necesidades')
      ops=int(input())
      while not (ops in range(1,j+1)):
       ops=int(input())
      if ops!=j:
       dic=self.cargarPedido()
       proveedor=servicios[ops-1]['Proveedor']
       