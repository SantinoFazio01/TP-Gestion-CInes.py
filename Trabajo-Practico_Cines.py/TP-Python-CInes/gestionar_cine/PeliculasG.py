class PeliculasG:
  def __init__(self,titulo,duracion,genero,estudioAnimacion):
    self.titulo = titulo
    self.duracion=duracion
    self.genero=genero
    self.estudioAnimacion=estudioAnimacion

  def get_titulo(self):
    return self.titulo

  def set_titulo(self,tit):
    self.titulo=tit
  def get_duracion(self):
     return self.duracion

  def set_duracion(self,duracione):
     self.duracion=duracione

  def get_genero(self):
     return self.genero

  def set_genero(self,generos):
     self.genero=generos

  def get_estudioAnimacion(self):
   return self.estudioAnimacion

  def set_estudioAnimacion(self,est):
   self.estudioAnimacion=est  


