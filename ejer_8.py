from ejer_7 import *

class Celular(Telefono,Camara,ReproductorMp3):
	def __init__(self,marca,model,color,numero):
		super().__init__(marca,model,color,numero)
		self.__bateria = 50

	def mensajear(self):
		self.mensaje = input('Ingrese mensaje: ')
		print('enviando mensaje')

	def filmar(self):
		print("filmando")

	def ver_bateria(self):
		print('Batería actual: ',self.__bateria,'%')

	def cargar_bateria(self):
		while self.__bateria < 100:
			self.__bateria += 10
			print('carga: ',self.__bateria,'%') 
				
		print('Carga finalizada!')	


	
celular = Celular('SAMSUNG','S10','NEGRO',303456)
# jvgjgfhjjbjbjgjjgjgjngj
# jgjgjjghjhjhjhjh

# asfjaskjfb

# print(__name__)