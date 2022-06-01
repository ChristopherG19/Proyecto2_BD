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
from random import randint
import re
#Librería para encriptar contraseñas
import hashlib
#Librería para ocultar password
from getpass import getpass

from numpy import False_
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
    time.sleep(0)

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

def SearchPer(PerfilActual):
  ver = True 
  while (ver):
    try:
      print('\nDesea buscar algo? (1: Si, 2: No)')
      opci = int(input('Opcion: '))
      print()
      if (opci == 1):
        Busqueda = input("Buscar: ")
        Datos = SearchPers(Busqueda)
        charac = "()"
        for x in range(len(charac)):     
          Datos = Datos.replace(charac[x],"")
          
        Datos = Datos.split(',')
        
        print("\nInformación encontrada: ")
        
        if (Datos[-1] == 'peliculas'):
          print("Codigo: ", Datos[0].replace('"',""))
          print("Titulo: ", Datos[1])
          print("Genero: ", Datos[2])
          print("Year Publicacion: ", Datos[3])
          print("Duracion: ", Datos[4])
          
        elif (Datos[-1] == 'actores'):
          print("Codigo: ", Datos[0].replace('"',""))
          print("Nombre: ", Datos[1].replace('"',""))
          SearchByAct(Datos[1])
          
        elif (Datos[-1] == 'directores'):
          print("Codigo: ", Datos[0].replace('"',""))
          print("Nombre: ", Datos[1].replace('"',""))
          SearchByDir(Datos[1])
          
        else:
          print(Datos)
        
        now = datetime.datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

        Upload_Busquedas(PerfilActual, Busqueda, dt_string)

        print()
        
      elif (opci == 2):
        print("Saliendo...")
        ver = False
      else:
        print("Opcion invalida")
      
    except ValueError:
      print("Error, ingreso de datos invalido")

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

def Modifi_Admins(usuario):
  veri = True
  while (veri):
    try:
        escritura_lenta('\n¿Que desea hacer primero?: ')
        escritura_lenta('1) Ver administradores')
        escritura_lenta('2) Agregar administradores')
        escritura_lenta('3) Modificar nombre administradores')
        escritura_lenta('4) Modificar contrasena propia')
        escritura_lenta('5) Eliminar administradores')
        escritura_lenta('6) Cancelar\n')
        print()
        op = int(input('Opcion: '))
        
        if (op == 1):
          permanecer2 = True
          offset = 0
          pag = 1
          escritura_lenta("Administradores\n")
          while(permanecer2):
              if(offset >= 0):
                  obtenerData2('Administradores', offset)
                  escritura_lenta('Página: '+ str(pag))
                  escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                  siguiente = input('(a/d/l): ')
                  if (siguiente == 'a'):
                      offset += 10
                      pag += 1
                  elif (siguiente == 'd'):
                      offset -= 10
                      pag -= 1
                  elif (siguiente == 'l'):
                      permanecer2 = False
                  else:
                      escritura_lenta('La opción ingresada no es válida')
              else:
                  #Corregir el offset y evitar que este se convierta en 0
                  offset = 0
                  pag = 1
                  
        elif (op == 2):
          Agregar_Admins()
          print('Administrador agregado exitosamente')
          
        elif (op == 3):
          Modi_Admins_NC()
        
        elif (op == 4):
          ChangePasswordMe(usuario)
        
        elif (op == 5):
          Delete_Admins(usuario)
          
        elif (op == 6):
          veri = False
          
        else:
          escritura_lenta('Opcion invalida\n')
        
    except ValueError:
      print('Error, opcion invalida')
        
def Delete_Admins(usuario):
  veri = True
  while(veri):
    try:
      codigo_adm = input('Codigo: ')
      IsActive = Get_AdminActive(codigo_adm)
      if (Get_Admin(codigo_adm) and codigo_adm != usuario and IsActive == False):
        permanecer3 = True
        while (permanecer3):
            try:
                escritura_lenta('Seguro que desea eliminar al administrador?')

                conf = input('(y/n): ')
                if (conf == 'y'):
                    # Eliminar 
                    DeleteAdmin(codigo_adm)
                    veri = False
                    permanecer3 = False
                    escritura_lenta('El administrador fue eliminado exitosamente')
                elif (conf == 'n'):
                    # Cancelar
                    veri = False
                    permanecer3 = False
                else:
                    print('Ingrese una opcion valida')

            except Exception as ex:
                print(ex)
                escritura_lenta('Ingrese una opcion valida')
      elif (codigo_adm == usuario):
        print('No puedes eliminar tu propia cuenta')
        veri = False
      elif (IsActive):  
        print('Administrador en linea')
        veri = False
      else:
          #no existe
          escritura_lenta('El administrador ingresado no existe')
          escritura_lenta('Desea volver a escribir el codigo? (y/n)')
          op = input('(y/n): ')
          if (op == 'n'):
            veri = False
      
    except ValueError:
      print("Error, ingrese datos validos")

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
      Upload_Administradores(codigoAd, nombreAd, contraAd, False)
      veri = False
    except ValueError:
      print("Error, ingrese datos validos")

def Modi_Admins_NC():
  veri = True
  while(veri):
    try:
      codigo_adm = input('Codigo: ')
      if (Get_Admin(codigo_adm) ):
        permanecer3 = True
        while (permanecer3):
            try:
                print('\nQue deseas hacer?')
                print('1) Modificar nombre')
                print('2) Salir\n')
                
                op = int(input('Opcion: '))
                
                if (op == 1):
                  print()
                  NuevoN = input('Nombre Nuevo: ')
                  UpdateNameAdmin(NuevoN, codigo_adm)
                  print('Nombre modificado exitosamente')
                  
                elif (op == 2):
                  permanecer3 = False
                  veri = False
                else:
                  print('Opcion invalida')
                  print()
                  
            except Exception as ex:
                print(ex)
                escritura_lenta('Ingrese una opcion valida')
      else:
          #no existe
          escritura_lenta('El administrador ingresado no existe')
          escritura_lenta('Desea volver a escribir el codigo? ')
          op = input('(y/n): ')
          if (op == 'n'):
            veri = False
      
    except ValueError:
      print("Error, ingrese datos validos")

def ChangePasswordMe(usuario):
  print()
  ver_contrasena2 = True 
  while (ver_contrasena2):
    contraActual = getpass('Contraseña actual: ')
    md5_hash = hashlib.md5()
    md5_hash.update(contraActual.encode())
    contraActual = md5_hash.hexdigest()

    #verificarla
    if (LogInAdmin(usuario, contraActual)):
      # Proseguir
      escritura_lenta('Ingrese la nueva contraseña ')
      contraNueva = getpass('\nNueva contraseña: ')
      contraNueva2 = getpass('\nIngresela nuevamente: ')

      if (contraNueva == contraNueva2):
        ''''''
        md5_hash = hashlib.md5()
        md5_hash.update(contraNueva.encode())
        contraNueva = md5_hash.hexdigest()

        Mod_ContraseñaAdmin(contraNueva, usuario)

        ver_contrasena2 = False
      else:
        print('Error, las contraseñas son distintas')

    else: 
      # Contraseña ingresada incorrectamente
      escritura_lenta('Contraseña ingresada incorrectamente')
      escritura_lenta('Desea probar nuevamente?')
      ooop = input('(s/n): ')
      if (ooop == 'n'):
        # Cancelar
        ver_contrasena2 = False

def Gen_hora():

  hora = random.randint(0,23)
  min = random.randint(0,59)
  seg = random.randint(0,59)
  
  if(hora >= 0 & hora < 10):
    hora = str(hora).rjust(2, '0')
  
  if(min >= 0 & min < 10):
    min = str(min).rjust(2, '0')
    
  if(seg >= 0 & seg < 10):
    seg = str(seg).rjust(2, '0')
    
  hora_f = str(hora) + ':' + str(min) + ':' + str(seg)
  
  return hora_f

def GenFechaRepro(year, mes, dia):
  meses30 = [4,6,9,11]
  meses31 = [1,3,5,7,8,10,12]
  meses28 = [2]

  newmonth = random.randint(int(mes), 12)
    
  newday = 0
  if (int(mes) == newmonth):
    # Se tiene que verificar que se termine de ver el mismo día, o los que restan del mes
    if (newmonth in meses30):
      newday = random.randint(int(dia), 30)
    elif (newmonth in meses31):
      newday = random.randint(int(dia), 31)
    elif (newmonth in meses28):
      newday = random.randint(int(dia), 28)
  else:
    if (newmonth in meses30):
      newday = random.randint(1, 30)
    elif (newmonth in meses31):
      newday = random.randint(1, 31)
    elif (newmonth in meses28):
      newday = random.randint(1, 28)
 
  if(newmonth >= 0 & newmonth < 10):
    newmonth = str(newmonth).rjust(2, '0')
  
  if(newday >= 0 & newday < 10):
    newday = str(newday).rjust(2, '0')
  
  fechaF = str(year)+'-'+str(newmonth)+'-'+str(newday)
  
  return fechaF 
 
def Gen_FechaFin(fecha):
  fechaS = fecha.split('-')
  year = fechaS[0]
  mes = fechaS[1]
  dia = fechaS[2]
  
  meses30 = [4,6,9,11]
  meses31 = [1,3,5,7,8,10,12]
  meses28 = [2]

  newmonth = random.randint(int(mes), 12)
    
  newday = 0
  if (int(mes) == newmonth):
    # Se tiene que verificar que se termine de ver el mismo día, o los que restan del mes
    if (newmonth in meses30):
      newday = random.randint(int(dia), 30)
    elif (newmonth in meses31):
      newday = random.randint(int(dia), 31)
    elif (newmonth in meses28):
      newday = random.randint(int(dia), 28)
  else:
    if (newmonth in meses30):
      newday = random.randint(1, 30)
    elif (newmonth in meses31):
      newday = random.randint(1, 31)
    elif (newmonth in meses28):
      newday = random.randint(1, 28)
 
  if(newmonth >= 0 & newmonth < 10):
    newmonth = str(newmonth).rjust(2, '0')
  
  if(newday >= 0 & newday < 10):
    newday = str(newday).rjust(2, '0')
  
  fechaF = str(year)+'-'+str(newmonth)+'-'+str(newday)
  
  return fechaF

def Gen_TimeDateRand(year):

  # Obtener la fecha

  meses30 = [1,3,5,7,8,10,12,4,6,9,11]
  meses31 = [1,3,5,7,8,10,12]
  meses28 = [2,1,3,5,7,8,10,12,4,6,9,11]

  dia = random.randint(1,31)
  mes = 0

  if (dia > 30):
    # Se puede seleccionar solo de meses con 31 días
    mes = random.choice(meses31)
  elif (dia <= 30 and dia > 28):
    # Se puede seleccionar solo de meses con 30 o más días
    mes = random.choice(meses30)
  else:
    mes = random.choice(meses28)

  # Obtener la hora

  horasPos = ['00', '01', '02',
              '03', '04', '05',
              '06', '07', '08',
              '09', '10', '11',
              '12', '13', '14',
              '15', '16', '17',
              '18', '19', '20',
              '21', '22', '23',]

  minsSegPos = ['00', '01', '02', '03', '04', '05',
            '06', '07', '08', '09', '10', '11',
            '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29',
            '31', '32', '33', '34', '35', '36',
            '37', '38', '39', '40', '41', '42',
            '43', '44', '45', '46', '47', '48',
            '49', '50', '51', '52', '53', '54',
            '55', '56', '57', '58', '59', '30']


  hora = random.choice(horasPos)
  mins = random.choice(minsSegPos)
  segs = random.choice(minsSegPos)
  
  dateTimeRand = str(year)+'-'+str(mes)+'-'+str(dia)+' '+str(hora)+':'+str(mins)+':'+str(segs)+'.000'

  return dateTimeRand
  
def Generacion_visualizaciones(cant_visua, fecha):
  
  for i in range(cant_visua):
    Code_perfil_random = random.choice(Get_AllPerfiles())
    Code_pelicula_random = random.choice(Get_AllMovies())
    TiempoConsumido = Get_PeliTime(Code_pelicula_random) - random.randint(0,Get_PeliTime(Code_pelicula_random)-1)
    Finish = random.choice([True, False])
    hora = Gen_hora()
    fechaC = ''

    now = datetime.datetime.now()
    horaExtra = now.strftime("%H:%M:%S")
    today = datetime.date.today()
    fechaExtra = today.strftime("%Y/%m/%d")
        
    if (Finish == True):
      Upload_PerfilReproducciones(Code_perfil_random,Code_pelicula_random,fechaExtra,horaExtra)
      fechaC = Gen_FechaFin(fecha)
    else:
      fechaC = '0001-01-01'

    Correo = Get_mail(Code_perfil_random)
    Tipo = Get_Sub(Correo)
    if (Tipo == 'Gratis' and Finish):
      
      anuncios_mostrar(anuncios_cantidad(anuncios_tiempo(Code_pelicula_random)),anuncios_tiempo(Code_pelicula_random), Correo)
    
    Upload_ContenidoPerfil(Code_perfil_random, Code_pelicula_random, TiempoConsumido, Finish, fecha, hora, fechaC)
    
    print(f"Visualizaciones insertadas ({i+1}/{cant_visua})")
    
  print("\nSimulacion completada exitosamente")

def Generar_busquedas(cant_busquedas):

  posBusquedas = ['Avengers', 'Shrek', 'Emma Watson', 'It', 'El pianista', 'Harry Potter', 'Chicago', 'Ron Howard', 
                  'Marc Forster', 'Steven Spielberg', 'Steven Spielberg', 'Joaquin Phoenix', 'Tom Hanks', 
                  'Leonardo DiCaprio', 'Jim Carrey', 'El viaje de Chihiro', 'The Lord of the Rings: The Return of the King', 
                  'El Conjuro', 'Spiderman', 'Brujillizas', 'High School Musical', 'Harry Potter y la Orden del Fénix',
                  'Dr. Strange', 'Batman', 'Avatar', 'Red', 'Moonfall', 'Encanto', 'Disney', 'Animales Fantásticos',
                  'Pixar', 'Tom Holand', 'Venom', 'Coraline', 'Big Hero 6', 'Acuaman', 'La mujer maravilla', 'Sonic', 'Joker',
                  'Zendaya', 'Will Smith', 'Ryan Renolds', 'Lin-Manual Miranda', 'Ben Affleck', 'Enredados', 'Luca',
                  'Avengers', 'Avengers', 'Avengers', 'Shrek', 'Shrek', 'Shrek', 'Harry Potter', 'Harry Potter', 'Steven Spielberg']

  for i in range(cant_busquedas):
    Code_perfil_random = random.choice(Get_AllPerfiles())
    busca_gen = random.choice(posBusquedas)
    fecha_gen = Gen_TimeDateRand(2022)

    Upload_Simulation_Search(Code_perfil_random, busca_gen, fecha_gen)
    print(f"Busqueda insertada ({i+1}/{cant_busquedas})")

    

