'''
  Universidad del Valle de Guatemala
  Bases de datos 1
  Proyecto 2

  Integrantes:
    - Gabriel Vicente 20498
    - Maria Isabel Solano 20504
    - Christopher García 20541
'''

#Libreria que permite determinar si strings coinciden con un patrón o sintaxis determinada
import datetime
import re
#Librería para encriptar contraseñas
import hashlib
#Librería para ocultar password
from getpass import getpass
#Otros documentos
from ConnectionBD import *
#Import tiempos
import time
import sys
import webbrowser

#Diversidad de funciones utilizadas como programación defensiva y otras funciones del apartado de usuario

def recomendaciones(perfil):
  pelicula_recomendacion(genero_perfil(perfil, 0), perfil)
  pelicula_recomendacion(genero_perfil(perfil, 1), perfil)
  pelicula_recomendacion(genero_perfil(perfil, 2), perfil)
  return 2

def anuncios_cantidad(tiempo):
  total_anuncios = round(tiempo/15)
  print(total_anuncios)
  return total_anuncios

def anuncios_mostrar(cantidad, tiempo, Correo):
  temp = 0 
  tiempo_transcurrido = 0
  for x in range(cantidad):
    tiempo_transcurrido = tiempo_transcurrido + 15
    if tiempo_transcurrido < tiempo:
      print("Anuncio mostrado al minuto...", tiempo_transcurrido)
    else:
      print("Anuncio mostrado al minuto...", tiempo)
    anuncio = anuncio_random(temp, Correo)
    temp, abrir = anuncio[0], anuncio[1]
    open_link(abrir)

def open_link(link):
  webbrowser.open(link)

def GenerarCodigo2(entidad):
  #Obtener data de la base de datos
  cant = Gen_code(entidad)
  codigo = str(entidad)[0:3] + str(cant)
  return codigo
  
def obtenerData2(entidad, offset):
  #Realizar query
  Conseguir_Data(entidad, offset)
  data = ''#Ingresar lista con toda la información
  return data

def escritura_lenta(frase):
  print()
  for i in frase:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)

#Programación defensiva para la solicitud de opciones
def SolicitudNum():
  Verificador = False
  num = 0
  while not Verificador:
    try:
      num = int(input("Opcion: "))
      Verificador = True
    except ValueError:
      escritura_lenta("Error, ingrese opcion valida\n")
  return num

def SolicitudNum2():
  Verificador = False
  num = 0
  while not Verificador:
    try:
      num = int(input("Opción: "))
      Verificador = True
    except ValueError:
      escritura_lenta("Error, ingrese opcion valida")
  return num

#Se valida si es un correo válido
def Correo_Validacion(correo):
  correo = correo.lower()
  Sintaxis = r"(?:[a-z0-9!#$%&*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&*+/=?^_{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
  return re.match(Sintaxis, correo) is not None

#Se crea la cuenta y se utiliza programación defensiva
def CrearCuenta ():
  Verificador = False
  Verificador2 = False
  Verificador3 = False
  Correo = ""
  Contra = ""
  while not Verificador:
    try:
      while not Verificador2:
        Correo = input("Correo: ")
        if (Correo_Validacion(Correo) and Get_Cuenta(Correo) == None):
          Verificador2 = True
        elif (Get_Cuenta(Correo) != None):
          print("\nLo sentimos, este correo ya está en uso. Pruebe con otro\n")
        else:
          escritura_lenta("Lo siento, correo invalido\n")

      #Encriptación de la contraseña
      Contra = getpass('Contrasena:')
      #print(Contra)
      md5_hash = hashlib.md5()
      md5_hash.update(Contra.encode())
      #print(md5_hash.hexdigest())

      Contra = md5_hash.hexdigest()

      escritura_lenta("\n\t\t\t\tTipos de cuenta: \n")
      escritura_lenta("1) Gratis (Maximo 1 perfil)")
      escritura_lenta("2) Estandar (Maximo 4 perfiles)")
      escritura_lenta("3) Avanzada (Maximo 8 perfiles)\n")

      opcion = 0
      TipoCuenta = ""
      
      while not Verificador3:
        opcion = SolicitudNum()
        if (opcion == 1):
          TipoCuenta = "Gratis"
          Verificador3 = True
        elif (opcion == 2):
          TipoCuenta = "Estandar"
          Verificador3 = True
        elif (opcion == 3):
          TipoCuenta = "Avanzada"
          Verificador3 = True
        else:
          escritura_lenta("Opcion invalida\n")
      
      Verificador = True
      
    except ValueError:
      escritura_lenta("Lo sentimos, ingreso de datos invalido\n")
    
  return (Correo, Contra, TipoCuenta)

def LoginCuenta():
  Verificador2 = False
  while not Verificador2:
    Correo = input("Correo: ")
    if (Correo_Validacion(Correo)):
      Verificador2 = True
    else:
      escritura_lenta("Lo siento, correo invalido\n")
  Contra = getpass('Contrasena:')
  md5_hash = hashlib.md5()
  md5_hash.update(Contra.encode())
  Contra = md5_hash.hexdigest()
  return (Correo, Contra)

def Check_Date(fecha):
  date = False
  try:
    datetime.datetime.strptime(fecha, '%Y-%m-%d')
    date = fecha
  except:
    print('Formato Incorrecto\n')
  return date

def SearchP():
  Verificador = True
  while (Verificador):
    try:
      print("\n...........Búsqueda personalizada...........")
      print("Seleccione una de las siguientes opciones: ")
      print('__________________________________________________________')
      print("\n1) Busqueda por actor")
      print("2) Busqueda por director")
      print("3) Busqueda por genero")
      print("4) Busqueda por premios ganados")
      print("5) Busqueda por fecha de estreno (año)")
      print("6) Busqueda por nombre")
      print("7) Cancelar búsqueda y salir\n")
      
      op1 = int(input("Opcion: "))
      
      if (op1 == 1):
        verificar_actor = True
        while (verificar_actor):
          actor = input('Nombre del actor: ')
          existencia = Get_Actor(actor)
          if (existencia):
            SearchByAct(actor)
            verificar_actor = False
          else:
            print("Lo sentimos, el actor no existe en la base de datos")
      
      elif (op1 == 2):
        verificar_director = True
        while (verificar_director):
          director = input('Nombre del director: ')
          existencia = Get_Director(director)
          if (existencia):
            SearchByDir(director)
            verificar_director = False
          else:
            print("Lo sentimos, el director no existe en la base de datos")    
      
      elif (op1 == 3):
        verificar_genero = True
        while(verificar_genero):
          genero = input('Genero: ')
          existencia = Get_Genero(genero)
          if (existencia):
            SearchByGen(genero)
            verificar_genero = False
          else:
            print("Lo sentimos, el genero no existe en la base de datos")
        
      elif (op1 == 4):
        verificar_premios = True
        while (verificar_premios):
          premio = input('Nombre del reconocimiento: ')
          existencia = Get_Premio(premio)
          if (existencia):
            SearchByPrem(premio)
            verificar_premios = False
          else:
            print("Lo sentimos, el reconocimiento no existe en la base de datos")   
                
      elif (op1 == 5):
        verificar_year = True
        while (verificar_year):
          try:
            yearp = int(input('Año de estreno: '))
            existencia = Get_Year(yearp)
            if (existencia):
              SearchByYear(yearp)  
              verificar_year = False
            else:
              print("Lo sentimos, no existe registro para este año en la base de datos")
          except:
            print("Ingreso de datos inválido")
        
      elif (op1 == 6):
        verificar_nombre = True
        while (verificar_nombre):
          nombre = input('Nombre de la película: ')
          existencia = Get_Name(nombre)
          if (existencia):
            SearchByName(nombre)
            verificar_nombre = False
          else:
            print("Lo sentimos, la película no existe en la base de datos") 
      
      elif (op1 == 7):
        Verificador = False
      else:
        print("Opción inválida")     
      
    except:
      print("Ingreso de datos inválidos")

def ManejoPerfiles(correo):
  permanecer = True
  while (permanecer):
    escritura_lenta('La suscripción actual de '+correo+ ' es ' + Get_Sub(correo)+"\n")
    if (Get_Sub(correo) == "Gratis"):
      print("Con esta suscripción tienes derecho a máximo 1 perfil (perfil actual)\n")
      cant = Get_Perfiles(correo)
      if (cant == 4):
        print("Hemos detectado un downgrade al tipo de tu cuenta (De estandar a gratis)")
        print("El unico perfil que podrá utilizar será: " + Get_PerfilIn(correo))
        DesPerfil(2, correo)
        DesPerfil(3, correo)
        DesPerfil(4, correo)
        permanecer = False
      elif (cant == 8):
        print("Hemos detectado un downgrade al tipo de tu cuenta (De avanzada a gratis)")
        print("El unico perfil que podrá utilizar será: " + Get_PerfilIn(correo))
        DesPerfil(2, correo)
        DesPerfil(3, correo)
        DesPerfil(4, correo)
        DesPerfil(5, correo)
        DesPerfil(6, correo)
        DesPerfil(7, correo)
        DesPerfil(8, correo)
        permanecer = False
      else:
        permanecer = False
      
    elif (Get_Sub(correo) == "Estandar"):
      print("Con esta suscripción tienes derecho a máximo 4 perfiles (perfil actual y otros 3)\n")
      try:
        cant = Get_Perfiles(correo)
        if (cant == 8):
          print("Hemos detectado un downgrade al tipo de tu cuenta (De avanzada a estandar)")
          print("Los unicos perfiles que podrá utilizar serán: ")
          print("Perfil 1: "+Get_PerfilIn(correo))
          print("Perfil 2: "+Get_PerfilCode2(correo,2))
          print("Perfil 3: "+Get_PerfilCode2(correo,3))
          print("Perfil 4: "+Get_PerfilCode2(correo,4))
          DesPerfil(5, correo)
          DesPerfil(6, correo)
          DesPerfil(7, correo)
          DesPerfil(8, correo)
          permanecer = False
        else: 
          print("Esta cuenta posee "+str(4-cant)+ " perfil(es) disponible(s)")
          if (cant == 4):
            print("Has alcanzado el número máximo de perfiles")
            permanecer = False
          elif (cant > 4):
            print("Hemos detectado un downgrade al tipo de tu cuenta")
          else:
            print("Desea crear los demás perfiles ahorita? ")
            op = input('(y/n): ')
            if (op == 'y'):
              
              inicio = 0
              
              while (inicio != (4-cant)):
                cant2 = Get_Perfiles(correo)
                CodigoP = GenerarCodigo2('perfiles')
                Verifica = True
                while(Verifica):
                  Nombre = input("Nombre del nuevo perfil: ")
                  if(Get_perfilesName(correo, Nombre) == None):
                    Upload_Perfiles(CodigoP, cant2+1, Nombre, False)
                    Upload_CuentaPerfiles(correo, CodigoP)
                    inicio += 1
                    Verifica = False
                  else:
                    print("Lo siento, este nombre de perfil ya existe")
              
              permanecer = False
              
            elif (op == 'n'):
              permanecer = False
            else:
              print("Opcion invalida")
      except Exception as ex:
        print("Ingreso de datos inválido")
        
    elif (Get_Sub(correo) == "Avanzada"):
      print("Con esta suscripción tienes derecho a máximo 8 perfiles (perfil actual y otros 7)\n")
      try:
        cant = Get_Perfiles(correo)
        print("Esta cuenta posee "+str(8-cant)+ " perfil(es) disponible(s)")
        if (cant == 8):
          print("Has alcanzado el número máximo de perfiles")
          permanecer = False
        else:
          print("Desea crear los demás perfiles ahorita? ")
          op = input('(y/n): ')
          if (op == 'y'):
            
            inicio = 0
            
            while (inicio != (8-cant)):
              cant2 = Get_Perfiles(correo)
              CodigoP = GenerarCodigo2('perfiles')
              Verifica = True
              while(Verifica):
                Nombre = input("Nombre del nuevo perfil: ")
                if(Get_perfilesName(correo, Nombre) == None):
                  Upload_Perfiles(CodigoP, cant2+1, Nombre, False)
                  Upload_CuentaPerfiles(correo, CodigoP)
                  inicio += 1
                  Verifica = False
                else:
                  print("Lo siento, este nombre de perfil ya existe")
            
            permanecer = False
            
          elif (op == 'n'):
            permanecer = False
          else:
            print("Opcion invalida")
      except Exception as ex:
        print("Ingreso de datos inválido")

def CambioPerfiles(correo, perfilAc):
  
  perfilActual = ""
  
  print("\nEl perfil actual de "+correo+" es "+ perfilAc+"\n")
  print("Perfiles disponibles")
  Get_PerfilesInfo(correo)
  
  verif = True
  while verif:
    print("\nIngrese el codigo del perfil al que quiere cambiar\n")
    opper = input("Codigo: ")
    NombreCode = Get_PerfilCode(correo, opper)
    IsActive = Get_PerfilActive(correo, NombreCode)
    
    if(NombreCode != None and IsActive == False):
      Mod_active(False, perfilAc)
      perfilActual = NombreCode
      Mod_active(True, perfilActual)
      verif = False
    elif (IsActive == True):
      print("Lo sentimos, perfil en uso")
    else: 
      print("Lo sentimos perfil no encontrado o desactivado")
      perfilActual = perfilAc
  
  return perfilActual

def SeleccionPerfiles(correo):
  
  perfilActual = ""
  perfilAc = Get_PerfilIn(correo) 
  
  print("\nEl perfil inicial de "+correo+" es "+ perfilAc+"\n")
  print("Perfiles disponibles")
  Get_PerfilesInfo(correo)
  
  verif = True
  while verif:
    print("\nIngrese el codigo del perfil con el que quiere ingresar\n")
    opper = input("Codigo: ")
    NombreCode = Get_PerfilCode(correo, opper)
    IsActive = Get_PerfilActive(correo, NombreCode)
    
    if(NombreCode != None and IsActive == False):
      perfilActual = NombreCode
      verif = False
    elif (IsActive == True):
      print("Lo sentimos, perfil en uso")
    else: 
      print("Lo sentimos perfil no encontrado o desactivado")
      perfilActual = perfilAc
  
  return perfilActual
  
def SolicitudNum3(frase):
  Verificador = False
  num = 0
  while not Verificador:
    try:
      num = int(input(f"{frase} "))
      Verificador = True
    except ValueError:
      print("Error, ingrese opcion valida")
  return num

def Agregar_Admins():
  veri = True
  while(veri):
    try:
      codigoAd = GenerarCodigo2('administradores')
      nombreAd = input("Ingrese nombre del nuevo administrador: ")
      #Encriptación de la contraseña
      contraAd = getpass('Ingrese password del nuevo administrador:')
      #print(Contra)
      md5_hash = hashlib.md5()
      md5_hash.update(contraAd.encode())
      #print(md5_hash.hexdigest())
      contraAd = md5_hash.hexdigest()    
      Upload_Administradores(codigoAd, nombreAd, contraAd)
      veri = False
    except ValueError:
      print("Error, ingrese datos validos")

