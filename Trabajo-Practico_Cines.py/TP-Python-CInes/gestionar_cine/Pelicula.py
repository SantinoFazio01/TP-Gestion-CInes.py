from gestionar_cine.PeliculasG import PeliculasG


class Pelicula(PeliculasG):
  def __init__(self, titulo, duracion, genero):
    super().__init__(titulo, duracion, genero, estudioAnimacion=None)