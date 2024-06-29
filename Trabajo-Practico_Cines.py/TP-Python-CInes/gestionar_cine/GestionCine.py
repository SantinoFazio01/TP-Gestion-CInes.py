import sqlite3 as sql

class GestionCine: 
  def __init__(self, nombreBD):
      self.conexion = sql.connect(nombreBD)
      self.cursor = self.conexion.cursor()


#cine
  
  def crearTablaCine(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS cine(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, direccion TEXT)''')
    self.conexion.commit()
    
  def addCine(self, nom, direc):
    self.cursor.execute('''INSERT INTO cine(nombre,direccion) VALUES (?, ?)''', (nom, direc))
    self.conexion.commit()
    
  def traerCine(self):
    self.cursor.execute('''SELECT * FROM cine''')
    self.resultado = self.cursor.fetchall()
    for res in self.resultado:
        print(res)

  def modificarCine(self):
    id = input('''Ingrese el id del cine a modificar: ''')
    nom = input('''Ingrese el nombre del cine: ''')
    direc = input('''Ingrese la direccion del cine: ''')
    self.cursor.execute('''UPDATE cine SET nombre = ?, direccion = ? WHERE id = ?;''', (nom, direc,id))
    self.conexion.commit()

  def borrarCine(self):
    id = input('''Ingrese el id del cine a borrar: ''')
    self.cursor.execute('''DELETE FROM cine WHERE id = ?;''', (id,))
    self.conexion.commit()
    
#peliculas
  def crearTablaPeli(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS pelicula(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, duracion INTEGER,genero TEXT)''')
    self.conexion.commit()
    

  def addPelicula(self,titulo, duracion,genero):
    self.cursor.execute('''INSERT INTO pelicula(titulo,duracion,genero) VALUES (?, ?, ?)''', (titulo, duracion,genero))
    self.conexion.commit()

  def traerPeli(self):
    self.cursor.execute('''SELECT * FROM pelicula''')
    self.resultado = self.cursor.fetchall()
    for res in self.resultado:
        print(res)

  def modificarPelicula(self):
    id = input('''Ingrese el id de la pelicula a modificar: ''')
    titulo = input('''Ingrese el titulo de la pelicula: ''')
    duracion = input('''Ingrese la duracion de la pelicula ''')
    genero = input('''Ingrese el genero de la pelicula ''')
    self.cursor.execute('''UPDATE pelicula SET titulo = ?, duracion = ?, genero = ? WHERE id = ?;''', (titulo, duracion, genero, id))
    self.conexion.commit()

  def borrarPelicula(self):
    id = input('''Ingrese el id de la pelicula a eliminar: ''')
    self.cursor.execute('''DELETE FROM pelicula WHERE id = ?;''', (id,))
    self.conexion.commit()

#peliculas animadas
  def crearTablaPeliAni(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculaAnimada(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, duracion INTEGER, genero TEXT, estudioAnimacion TEXT)''')
    self.conexion.commit()
  
  def addPelicula_animada(self,titulo, duracion,genero,estudioAnimacion):
    self.cursor.execute('''INSERT INTO peliculaAnimada(titulo,duracion,genero,estudioAnimacion) VALUES (?,?,?,?)''', (titulo, duracion,genero,estudioAnimacion))
    self.conexion.commit()

  def traerPeliAnimadas(self):
    self.cursor.execute('''SELECT * FROM peliculaAnimada''')
    self.resultado = self.cursor.fetchall()
    for res in self.resultado:
        print(res)

  def modificarPeliculaAnimada(self):
    id = input('''Ingrese el id de la pelicula a modificar: ''')
    titulo = input('''Ingrese el titulo de la pelicula: ''')
    duracion = input('''Ingrese la duracion de la pelicula ''')
    genero = input('''Ingrese el genero de la pelicula ''')
    estudioAnimacion = input('''Ingrese el estudio de animacion de la pelicula ''''')
    self.cursor.execute('''UPDATE peliculaAnimada SET titulo = ?, duracion = ?, genero = ?, estudioAnimacion = ? WHERE id = ?;''', (titulo, duracion, genero, estudioAnimacion, id))
    self.conexion.commit()

  def borrarPeliculaAnimada(self):
    id = input('''Ingrese el id de la pelicula animada a eliminar: ''')
    self.cursor.execute('''DELETE FROM peliculaAnimada WHERE id = ?;''', (id,))
    self.conexion.commit()
  
  def cerrarConexion(self):
    self.cursor.close()
    self.conexion.close()