'''
  Universidad del Valle de Guatemala
  Bases de datos 1
  Proyecto 2

  Integrantes:
    - Gabriel Vicente 20498
    - Maria Isabel Solano 20504
    - Christopher García 20541
'''

#Se importan librerias utilizadas para la conexión con Postgresql
import psycopg2
import psycopg2.extras
import random

#--------------------------------------------------- IMPORTANTE ---------------------------------------------------
#Cambiar estos valores para poder conectarse a la base de datos local
connect_base = psycopg2.connect("host=localhost dbname=Proyecto_3 user=postgres port=5432 password=Basededatos2022")
cursor = connect_base.cursor(cursor_factory=psycopg2.extras.DictCursor)
#-------------------------------------------------------------------------------------------------------------------

#Funciones con queries para ingresar datos a la base de datos
def Upload_Cuenta(Correo, Contra, TipoCuenta, IngresoF, IngresoH):
  DatosC = (Correo, Contra, TipoCuenta, True, IngresoF, IngresoH)
  Query = "INSERT INTO Cuenta VALUES (%s, %s, %s, %s, %s, %s)"
  cursor.execute(Query, DatosC)
  connect_base.commit() 
  
def Upload_Perfiles(CodigoP, Num, Nombre_P, activo):
  DatosP = (CodigoP, Num, Nombre_P, True, activo)
  Query = "INSERT INTO Perfiles VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(Query, DatosP)
  connect_base.commit() 
  
def Upload_CuentaPerfiles(CorreoC, CodigoP):
  DatosCP = (CorreoC, CodigoP)
  Query = "INSERT INTO Cuenta_Perfiles VALUES (%s, %s)"
  cursor.execute(Query, DatosCP)
  connect_base.commit() 
  
def Upload_Peliculas(CodigoPl, Titulo, Genero, yearEstreno, Duracion):
  Link = 'www.google.com'
  DatosPl = (CodigoPl, Titulo, Genero, yearEstreno, Duracion, Link)
  Query = "INSERT INTO Peliculas VALUES (%s, %s, %s, %s, %s, %s)"
  cursor.execute(Query, DatosPl)
  connect_base.commit() 
  
def Upload_Administradores (CodigoAdmin, NombreAdmin, Contra):
  DatosAdmin = (CodigoAdmin, NombreAdmin, Contra)
  Query = "INSERT INTO Administradores VALUES (%s, %s, %s)"
  cursor.execute(Query, DatosAdmin)
  connect_base.commit() 
  
def Upload_PerfilReproducciones (CodigoP, CodigoPl, VistaF, VistaH):
  DatosCP = (CodigoP, CodigoPl, VistaF, VistaH)
  Query = "INSERT INTO Perfil_Reproducciones VALUES (%s, %s, %s, %s)"
  cursor.execute(Query, DatosCP)
  connect_base.commit() 
  
def Upload_Actores (CodigoAct, NombreAct):
  DatosAct = (CodigoAct, NombreAct)
  Query = "INSERT INTO Actores VALUES (%s, %s)"
  cursor.execute(Query, DatosAct)
  connect_base.commit() 
  
def Upload_Directores (CodigoDir, NombreDir):
  DatosDir = (CodigoDir, NombreDir)
  Query = "INSERT INTO Directores VALUES (%s, %s)"
  cursor.execute(Query, DatosDir)
  connect_base.commit() 

def Upload_ActoresPeliculas (CodigoPl, CodigoAct):
  DatosActPl = (CodigoPl, CodigoAct)
  Query = "INSERT INTO Actores_Peliculas VALUES (%s, %s)"
  cursor.execute(Query, DatosActPl)
  connect_base.commit() 
  
def Upload_DirectoresPeliculas (CodigoPl, CodigoDir):
  DatosAPl = (CodigoPl, CodigoDir)
  Query = "INSERT INTO Directores_Peliculas VALUES (%s, %s)"
  cursor.execute(Query, DatosAPl)
  connect_base.commit() 
  
def Upload_Premiaciones (CodigoPl, Premiacion, Reconocimiento, Fecha):
  DatosPrem = (CodigoPl, Premiacion, Reconocimiento, Fecha)
  Query = "INSERT INTO Premiaciones VALUES (%s, %s, %s, %s)"
  cursor.execute(Query, DatosPrem)
  connect_base.commit() 

def Upload_ContenidoPerfil (CodigoP, CodigoPl, MinConsumidos, Concluida, VistaF, VistaH, VistaF2):
  DatosContP = (CodigoP, CodigoPl, MinConsumidos, Concluida, VistaF, VistaH, VistaF2)
  Query = "INSERT INTO Contenido_Perfil VALUES (%s, %s, %s, %s, %s, %s, %s)"
  cursor.execute(Query, DatosContP)
  connect_base.commit() 
  
def Upload_FavPerfil (CodigoP, CodigoPl, CorreoC, VistaF, VistaH):
  DatosFavPerfil = (CodigoP, CodigoPl, CorreoC, VistaF, VistaH)
  Query = "INSERT INTO Favoritos_Perfil VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(Query, DatosFavPerfil)
  connect_base.commit() 
  
def Upload_Anunciantes (CodigoAn, NombreAn):
  DatosAn = (CodigoAn, NombreAn)
  Query = "INSERT INTO anunciantes VALUES (%s, %s)"
  cursor.execute(Query, DatosAn)
  connect_base.commit() 
  
def Upload_Anuncios (CodigoA, CodigoAnun, Duracion, ContenidoProm, Link):
  DatosAnun = (CodigoA, CodigoAnun, Duracion, ContenidoProm, Link)
  Query = "INSERT INTO Anuncios VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(Query, DatosAnun)
  connect_base.commit()  
  
def Upload_Rep_Anuncios (CodigoA, CorreoC):
  DatosRepAnun = (CodigoA, CorreoC)
  Query = "INSERT INTO RepAnuncios VALUES (%s, %s)"
  cursor.execute(Query, DatosRepAnun)
  connect_base.commit()  

def Upload_Intentos (CorreoC, Fecha, CantidadIn):
  DatosInten = (CorreoC, Fecha, CantidadIn)
  Query = "INSERT INTO Intentos VALUES (%s, %s, %s)"
  cursor.execute(Query, DatosInten)
  connect_base.commit()  

#----------------------------------------------------------------------------------
#Funciones con queries para revisión de datos, modificación y obtención de datos 
#----------------------------------------------------------------------------------

#Query de inicio
def LogIn(CorreoC, ContraC):
  DatosLogIn = (CorreoC, ContraC,)
  Query = "SELECT * FROM Cuenta WHERE (Correo = %s AND Contrasena = %s)"
  cursor.execute(Query, DatosLogIn)
  Cuenta = cursor.fetchone()
  connect_base.commit()
  if Cuenta == None:
    return Cuenta
  else:
    return Cuenta['estado']

#Query de inicio Admin
def LogInAdmin(CodigoU, ContraU):
  DatosLogInA = (CodigoU, ContraU,)
  Query = "SELECT * FROM Administradores WHERE (Codigo = %s AND Contrasena = %s)"
  cursor.execute(Query, DatosLogInA)
  Cuenta = cursor.fetchone()
  connect_base.commit()
  if Cuenta == None:
    return Cuenta
  else:
    return Cuenta['nombre']

#----------------------------------------------------------------------------------
#                                Búsqueda de películas
#----------------------------------------------------------------------------------

#Query de Búsqueda#0: Todas las películas 
def SearchMovies():
  Query = "SELECT * FROM Peliculas"
  cursor.execute(Query)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Año: ", row[3])
    print("Duracion: ", row[4])
    print("----------------------------------\n")
  connect_base.commit()  
  
#Filtros
'''
  - Por nombre
  - Por actores
  - Por directores
  - Por género
  - Por Premios
  - Por Fecha Estreno (año)
'''
#Query de Búsqueda#1: Nombre
def SearchByName(Nombre):
  DatosSN = (Nombre,)
  Query  = "SELECT * FROM Peliculas WHERE Titulo = %s"
  cursor.execute(Query, DatosSN)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Duracion: ", row[4])
    print("----------------------------------\n")

#Query de Búsqueda#2: Actores
def SearchByAct(Actor):
  DatosSA = (Actor,)
  Query  = "SELECT * FROM Peliculas p JOIN Actores_Peliculas ac ON p.Codigo = ac.Codigo_Pelicula JOIN Actores a ON a.Codigo = ac.Codigo_Actor and a.Nombre = %s"
  cursor.execute(Query, DatosSA)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Duracion: ", row[4])
    print("----------------------------------\n")
  connect_base.commit() 

#Query de Búsqueda#3: Directores
def SearchByDir(Director):
  DatosSD = (Director,)
  Query  = "SELECT * FROM Peliculas p JOIN Directores_Peliculas ap ON p.Codigo = ap.Codigo_Pelicula JOIN Directores a ON a.Codigo = ap.Codigo_Director AND a.Nombre = %s"
  cursor.execute(Query, DatosSD)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Duracion: ", row[4])
    print("----------------------------------\n")
  connect_base.commit() 
  
#Query de Búsqueda#4: Género
def SearchByGen(Genero):
  DatosSG = (Genero,)
  Query  = "SELECT * FROM Peliculas WHERE Genero LIKE %s"
  cursor.execute(Query, DatosSG)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Duracion: ", row[4])
    print("----------------------------------\n")
  connect_base.commit() 

#Query de Búsqueda#5: Premios
def SearchByPrem(Reco):
  DatosSP = (Reco,)
  Query  = "SELECT * FROM Peliculas p JOIN Premiaciones p2 ON p2.Codigo_pelicula = p.Codigo AND p2.Reconocimiento = %s"
  cursor.execute(Query, DatosSP)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Duracion: ", row[4])
    print("----------------------------------\n")
  connect_base.commit() 
  
#Query de Búsqueda#6: Fecha
def SearchByYear(Year):
  DatosSY = (Year,)
  Query = "SELECT * FROM Peliculas WHERE YearP = %s"
  cursor.execute(Query, DatosSY)
  Peliculas = cursor.fetchall()
  print("\n")
  for row in Peliculas:
    print("----------------------------------")
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Año: ", row[3])
    print("Duracion: ", row[4])
    print("----------------------------------\n")
  connect_base.commit()
  
#----------------------------------------------------------------------------------
#                               Opciones Administrador
#----------------------------------------------------------------------------------

def Conseguir_Data(entidad, offset):
  queryCD = f"SELECT * FROM {entidad} LIMIT 10 OFFSET {offset}"
  cursor.execute(queryCD)
  data = cursor.fetchall()
  for x in data:
    print(x)
  connect_base.commit()

def Gen_code(entidad):
  queryGC = f"SELECT COUNT(*) FROM {entidad}"
  cursor.execute(queryGC)
  data = cursor.fetchone()
  connect_base.commit()
  return data

def Modificar_Pelicula(columna, nuevo_dato, id):
  queryMP = f"UPDATE peliculas SET {columna} = {repr(nuevo_dato)} WHERE codigo = {repr(id)}"
  cursor.execute(queryMP)
  connect_base.commit()
  
def Mod_CorreoU (nuevo_c, ant_c):
  DatosMU = (nuevo_c, ant_c,)
  queryMU = "UPDATE cuenta SET correo = %s WHERE correo = %s"
  cursor.execute(queryMU, DatosMU)
  connect_base.commit()

def Mod_Anuncios(columna, nuevo_dato, id):
  queryMA = f"UPDATE anuncios SET {columna} = {repr(nuevo_dato)} WHERE codigo = {repr(id)}"
  cursor.execute(queryMA)
  connect_base.commit()
  
def Mod_Anunciantes(columna, nuevo_dato, id):
  queryMA = f"UPDATE anunciantes SET {columna} = {repr(nuevo_dato)} WHERE codigo = {repr(id)}"
  cursor.execute(queryMA)
  connect_base.commit()
  
def Mod_ActoresN(columna, nuevo_dato, id):
  queryMA = f"UPDATE actores SET {columna} = {repr(nuevo_dato)} WHERE codigo = {repr(id)}"
  cursor.execute(queryMA)
  connect_base.commit()
  
def Mod_DirectoresN(columna, nuevo_dato, id):
  queryMA = f"UPDATE directores SET {columna} = {repr(nuevo_dato)} WHERE codigo = {repr(id)}"
  cursor.execute(queryMA)
  connect_base.commit()

def Mod_Usuarios(nueva_sus, correo):
  DatosMU = (nueva_sus, correo,)
  queryMU = "UPDATE cuenta SET Tipo = %s WHERE correo = %s"
  cursor.execute(queryMU, DatosMU)
  connect_base.commit()
  
def Mod_perfil(nueva_sus, cod_per, correo):
  DatosMU = (nueva_sus, cod_per, correo,)
  queryMU = """
  UPDATE perfiles SET nombre_perfil = %s 
    FROM (perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo)
  WHERE perfiles.codigo = %s AND cp.correo_cuenta = %s
  """
  cursor.execute(queryMU, DatosMU)
  connect_base.commit()
  
def Mod_active(isActive, perfil):
  DatosMU = (isActive, perfil,)
  queryMU = "UPDATE perfiles SET activo = %s WHERE nombre_perfil = %s"
  cursor.execute(queryMU, DatosMU)
  connect_base.commit()

def Mod_premiaciones(columna, nuevo_dato, codigo_peli, col1, val1, col2, val2):
  DatosMP = (columna, nuevo_dato, codigo_peli, col1, val1, col2, val2)
  queryMP = "UPDATE premiaciones SET %s = %s WHERE codigo_pelicula = %s and %s = %s and %s = %s"
  cursor.execute(queryMP, DatosMP)
  connect_base.commit()

def Mod_premiaciones_prem(nuevo_dato, codigo_peli, fecha, reconocimiento):
  DatosMP = (nuevo_dato, codigo_peli, fecha, reconocimiento)
  queryMP = "UPDATE premiaciones SET premiacion = %s WHERE codigo_pelicula = %s and fecha = %s and reconocimiento = %s"
  cursor.execute(queryMP, DatosMP)
  connect_base.commit()

def Mod_premiaciones_rec(nuevo_dato, codigo_peli, premiacion, fecha):
  DatosMP = (nuevo_dato, codigo_peli, premiacion, fecha)
  queryMP = "UPDATE premiaciones SET reconocimiento = %s WHERE codigo_pelicula = %s and premiacion = %s and fecha = %s"
  cursor.execute(queryMP, DatosMP)
  connect_base.commit()

def Mod_premiaciones_fecha(nuevo_dato, codigo_peli, premiacion, reconocimiento):
  DatosMP = (nuevo_dato, codigo_peli, premiacion, reconocimiento)
  queryMP = "UPDATE premiaciones SET fecha = %s WHERE codigo_pelicula = %s and premiacion = %s and reconocimiento = %s"
  cursor.execute(queryMP, DatosMP)
  connect_base.commit()

def Delete_Pelicula(id):
  DatosDP = (id,)
  queryDP = "DELETE FROM Peliculas WHERE codigo = %s"
  cursor.execute(queryDP, DatosDP)
  connect_base.commit()

def Delete_Anuncio(id):
  DatoDA = (id,)
  queryDA = "DELETE FROM Anuncios WHERE codigo = %s"
  cursor.execute(queryDA, DatoDA)
  connect_base.commit()
  
def Delete_Anunciante(id):
  DatoDA = (id,)
  queryDA = "DELETE FROM Anunciantes WHERE codigo = %s"
  cursor.execute(queryDA, DatoDA)
  connect_base.commit()

def Delete_Premiacion(peli, premiacion, reconocimiento, fecha):
  DatoDP = (peli, premiacion, reconocimiento, fecha)
  queryDP = " DELETE FROM premiaciones WHERE codigo_pelicula = %s and premiacion = %s and reconocimiento = %s and fecha = %s"
  cursor.execute(queryDP, DatoDP)
  connect_base.commit()

def Desactivar_Usuarios(nuevoEstado, correo):
  DatoDU = (nuevoEstado, correo,)
  queryDU = "UPDATE cuenta SET estado = %s where correo = %s"
  cursor.execute(queryDU,DatoDU)
  connect_base.commit()

def Get_Sub(correo):
  DatoGS = (correo,)
  queryGS = "Select * from Cuenta where correo = %s"
  cursor.execute(queryGS, DatoGS)
  cuenta = cursor.fetchone()
  connect_base.commit()
  if cuenta == None:
    return cuenta
  else: 
    return cuenta['tipo']
  
def Get_Cuenta(correo):
  DatoGS = (correo,)
  queryGS = "Select * from Cuenta where correo = %s"
  cursor.execute(queryGS, DatoGS)
  cuenta = cursor.fetchone()
  connect_base.commit()
  return cuenta

def EndSesion(PerfilActual):
  Datos = (PerfilActual, )
  query = "UPDATE Perfiles SET activo = FALSE WHERE Nombre_Perfil = %s"
  cursor.execute(query, Datos)
  connect_base.commit()

def UpdateIntentos(contadorN, fecha, correo):
  Datos = (contadorN, fecha, correo,)
  queryGS = "UPDATE intentos SET cantidadintentos = %s, fecha = %s WHERE correo_cuenta = %s"
  cursor.execute(queryGS, Datos)
  connect_base.commit()

def getContador(correo):
  DatoGS = (correo,)
  queryGS = "Select * from intentos where correo_cuenta = %s"
  cursor.execute(queryGS, DatoGS)
  cuenta = cursor.fetchone()
  connect_base.commit()
  if(cuenta == None):
    return cuenta
  else:
    return cuenta['cantidadintentos']

def Get_Estado(correo):
  DatoGE = (correo,)
  queryGE = "Select * from Cuenta where correo = %s"
  cursor.execute(queryGE, DatoGE)
  cuenta = cursor.fetchone()
  connect_base.commit()
  if cuenta == None:
    return cuenta
  else: 
    return cuenta[3]

def Get_Director(dato):
  DatoGD = (dato,)
  queryGD = "Select * from Directores WHERE nombre = %s"
  cursor.execute(queryGD, DatoGD)
  Director = cursor.fetchone()
  connect_base.commit()
  return Director

def Get_Correos(entidad, offset):
  queryCD = f"SELECT correo FROM {entidad} LIMIT 10 OFFSET {offset}"
  cursor.execute(queryCD)
  data = cursor.fetchall()
  for x in data:
    print(x)
  connect_base.commit()  

def Get_Director2(dato):
  DatoGD = (dato,)
  queryGD = "Select * from Directores WHERE codigo = %s"
  cursor.execute(queryGD, DatoGD)
  Director = cursor.fetchone()
  connect_base.commit()
  return Director

def Get_Actor(dato):
  DatoGA = (dato,)
  queryGA = "Select * from Actores WHERE nombre = %s"
  cursor.execute(queryGA, DatoGA)
  Actor = cursor.fetchone()
  connect_base.commit()
  return Actor

def Get_Actor2(dato):
  DatoGA = (dato,)
  queryGA = "Select * from Actores WHERE codigo = %s"
  cursor.execute(queryGA, DatoGA)
  Actor = cursor.fetchone()
  connect_base.commit()
  return Actor

def Get_Anunciante(dato):
  DatoGD = (dato,)
  queryGD = "Select * from Anunciantes WHERE codigo = %s"
  cursor.execute(queryGD, DatoGD)
  Anunciante = cursor.fetchone()
  connect_base.commit()
  return Anunciante

def Get_Movie(codigo):
  Dato = (codigo,)
  query = "SELECT * FROM Peliculas WHERE codigo = %s"
  cursor.execute(query,Dato)
  Peli = cursor.fetchone()
  connect_base.commit()
  return Peli

def Get_Anuncio(codigo):
  Dato = (codigo,)
  query = "SELECT * FROM anuncios WHERE codigo = %s"
  cursor.execute(query,Dato)
  Anun = cursor.fetchone()
  connect_base.commit()
  return Anun

def Get_Genero(codigo):
  Dato = (codigo,)
  query = "SELECT * FROM Peliculas WHERE genero = %s"
  cursor.execute(query,Dato)
  Peli = cursor.fetchone()
  connect_base.commit()
  return Peli

def Get_Premio(codigo):
  Dato = (codigo,)
  query = "SELECT * FROM Peliculas pl JOIN premiaciones p ON pl.codigo = p.codigo_pelicula AND p.reconocimiento = %s"
  cursor.execute(query,Dato)
  Peli = cursor.fetchone()
  connect_base.commit()
  return Peli

def Get_Year(codigo):
  Dato = (codigo,)
  query = "SELECT * FROM Peliculas WHERE yearp = %s"
  cursor.execute(query,Dato)
  Peli = cursor.fetchone()
  connect_base.commit()
  return Peli

def Get_Name(codigo):
  Dato = (codigo,)
  query = "SELECT * FROM Peliculas WHERE titulo = %s"
  cursor.execute(query,Dato)
  Peli = cursor.fetchone()
  connect_base.commit()
  return Peli

def Get_Perfiles(correo):
  Dato = (correo,)
  query = "SELECT COUNT(*) FROM cuenta_perfiles WHERE correo_cuenta = %s"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  if data == None:
    return data
  else: 
    return data[0] 

def Get_PerfilIn(correo):
  Dato = (correo,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s WHERE p.numerop = 1"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  if data == None:
    return data
  else:
    return data['nombre_perfil']
  
def Get_PerfilActive(correo, PerfilActual):
  Dato = (correo, PerfilActual,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s WHERE p.Nombre_Perfil = %s"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  if data == None:
    return data
  else:
    return data['activo']

def Get_PerfilesInfo(correo):
  Dato = (correo,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s AND p.estado = 'TRUE'"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  for row in data:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("No. Perfil: ", row[1])
    print("Nombre Perfil: ", row[2])
    print("----------------------------------")
  connect_base.commit()
  
def Get_PerfilesInfo2(correo):
  Dato = (correo,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  for row in data:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Nombre Perfil: ", row[2])
    print("----------------------------------")
  connect_base.commit()
  
def Get_PerfilCode(correo, cod):
  Dato = (correo, cod,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s WHERE p.codigo = %s AND p.estado = 'TRUE'"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  if data == None:
    return data
  else:
    return data['nombre_perfil']
  
def Get_PeliTime(cod):
  Dato = (cod,)
  query = "SELECT * FROM peliculas p WHERE p.codigo = %s"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  if data == None:
    return data
  else:
    return data['duracion']
  
def Get_PerfilCode2(correo, cod):
  Dato = (correo, cod,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s WHERE p.numerop = %s AND p.estado = 'TRUE'"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  if data == None:
    return data
  else:
    return data['nombre_perfil']
  
def Get_PerfilCode3(correo, cod):
  Dato = (correo, cod,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s WHERE p.codigo = %s"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  return data

def Get_perfilesName(correo, Nombre):
  Dato = (correo, Nombre,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo AND correo_cuenta = %s WHERE p.nombre_perfil = %s AND p.estado = 'TRUE'"
  cursor.execute(query, Dato)
  data = cursor.fetchone()
  connect_base.commit()
  return data

def Get_AllPerfiles():
  query = "SELECT codigo FROM perfiles"
  cursor.execute(query)
  data = cursor.fetchall()
  perfiles = []
  for row in data:
    perfiles.append(row[0])
  connect_base.commit()
  return perfiles

def Get_AllMovies():
  query = "SELECT codigo FROM peliculas"
  cursor.execute(query)
  data = cursor.fetchall()
  peliculas = []
  for row in data:
    peliculas.append(row[0])
  connect_base.commit()
  return peliculas

def mostrarfavoritos(perfil):
  Dato = (perfil,)
  query = "select fp.codigo_pelicula,  p.titulo, p.genero from favoritos_perfil fp join peliculas p on fp.codigo_pelicula = p.codigo where fp.codigo_perfil = %s group by fp.codigo_pelicula,  p.titulo, p.genero"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  for row in data:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("----------------------------------\n")
  connect_base.commit()

def mostrarviendo(perfil):
  Dato = (perfil,)
  query = "select fp.codigo_pelicula,  p.titulo, p.genero, round(avg(fp.minconsumidos))  from contenido_perfil fp join peliculas p on fp.codigo_pelicula = p.codigo where fp.codigo_perfil = %s and fp.concluida is not true group by fp.codigo_pelicula,  p.titulo, p.genero"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  for row in data:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("Minutos vistos promedio: ", row[3])
    print("----------------------------------\n")
  connect_base.commit()

def mostrarvistos(perfil):
  Dato = (perfil,)
  query = "select p.codigo ,p.titulo, p.genero  from perfil_reproducciones pr join peliculas p ON pr.codigo_pelicula = p.codigo where pr.codigo_perfil = %s group by  p.codigo ,p.titulo, p.genero"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  for row in data:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("----------------------------------\n")
  connect_base.commit()

def ContenidoFinalizadoRegistros (CP, CA):
  DatoDU = (CP, CA,)
  queryDU = "UPDATE contenido_perfil SET concluida = 'true' WHERE codigo_perfil = %s and codigo_pelicula = %s"
  cursor.execute(queryDU,DatoDU)
  connect_base.commit()

def Get_CodigoPerfil(correo, perfil):
  Dato = (correo,perfil,)
  query = "SELECT * FROM perfiles p JOIN cuenta_perfiles cp ON cp.codigo_perfil = p.codigo WHERE correo_cuenta = %s and p.nombre_perfil = %s AND p.estado = 'TRUE'"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  codigo_perfil = ""
  for row in data:
    codigo_perfil = row[0]
  connect_base.commit()
  return codigo_perfil

def DesPerfil(numerop, correo):
  Dato = (numerop, correo,)
  query = "UPDATE perfiles p SET estado = 'FALSE' FROM cuenta_perfiles cp WHERE cp.codigo_perfil = p.codigo AND p.numerop = %s AND correo_cuenta = %s"
  cursor.execute(query, Dato) 
  connect_base.commit()
  
def ActPerfil(correo):
  Dato = (correo,)
  query = "UPDATE perfiles p SET estado = 'TRUE' FROM cuenta_perfiles cp WHERE cp.codigo_perfil = p.codigo AND correo_cuenta = %s"
  cursor.execute(query, Dato) 
  connect_base.commit()

def genero_perfil(codigoP, cantidad):
  Dato = (codigoP,cantidad,)
  query = "select A.genero from (select p.genero, count(*)  from perfil_reproducciones pr join peliculas p on p.codigo = pr.codigo_pelicula where pr.codigo_perfil = %s group by p.genero order by count(*) desc limit 1 offset %s) A;"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  genero = ""
  for row in data:
    genero = row[0]
  connect_base.commit()
  return genero

def pelicula_recomendacion(genero,perfil):
  Dato = (genero, perfil,)
  query = "select * from peliculas p where p.genero = %s and p.codigo not in (select pr.codigo_pelicula from perfil_reproducciones pr where pr.codigo_perfil = %s) limit 1;"
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  genero = ""
  for row in data:
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Titulo: ", row[1])
    print("Genero: ", row[2])
    print("----------------------------------\n")
  connect_base.commit()
  return genero

def anuncios_tiempo(pelicula):
  Datos = (pelicula,)
  Query = "SELECT * FROM peliculas WHERE (codigo = %s)"
  cursor.execute(Query, Datos)
  contenido = cursor.fetchone()
  connect_base.commit()
  if contenido == None:
    return contenido
  else:
    return contenido['duracion']

def anuncio_random(temp, Correo):
  numoer = random.randint(0, Gen_code('anuncios')[0]-1)
  if temp == numoer and numoer != Gen_code('anuncios')[0]-1:
    numoer = numoer + 1
  elif temp == numoer and numoer == Gen_code('anuncios')[0]-1:
    numoer = numoer - 1
  print(numoer)
  codigo = "anu["+str(numoer)+"]"
  Datos = (codigo,)
  Query = "SELECT * FROM anuncios WHERE (codigo = %s)"
  cursor.execute(Query, Datos)
  Peliculas = cursor.fetchall()
  print("\n")
  link = ''
  for row in Peliculas:
    link = row[4]
    print("----------------------------------")
    print("Codigo: ", row[0])
    print("Contenido Promocional: ", row[3])
    print("Link: ", row[4])
    Upload_Rep_Anuncios(row[0], Correo)
    print("----------------------------------\n")
  connect_base.commit()
  return [numoer, link]

def Conseguir_Data_2(entidad, offset):
  queryCD = f"SELECT * FROM {entidad} LIMIT 10 OFFSET {offset}"
  cursor.execute(queryCD)
  data = cursor.fetchall()
  for x in data:
    print("\nCodigo: ", x[0])
    print("Titulo: ", x[1])
  connect_base.commit()

def comprobar_pelicula(codigo):
  Datos = (codigo,)
  Query = "SELECT * FROM peliculas WHERE (codigo = %s)"
  cursor.execute(Query, Datos)
  contenido = cursor.fetchone()
  connect_base.commit()
  if contenido == None:
    return contenido
  else:
    return contenido['link']

def TopDir():
  Query = """SELECT COUNT(d.nombre), d.nombre
  FROM perfil_reproducciones pr
  JOIN cuenta_perfiles cp ON cp.codigo_perfil = pr.codigo_perfil
  JOIN cuenta c ON c.correo = cp.correo_cuenta AND c.tipo = 'Estandar' OR c.tipo = 'Avanzada'
  JOIN peliculas p ON p.codigo = pr.codigo_pelicula
  JOIN directores_peliculas dp ON dp.codigo_pelicula = p.codigo
  JOIN directores d ON d.codigo = dp.codigo_director
  GROUP BY d.nombre
  ORDER BY COUNT(d.nombre) DESC
  LIMIT 10"""
  cursor.execute(Query)
  contenido = cursor.fetchall()
  for row in contenido:
    print("Director:", row[1], " con ", row[0], " apariciones")
  connect_base.commit()
  
def TopAct():
  Query = """SELECT COUNT(a.nombre), a.NOMBRE
  FROM perfil_reproducciones pr
  JOIN cuenta_perfiles cp ON cp.codigo_perfil = pr.codigo_perfil
  JOIN cuenta c ON c.correo = cp.correo_cuenta AND c.tipo = 'Estandar' OR c.tipo = 'Avanzada'
  JOIN peliculas p ON p.codigo = pr.codigo_pelicula
  JOIN actores_peliculas ap ON ap.codigo_pelicula = p.codigo
  JOIN actores a ON a.codigo = ap.codigo_actor
  GROUP BY a.nombre
  ORDER BY COUNT(a.nombre) DESC
  LIMIT 10"""
  cursor.execute(Query)
  contenido = cursor.fetchall()
  for row in contenido:
    print("Actor:", row[1], " con ", row[0], " apariciones")
  connect_base.commit()
  
def GetCantReprGratis(FechaInicial, FechaFinal):
  Datos = (FechaInicial, FechaFinal, FechaInicial, FechaFinal,)
  Query = """SELECT A.generos, COUNT(A.generos) AS Cant_reproducciones
  FROM (
    SELECT p.genero AS generos
          FROM contenido_perfil cp 
              JOIN peliculas p ON cp.codigo_pelicula = p.codigo
              JOIN cuenta_perfiles cpe ON cpe.codigo_perfil = cp.codigo_perfil
              JOIN cuenta c ON c.correo = cpe.correo_cuenta AND c.tipo = 'Gratis'
          WHERE cp.concluida IS NOT TRUE AND cp.vistaf >= %s AND cp.vistaf <= %s     
      UNION ALL
      SELECT p.genero AS generos
          FROM perfil_reproducciones pr 
              JOIN peliculas p ON pr.codigo_pelicula = p.codigo
              JOIN cuenta_perfiles cpe ON cpe.codigo_perfil = pr.codigo_perfil
              JOIN cuenta c ON c.correo = cpe.correo_cuenta AND c.tipo = 'Gratis'
          WHERE pr.vistaf >= %s AND pr.vistaf <= %s
  ) A
  GROUP BY A.generos
  ORDER BY COUNT(A.generos) DESC"""
  cursor.execute(Query, Datos)
  contenido = cursor.fetchall()
  print("\n------------ Tipo de cuenta: Gratis ------------")
  if(contenido == None or contenido == []):
    print("No hay registros de este tipo de cuenta actualmente")
  else:
    for row in contenido:
      print("Genero:", row[0], " con ", row[1], " de reproducciones")
    connect_base.commit()
  
def GetCantReprEst(FechaInicial, FechaFinal):
  Datos2 = (FechaInicial, FechaFinal, FechaInicial, FechaFinal,)
  Query2 = """SELECT A.generos, COUNT(A.generos) AS Cant_reproducciones
  FROM (
    SELECT p.genero AS generos
          FROM contenido_perfil cp 
              JOIN peliculas p ON cp.codigo_pelicula = p.codigo
              JOIN cuenta_perfiles cpe ON cpe.codigo_perfil = cp.codigo_perfil
              JOIN cuenta c ON c.correo = cpe.correo_cuenta AND c.tipo = 'Estandar'
          WHERE cp.concluida IS NOT TRUE AND cp.vistaf >= %s AND cp.vistaf <= %s     
      UNION ALL
      SELECT p.genero AS generos
          FROM perfil_reproducciones pr 
              JOIN peliculas p ON pr.codigo_pelicula = p.codigo
              JOIN cuenta_perfiles cpe ON cpe.codigo_perfil = pr.codigo_perfil
              JOIN cuenta c ON c.correo = cpe.correo_cuenta AND c.tipo = 'Estandar'
          WHERE pr.vistaf >= %s AND pr.vistaf <= %s
  ) A
  GROUP BY A.generos
  ORDER BY COUNT(A.generos) DESC"""
  cursor.execute(Query2, Datos2)
  contenido2 = cursor.fetchall()
  print("\n------------ Tipo de cuenta: Estandar ------------")
  if(contenido2 == None or contenido2 == []):
    print("No hay registros de este tipo de cuenta actualmente")
  else:
    for row in contenido2:
      print("Genero:", row[0], " con ", row[1], " de reproducciones")
    connect_base.commit()
  
def GetCantReprAva(FechaInicial, FechaFinal):
  Datos3 = (FechaInicial, FechaFinal, FechaInicial, FechaFinal,)
  Query3 = """SELECT A.generos, COUNT(A.generos) AS Cant_reproducciones
  FROM (
    SELECT p.genero AS generos
          FROM contenido_perfil cp 
              JOIN peliculas p ON cp.codigo_pelicula = p.codigo
              JOIN cuenta_perfiles cpe ON cpe.codigo_perfil = cp.codigo_perfil
              JOIN cuenta c ON c.correo = cpe.correo_cuenta AND c.tipo = 'Avanzada'
          WHERE cp.concluida IS NOT TRUE AND cp.vistaf >= %s AND cp.vistaf <= %s     
      UNION ALL
      SELECT p.genero AS generos
          FROM perfil_reproducciones pr 
              JOIN peliculas p ON pr.codigo_pelicula = p.codigo
              JOIN cuenta_perfiles cpe ON cpe.codigo_perfil = pr.codigo_perfil
              JOIN cuenta c ON c.correo = cpe.correo_cuenta AND c.tipo = 'Avanzada'
          WHERE pr.vistaf >= %s AND pr.vistaf <= %s
  ) A
  GROUP BY A.generos
  ORDER BY COUNT(A.generos) DESC"""
  cursor.execute(Query3, Datos3)
  contenido3 = cursor.fetchall()
  print("\n------------ Tipo de cuenta: Avanzada ------------")
  if(contenido3 == None or contenido3 == []):
    print("No hay registros de este tipo de cuenta actualmente")
  else:
    for row in contenido3:
      print("Genero:", row[0], " con ", row[1], " de reproducciones")
    connect_base.commit()
    
def query_reporte_1(A,B,C,D):

  Dato = (A, B,C,D,)
  query = """select generos, sum(minutos_consumidos) as minutos_consumidos from (
    select p.genero as generos, cp.minconsumidos as minutos_consumidos
      from contenido_perfil cp 
        join peliculas p ON cp.codigo_pelicula = p.codigo
      where cp.concluida is not true and cp.vistaf >= %s and cp.vistaf <= %s
    union all
    select p.genero, p.duracion as minutos_consumidos
      from perfil_reproducciones pr 
        join peliculas p on pr.codigo_pelicula = p.codigo
      where pr.vistaf >= %s and pr.vistaf <= %s
  ) A
    group by generos
    order by minutos_consumidos desc
    limit 10
  """
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  genero = ""
  for row in data:
    print("----------------------------------")
    print("Genero: ", row[0])
    print("Minutos Consumidos: ", row[1])
    print("----------------------------------\n")
  connect_base.commit()

  return genero

def query_reporte_4():
  query = """select count(*) from cuenta c where c.ingresof > (current_date - interval '6 months') and c.tipo = 'Avanzada';"""
  cursor.execute(query)
  data = cursor.fetchall()
  genero = ""
  print(f"Cuentas avanzadas creadas en los ultimos 6 meses:")
  for row in data:
    print("----------------------------------")
    print("Cantidad: ", row[0])
    print("----------------------------------\n")
  connect_base.commit()
  return genero

def query_reporte_5(A):
  Dato = (A,)
  query = """select avg(hora)::interval(2)  from (select c.ingresoh as hora, c.ingresof as fecha from cuenta c
  union all
  select cp.vistah as hora, cp.vistaf as fecha from contenido_perfil cp
  union all
  select fp.vistah as hora, fp.vistaf as fecha from favoritos_perfil fp
  union all 
  select pr.vistah as hora, pr.vistaf as fecha from perfil_reproducciones pr
  ) A where fecha = %s;
  """
  cursor.execute(query, Dato)
  data = cursor.fetchall()
  genero = ""
  print(f"Fecha: {A}")
  for row in data:
    #print(row)
    if row == None or row == [None]:
      print("------------------------------------------")
      print("Hora pico: Sin registro para esta fecha")
      print("-----------------------------------------\n")
    else:
      print("----------------------------------")
      print("Hora pico: ", row[0])
      print("----------------------------------\n")
  connect_base.commit()
  return genero

def query_reporte_6():
  Dato = ()
  query = """select r.correo_cuenta, a.codigo, a.link, count(*) as repeticiones
    from repanuncios r
        join anuncios a on a.codigo = r.codigo_a
    group by r.correo_cuenta, a.codigo, a.link;
  """
  cursor.execute(query)
  data = cursor.fetchall()
  genero = ""
  for row in data:
    print("----------------------------------")
    print("Correo:         ", row[0])
    print("Codigo anuncio: ", row[1])
    print("Link:           ", row[2])
    print("Repeticions:    ", row[3])
    print("----------------------------------\n")
  connect_base.commit()
  return genero
