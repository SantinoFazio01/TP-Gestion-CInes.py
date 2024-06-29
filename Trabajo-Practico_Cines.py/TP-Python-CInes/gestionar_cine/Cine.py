from gestionar_cine import GestionCine
from gestionar_cine.PeliculasG import PeliculasG

class Cine:
  def __init__(self,nombre,direccion):
    self.nombre = nombre
    self.direccion = direccion
    self.peliculas = []

  def get_nombre(self):
    return self.nombre

  def set_nombre(self,nombres):
    self.nombre=nombres

  def get_direccion(self):
    return self.direccion
  
  def set_direccion(self,direcciones):
    self.direccion=direcciones

  def agregar_pelicula(self, pelicula):

    
      self.peliculas.append(pelicula)

  def mostrar_info(self):
      for pelicula in self.peliculas:
          print(f"Título: {pelicula.get_titulo()}")
          print(f"Duración: {pelicula.get_duracion()}")
          print(f"Género: {pelicula.get_genero()}")
          if pelicula.get_estudioAnimacion() != None:
            print(f"estudio de animacion: {pelicula.get_estudioAnimacion()}")
          print("--------------------")



  