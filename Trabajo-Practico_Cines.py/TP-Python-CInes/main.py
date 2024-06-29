from gestionar_cine.Cine import Cine
from gestionar_cine.GestionCine import GestionCine
from gestionar_cine.PeliculasG import PeliculasG
from gestionar_cine.Pelicula import Pelicula
from gestionar_cine.PeliculaAnimada import PeliculaAnimada

gestion=GestionCine("base/cine.db")

#CREAR TABLAS  
#gestion.crearTablaCine()
#gestion.crearTablaPeli()
#gestion.crearTablaPeliAni()

#AGREGAR INFO
#gestion.addPelicula("El padrino", 175, "Drama")
#gestion.addPelicula_animada("intensamente",175, "Drama","disney")
#gestion.addCine("cine 1","direccion")

#MODIFICAR INFO
#gestion.traerPeliAnimadas()
#gestion.modificarPeliculaAnimada()
#gestion.traerPeliAnimadas()

#gestion.traerPeli()
#gestion.modificarPelicula()
#gestion.traerPeli()

#gestion.modificarCine()
#gestion.traerCine()

#BORRAR EN CADA OCACION
#gestion.borrarPelicula()
#gestion.borrarCine()
#gestion.borrarPeliculaAnimada()
#gestion.traerCine()
#gestion.traerPeli()
#gestion.traerPeliAnimadas()

peli1=PeliculasG("El padrino", 175, "Drama",None)
peli2=PeliculaAnimada("intensamente",175, "Drama","disney")
cine1=Cine("yanel", "av 32")

cine1.agregar_pelicula(peli1)
cine1.agregar_pelicula(peli2)
cine1.mostrar_info()

gestion.cerrarConexion()