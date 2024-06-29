from gestionar_cine.PeliculasG import PeliculasG


class PeliculaAnimada(PeliculasG):
  def __init__(self, titulo, duracion, genero, estudioAnimacion):
    super().__init__(titulo, duracion, genero, estudioAnimacion)