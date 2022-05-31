'''
  Universidad del Valle de Guatemala
  Bases de datos 1
  Proyecto 2

  Integrantes:
    - Gabriel Vicente 20498
    - Maria Isabel Solano 20504
    - Christopher García 20541
'''

#librerias
from getpass import getpass
from logging import exception
from msilib.schema import Error
from pickle import TRUE
from re import A
from unittest.loader import VALID_MODULE_NAME
from sympy import true
from Funciones import *
from ConnectionBD import *

#Funciones que seran añadidas luego al documento Funciones
def obtenerData(entidad, offset):
    #Realizar query
    Conseguir_Data(entidad, offset)
    data = ''#Ingresar lista con toda la informacion
    return data

def obtenerCorreos(entidad, offset):
    #Realizar query
    Get_Correos(entidad, offset)
    data = ''#Ingresar lista con toda la informacion
    return data

'''
Genera un codigo Concatendando las primeras 3 letras del nombre
 de la entidad y el numero correspondiente dependiendo de la cantidad de
 datos que se encuentran ingresados en la tabla correspondiente (count)
'''
def GenerarCodigo(entidad):
    #Obtener data de la base de datos
    cant = Gen_code(entidad)
    codigo = str(entidad)[0:3] + str(cant)
    return codigo

'''
Agregar contenido hace cambios en las siguientes entidades
- 
'''
def AgregarContenido():
    #Parte 1, datos generales - Tabla Peliculas
    codigo_pel = GenerarCodigo('Peliculas')
    titulo = input('Titulo: ')
    genero = input('Genero: ')
    duracion= 0
    verificador_num = True
    while (verificador_num):
        try:
            duracion = int(input('Duracion: '))
            verificador_num = False #salir del verificador
        except:
            escritura_lenta('Ingrese un numero valido')
    anio = 0
    verificador_num = True
    while(verificador_num):
        try:
            anio = int(input('Año: '))
            verificador_num = False
        except:
            escritura_lenta('Ingrese un numero valido')
    '''INGRESAR A LA BASE DE DATOS'''
    Upload_Peliculas(codigo_pel, titulo, genero, anio, duracion)

    #Parte 2, directores - Tablas directores y director_pelicula
    permanecer = True
    while (permanecer):
        escritura_lenta('\n¿Desea ingresar un(otro) director? ')
        otro = input('(y/n): ')
        
        if (otro == 'y'):
            verificador_director = True
            while (verificador_director): 
                director = input('Nombre del director: ')
                existencia = Get_Director(director)
                if (existencia):
                    #Ya existe en la base de datos
                    codigo_director = existencia[0]
                    '''
                    Ingresar a la BD director_pelicula el codigo del 
                    director y el codigo de la pelicula
                    '''
                    Upload_DirectoresPeliculas(codigo_pel, codigo_director)
                    print('Director(es) ingresado(s) exitosamente')
                    verificador_director = False
                else:
                    escritura_lenta('El director ingresado no existe, desea ingresarlo nuevamente o crear un usuario')
                    escritura_lenta('1) Añadirlo')
                    escritura_lenta('2) Ingresarlo nuevamente\n')
                    oppp = input('Opcion: ')
                    if (oppp == '1'):
                        #Crear dato en la base de datos
                        codigo_director = GenerarCodigo('directores')
                        '''
                        Ingresar a la tabla directores, nombre y codigo
                        Ingresar a la tabla director_pelicula el codigo del
                        director y el codigo de la pelicula
                        '''
                        Upload_Directores(codigo_director, director)
                        Upload_DirectoresPeliculas(codigo_pel, codigo_director)
                        print('Director(es) ingresado(s) exitosamente')
                        verificador_director = False     

        elif (otro == 'n'):
            #Salir de ingresar directores y continuar
            permanecer = False

        else: 
            #Error
            escritura_lenta('Ingrese una respuesta valida\n')

    #Parte 3. Actores - Tablas Actores y Actores_peliculas
    permanecer = True
    while (permanecer):
        escritura_lenta('\nDesea ingresar el nombre de un actor? ')
        otro = input('(y/n): ')

        if (otro == 'y'):
            verificar_actor = True
            while (verificar_actor):
                actor = input('Nombre del actor: ')
                existencia = Get_Actor(actor)
                if (existencia):
                    #Ya existe en la base de datos
                    codigo_actor = existencia[0]
                    '''
                    Ingresar a la tabla Actor_Pelicula (codigo_pelicula, codigo_actor)
                    '''
                    Upload_ActoresPeliculas(codigo_pel, codigo_actor)
                    print('Actor(es) ingresado(s) exitosamente')
                    verificar_actor = False
                else:
                    escritura_lenta('El actor ingresado no existe, desea ingresarlo nuevamente o crear un usuario')
                    escritura_lenta('1) Añadirlo')
                    escritura_lenta('2) Ingresarlo nuevamente\n')
                    oppp = input('Opcion: ')
                    if (oppp == '1'):
                        #Crear dato en la base de datos
                        codigo_actor = GenerarCodigo('actores')
                        '''
                        Ingresar a la tabla actores (codigo y nombre)
                        '''
                        '''
                        Ingresar a la tabla actores_peliculas (codigo y codigo_pelicula)
                        '''
                        Upload_Actores(codigo_actor, actor)
                        Upload_ActoresPeliculas(codigo_pel, codigo_actor)
                        print('Actor(es) ingresado(s) exitosamente')
                        verificar_actor = False
                        
        elif (otro == 'n'):
            #Salir de ingresar actores y continuar
            permanecer = False
        else :
            #Error
            escritura_lenta('Ingrese una respuesta valida\n')

    #Parte 4, Premiaciones - Tabla premiaciones
    permanecer = True
    while (permanecer):
        escritura_lenta('\nLa pelicula ha recibido algun(os) premio(s)? ')
        otro = input('(y/n): ')
        if (otro == 'y'):
            premiacion = input('Premiacion: ')
            reconocimiento = input('Reconocimiento: ')
            verificador_fecha = True
            fecha = ''
            while (verificador_fecha):
                fecha = input('Fecha (YYYY-MM-DD): ')
                if (Check_Date(fecha)):
                    #se puede continuar
                    verificador_fecha = False
                else: 
                    escritura_lenta('Ingrese una fecha valida')

            '''
            Ingresar a la BD, a la tabla premiaciones codigo_pelicula, 
             premiacion, reconocimiento y fecha
            '''
            Upload_Premiaciones(codigo_pel, premiacion, reconocimiento, fecha)
            print('Premiacion ingresada exitosamente')
            permanecer = False
        elif (otro == 'n'):
            #Salir de ingresar premios y continuar
            permanecer = False
        else:
            #Error
            escritura_lenta('Ingrese una respuesta valida \n')

'''
Permite hacer cambios en el contenido
'''
def ModContenido_pelicula():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver contenido')
            escritura_lenta('2) Modificar utilizando codigo')
            escritura_lenta('3) Cancelar')
            print()
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Peliculas', offset)
                        escritura_lenta('Pagina: '+ str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_pel = input('Codigo pelicula: ')
                    if (Get_Movie(cod_pel)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) Titulo')
                                escritura_lenta('2) Genero')
                                escritura_lenta('3) Año')
                                escritura_lenta('4) Duracion')
                                escritura_lenta('5) Cancelar')
                                print()
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                print()
                                
                                if(dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        cambiarlo en la base de datos 
                                    '''
                                    Modificar_Pelicula('titulo', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 2):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        cambiarlo en la base de datos
                                    '''
                                    Modificar_Pelicula('genero', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 3):
                                    verificador_num = True
                                    while (verificador_num):
                                        try:
                                            nuevoDato = int(input('Nuevo año: '))
                                            verificador_num = False
                                        except:
                                            escritura_lenta('Ingrese un dato valido')
                                    '''
                                        Obtener nuevo dato del usuario y
                                        cambiarlo en la base de datos
                                    '''
                                    Modificar_Pelicula('YearP', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 4):
                                    verificador_num = True
                                    while (verificador_num):
                                        try:
                                            nuevoDato = int(input('Nueva duracion: '))
                                            verificador_num = False
                                        except:
                                            escritura_lenta('Ingrese un dato valido')
                                    '''
                                        Obtener nuevo dato del usuario y
                                        cambiarlo dato en la base de datos
                                    '''
                                    Modificar_Pelicula('Duracion', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 5):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False
                                
                                else:
                                    escritura_lenta('La opcion ingresada no es valida')
                                      
                            except Exception as ex:
                                #
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('La pelicula ingresada no existe')
                        escritura_lenta('Desea volver a escribir el codigo? ')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
        except Exception as ex:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Permite elimiar peliculas
'''
def Eliminar_pelicula(usuario):
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver contenido')
            escritura_lenta('2) Eliminar utilizando codigo')
            escritura_lenta('3) Cancelar')
            print()
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Peliculas', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_pel = input('Codigo pelicula: ')
                    if (Get_Movie(cod_pel)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            escritura_lenta('¿Seguro que desea eliminar la pelicula? ')
                            confirm = input('(y/n): ')
                            if (confirm == 'y'):
                                '''
                                Ejecutar query para eliminar contenido con ese nombre!
                                '''
                                Delete_Pelicula(cod_pel)
                                UploadBitacora(usuario)
                                print('Pelicula eliminada exitosamente')
                                permanecer3 = False
                                permanecer2 = False
                                
                            elif (confirm == 'n'):
                                #cancelar la eliminacion de la pelicula escrita
                                permanecer3 = False
                                permanecer2 = False
                            else: 
                                #Error
                                print('La opcion ingresada no existe')
                    else:
                        #no existe
                        escritura_lenta('La pelicula ingresada no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
                
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Agrega Anunciantes a la tabla Anunciantes
'''
def Agregar_Anunciantes():
    codigo_anunciante = GenerarCodigo('anunciantes')
    nombre = input('Nombre anunciante: ')
    '''
    Agregar Anuncainte a la tabla anunciantes
    '''
    Upload_Anunciantes(codigo_anunciante, nombre)
    print('Anunciante agregado con exito')

def ModAnunciantes():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver anunciantes')
            escritura_lenta('2) Modificar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anunciantes', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_an = input('Codigo Anunciante: ')
                    if (Get_Anunciante(cod_an)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) Nombre')
                                escritura_lenta('2) Cancelar\n')
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                
                                if (dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos 
                                    '''
                                    Mod_Anunciantes('nombre', nuevoDato, cod_an)
                                    print('Anunciante modificado exitosamente')
                                    permanecer3 = False
                                    permanecer2 = False
                                    
                                elif(dato_mod == 2):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El anunciante ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

def EliminarAnunciantes(usuario):
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver anunciantes')
            escritura_lenta('2) Eliminar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver anuncios
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anunciantes', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Eliminar con codigo
                Codigo_anunciante = input('Ingrese el codigo del anunciante: ')
                Delete_Anunciante(Codigo_anunciante)
                print('Anunciante eliminado exitosamente')
                UploadBitacora(usuario)
            elif (op == 3):
                #salir
                permanecer = False
        except Exception as ex:
            print(ex)
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Agrega Anuncions a la tabla Anuncios
'''
def Agregar_Anuncios():
    permanecer = True
    while (permanecer):
        cod_anuncio = GenerarCodigo('anuncios')
        anunciante = input('Codigo del anunciante: ')
        existencia = Get_Anunciante(anunciante)
        if (existencia):
            #existe
            cod_anunciante = existencia[0]
            contenido = input('Contenido de anuncio: ')
            duracion = 0
            verificador_num = True
            while (verificador_num):
                try:
                    duracion = int(input('Duracion: '))
                    verificador_num = False
                except:
                    escritura_lenta('Ingrese una respuesta valida\n')
            Link = input('Link del contenido: ')
            #salir de la funcion
            Upload_Anuncios(cod_anuncio, cod_anunciante, duracion, contenido, Link)
            print('Anuncio agregado exitosamente')
            permanecer = False
        else:
            escritura_lenta('El anunciante no existe')
            escritura_lenta('Desea escribir nuevamente el nombre del anunciante? \n')
            op = input('(y/n): ')
            if (op == 'n'):
                permanecer = False

def ModAnuncios():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver anuncios')
            escritura_lenta('2) Modificar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anuncios', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_an = input('Codigo Anuncio: ')
                    if (Get_Anuncio(cod_an)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) ContenidoPromocional')
                                escritura_lenta('2) Link')
                                escritura_lenta('3) Duracion')
                                escritura_lenta('4) Cancelar\n')
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                
                                if (dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos 
                                    '''
                                    Mod_Anuncios('contenidopromocional', nuevoDato, cod_an)
                                    print('Anuncio modificado exitosamente')
                                    permanecer3 = False
                                    permanecer2 = False
                                elif (dato_mod == 2):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos
                                    '''
                                    Mod_Anuncios('Link', nuevoDato, cod_an)
                                    print('Anuncio modificado exitosamente')
                                    permanecer3 = False
                                    permanecer2 = False
                                elif(dato_mod == 3):
                                    verificador_num = True
                                    while (verificador_num):
                                        try:
                                            nuevoDato = int(input('Nueva duracion: '))
                                            verificador_num = False
                                        except Exception as ex:
                                            
                                            escritura_lenta('Ingrese un dato valido')
                                    '''
                                        Cambiar en la base de datos
                                    '''
                                    Mod_Anuncios('duracion', nuevoDato, cod_an)
                                    print('Anuncio modificado exitosamente')
                                    permanecer3 = False
                                    permanecer2 = False
                                elif(dato_mod == 4):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El anunciante ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Eliminar anunciantes
'''
def EliminarAnuncios(usuario):
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver contenido')
            escritura_lenta('2) Eliminar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver anuncios
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anuncios', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Eliminar con codigo
                Codigo_anuncio = input('Ingrese el codigo del anuncio: ')
                Delete_Anuncio(Codigo_anuncio)
                UploadBitacora(usuario)
                print('Anuncio eliminado exitosamente')

            elif (op == 3):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Upgrade/Downgrade Usuarios
'''
def DownUpGrade_Usuarios():
    permanecer = True
    while (permanecer):
        escritura_lenta('Ingrese el correo de la cuenta que desea modificar\n')
        correo = input('Correo: ')
        if (Correo_Validacion(correo)):
            #El correo es valido
            escritura_lenta('La suscripcion actual de '+correo+ ' es ' + Get_Sub(correo))
            permanecer2 = True
            while (permanecer2):
                escritura_lenta('A que suscripcion desea cambiarlo? (1, 2, 3)\n')
                nuevaSus = input('Nueva suscripcion: ')
                if (nuevaSus == '1'):
                    #gratis
                    '''
                    Query que cambia la suscripcion
                    '''
                    Mod_Usuarios('Gratis', correo)
                    print('Cambio de suscripcion exitoso')
                    permanecer2 = False
                    permanecer = False
                elif (nuevaSus == '2'):
                    #estandar
                    '''
                    Query que cambia la suscripcion
                    '''
                    Mod_Usuarios('Estandar', correo)
                    print('Cambio de suscripcion exitoso')
                    cant = Get_Perfiles(correo)
                    if (cant == 4):
                        ActPerfil(correo)
                    permanecer2 = False
                    permanecer = False
                elif (nuevaSus == '3'):
                    #premium
                    '''
                    Query que cambia la suscripcion
                    '''
                    Mod_Usuarios('Avanzada', correo)
                    print('Cambio de suscripcion exitoso')
                    cant = Get_Perfiles(correo)
                    if (cant == 8):
                        ActPerfil(correo)
                    permanecer2 = False
                    permanecer = False
                else:
                    #Error
                    escritura_lenta('La opcion ingresada no es valida')
                    escritura_lenta('¿Desea continuar? ')
                    oppp = input('(y/n)')
                    if (oppp == 'n'):
                        permanecer2 = False
                        permanecer = False
                
        else:
            #el correo no es valido
            escritura_lenta('Desea ingresar el correo nuevamente? ')
            op = input('(y/n): ')
            if (op == 'n'):
                permanecer = False

'''
Desactivar usuarios
'''
def desactivar_Usuarios():
    permanecer = True
    while (permanecer):
        escritura_lenta('Ingrese el correo de la cuenta que desea desactivar\n')
        correo = input('Correo: ')
        if (Correo_Validacion(correo)):
            #El correo es valido
            if Get_Estado(correo):
                escritura_lenta('El estado actual de '+correo+ ' es cuenta activada')
            else:
                escritura_lenta('El estado actual de '+correo+ ' es cuenta desactivada')
            permanecer2 = True
            while (permanecer2):
                escritura_lenta('Seguro que desea toggle con el estado de la cuenta? ')
                opp = input('(y/n): ')
                if (opp == 'y'):
                    nuevoEstado = not Get_Estado(correo)
                    '''
                    Query para acer UPDATE en el dato
                    '''
                    if Get_Estado(correo):
                        Desactivar_Usuarios(nuevoEstado, correo)
                        print('Desactivacion exitosa')
                    else:
                        Desactivar_Usuarios(nuevoEstado, correo)
                        print('Activacion exitosa')
                    permanecer2 = False
                    permanecer = False
                elif (opp == 'n'):
                    permanecer2 = False
                    permanecer = False
                else:
                    #Error
                    escritura_lenta('La opcion ingresada no es valida')
                
        else:
            #el correo no es valido
            escritura_lenta('Desea ingresar el correo nuevamente? (y/n)')
            op = input('(y/n): ')
            if (op == 'n'):
                permanecer = False

def reporte_1():
    escritura_lenta('Ingreso de los rangos de fecha')
    escritura_lenta('Fecha A\n')
    year_A =    SolicitudNum3('Ingresa el valor de Year: ')
    month_A =   SolicitudNum3('Ingresa el valor de Month: ')
    if month_A < 1 or month_A > 12:
        month_A = 1
    day_A =     SolicitudNum3('Ingresa el valor de Day: ')
    if day_A < 1 or day_A > 31:
        day_A = 1
    escritura_lenta('Fecha B\n')
    year_B =    SolicitudNum3('Ingresa el valor de Year: ')
    month_B =   SolicitudNum3('Ingresa el valor de Month: ')
    if month_B < 1 or month_B > 12:
        month_B = 1
    day_B =     SolicitudNum3('Ingresa el valor de  Day: ')
    if day_B < 1 or day_B > 31:
        day_B = 1

    fechaA= str(year_A)+'-'+str(month_A)+'-'+str(day_A)

    fechaB= str(year_B)+'-'+str(month_B)+'-'+str(day_B)
    query_reporte_1(fechaA, fechaB, fechaA, fechaB)

    return 2

def reporte_2():
    escritura_lenta('Ingreso de los rangos de fecha\n')
    escritura_lenta('Fecha A\n')
    year_A =    SolicitudNum3('Ingresa el valor de Year: ')
    month_A =   SolicitudNum3('Ingresa el valor de Month: ')
    if month_A < 1 or month_A > 12:
        month_A = 1
    day_A =     SolicitudNum3('Ingresa el valor de Day: ')
    if day_A < 1 or day_A > 31:
        day_A = 1
    escritura_lenta('Fecha B\n')
    year_B =    SolicitudNum3('Ingresa el valor de Year: ')
    month_B =   SolicitudNum3('Ingresa el valor de Month: ')
    if month_B < 1 or month_B > 12:
        month_B = 1
    day_B =     SolicitudNum3('Ingresa el valor de  Day: ')
    if day_B < 1 or day_B > 31:
        day_B = 1

    fechaA= str(year_A)+'-'+str(month_A)+'-'+str(day_A)
    fechaB= str(year_B)+'-'+str(month_B)+'-'+str(day_B)
    
    GetCantReprGratis(fechaA, fechaB)
    GetCantReprEst(fechaA, fechaB)
    GetCantReprAva(fechaA, fechaB)

def reporte_3():
    TopAct()
    print()
    TopDir()

def reporte_5():
    escritura_lenta('Ingreso de la fecha\n')

    year_A =    SolicitudNum3('Ingresa el valor de Year: ')
    month_A =   SolicitudNum3('Ingresa el valor de Month: ')
    if month_A < 1 or month_A > 12:
        month_A = 1
    day_A =     SolicitudNum3('Ingresa el valor de Day: ')
    if day_A < 1 or day_A > 31:
        day_A = 1

    fechaA= str(year_A)+'-'+str(month_A)+'-'+str(day_A)

    query_reporte_5(fechaA)

    return 2

def Mod_Actores():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver actores')
            escritura_lenta('2) Agregar actores')
            escritura_lenta('3) Modificar utilizando codigo')
            escritura_lenta('4) Eliminar utilizando codigo')
            escritura_lenta('5) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('actores', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                # Agregar actores
                verificar_actor = True
                while (verificar_actor):
                    actor = input('Nombre del actor: ')
                    existencia = Get_Actor(actor)
                    if (existencia):
                        #Ya existe en la base de datos
                        print(actor, ' ya existe en la base de datos')
                        # Ignorar y salir 
                        verificar_actor = False
                    else:
                        escritura_lenta('El dato ingresado fue '+actor+', \n¿está seguro que desea ingresarlo?')
                        oppp = input('(y/n) ')
                        if (oppp == 'y'):
                            #Crear dato en la base de datos
                            codigo_actor = GenerarCodigo('actores')

                            # Insertar en la base de datos
                            Upload_Actores(codigo_actor, actor)

                            print('Actor ingresado exitosamente')
                            verificar_actor = False
                        else:
                            verificar_actor = False
                            ''''''

            elif (op == 3):
                #Modificar actores con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_an = input('Codigo actor: ')
                    if (Get_Actor2(cod_an)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) Nombre')
                                escritura_lenta('2) Cancelar\n')
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                
                                if (dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos 
                                    '''
                                    Mod_ActoresN('nombre', nuevoDato, cod_an)
                                    print('Actor modificado exitosamente')
                                    permanecer3 = False
                                    permanecer2 = False
                                    
                                elif(dato_mod == 2):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El actor ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 4):
                # Eliminar Actores
                permanecer2 = True
                while (permanecer2):
                    cod_ac = input('Codigo actor: ')
                    if (Get_Actor2(cod_ac)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                print(Get_Actor2(cod_ac))
                                escritura_lenta('Seguro que desea eliminar al Actor?')

                                conf = input('(y/n): ')
                                if (conf == 'y'):
                                    # Eliminar 
                                    Delete_Actor(cod_ac)
                                    permanecer2 = False
                                    permanecer3 = False
                                    escritura_lenta('El actor fue eliminado exitosamente')
                                elif (conf == 'n'):
                                    # Cancelar
                                    permanecer2 = False
                                    permanecer3 = False
                                else:
                                    print('Ingrese una opcion valida')

                            except Exception as ex:
                                print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El actor ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 5):
                #salir
                permanecer = False
        except Exception as err:
            escritura_lenta('Ingrese una respuesta valida\n')
            print(err)
    
def Mod_Directores():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver directores')
            escritura_lenta('2) Agregar Directores')
            escritura_lenta('3) Modificar utilizando codigo')
            escritura_lenta('4) Eliminar utilizando codigo')
            escritura_lenta('5) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('directores', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                # Agregar Directores
                verificar_director = True
                while (verificar_director):
                    director = input('Nombre del director: ')
                    existencia = Get_Director2(director)
                    if (existencia):
                        #Ya existe en la base de datos
                        print(director, ' ya existe en la base de datos')
                        # Ignorar y salir 
                        verificar_director = False
                    else:
                        escritura_lenta('El dato ingresado fue '+director+', \n¿está seguro que desea ingresarlo?')
                        oppp = input('(y/n) ')
                        if (oppp == 'y'):
                            #Crear dato en la base de datos
                            codigo_director = GenerarCodigo('directores')

                            # Insertar en la base de datos
                            Upload_Directores(codigo_director, director)

                            print('Actor ingresado exitosamente')
                            verificar_director = False
                        else:
                            verificar_director = False
                            ''''''

            elif (op == 3):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_an = input('Codigo director: ')
                    if (Get_Director2(cod_an)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) Nombre')
                                escritura_lenta('2) Cancelar\n')
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                
                                if (dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos 
                                    '''
                                    Mod_DirectoresN('nombre', nuevoDato, cod_an)
                                    print('Director modificado exitosamente')
                                    permanecer3 = False
                                    permanecer2 = False
                                    
                                elif(dato_mod == 2):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El director ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 4):
                # Eliminar Directores
                permanecer2 = True
                while (permanecer2):
                    cod_dir = input('Codigo director: ')
                    if (Get_Director2(cod_dir)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                print(Get_Director2(cod_dir))
                                escritura_lenta('Seguro que desea eliminar al director?')

                                conf = input('(y/n): ')
                                if (conf == 'y'):
                                    # Eliminar 
                                    Delete_Director(cod_dir)
                                    permanecer2 = False
                                    permanecer3 = False
                                    escritura_lenta('El director fue eliminado exitosamente')
                                elif (conf == 'n'):
                                    # Cancelar
                                    permanecer2 = False
                                    permanecer3 = False
                                else:
                                    print('Ingrese una opcion valida')

                            except Exception as ex:
                                print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El director ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 5):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')  

def Mod_Perfiles():
    veri = True
    while (veri):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver cuentas')
            escritura_lenta('2) Modificar perfiles')
            escritura_lenta('3) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        Get_Correos('cuenta', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1
            elif (op == 2):
                #Modificar con correo
                permanecer2 = True
                while (permanecer2):
                    correo_u = input('Correo: ')
                    if (Get_Cuenta(correo_u)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('Correo encontrado')
                                escritura_lenta('Opciones disponibles: ')
                                escritura_lenta('1) Ver perfiles')
                                escritura_lenta('2) Modificar perfil utilizando codigo')
                                escritura_lenta('3) Cancelar\n')
                                opci = int(input('Dato: '))
                                
                                if (opci == 1):
                                    Get_PerfilesInfo2(correo_u)
                                
                                elif (opci == 2): 
                                    #Modificar con codigo
                                    permanecer4 = True
                                    while (permanecer4):
                                        cod_per = input('Codigo perfil: ')
                                        if (Get_PerfilCode3(correo_u, cod_per)):
                                            #existe
                                            permanecer5 = True
                                            while (permanecer5):
                                                try:
                                                    escritura_lenta('\nQue dato desea modificar?: ')
                                                    escritura_lenta('1) Nombre')
                                                    escritura_lenta('2) Cancelar\n')
                                                    nuevoDato =''
                                                    dato_mod = int(input('Dato: '))
                                                    
                                                    if (dato_mod == 1):
                                                        nuevoDato = input('Nuevo: ')
                                                        '''
                                                            Cambiar en la base de datos 
                                                        '''
                                                        Mod_perfil(nuevoDato, cod_per, correo_u)
                                                        print('Perfil modificado exitosamente')
                                                        permanecer5 = False
                                                        permanecer4 = False
                                                        permanecer3 = False
                                                        permanecer2 = False
                                                        
                                                    elif(dato_mod == 2):
                                                        escritura_lenta('[Cancelando...]\n')
                                                        permanecer5 = False
                                                        permanecer4 = False

                                                    else:
                                                        escritura_lenta('La opcion ingresada no es valida')  
                                                except Exception as ex:
                                                    escritura_lenta('Ingrese una opcion valida')
                                        else:
                                            print('El codigo de perfil no existe')
                                elif (opci == 3):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El correo ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                veri = False
            
        except:
            print('Error, opcion invalida')
    
def Mod_Premiaciones():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver premiaciones')
            escritura_lenta('2) Modificar nombre de la premiacion')
            escritura_lenta('3) Modificar nombre del reconocimiento')
            escritura_lenta('4) Modificar fecha del reconocimiento')
            escritura_lenta('5) Eliminar una premiacion')
            escritura_lenta('6) Cancelar')
            op = input("\nOpcion: ")
            if(op == '1'):
                #ver premiaciones
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('premiaciones', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == '2'):
                #Modificar nombre de la premiación
                escritura_lenta('Por favor ingrese los datos que a continuación se le solicitaran\n')
                codigo_pelicula = input('Codigo de la pelicula: ')
                reconocimiento = input('Reconocimiento: ')
                fecha = ''
                verificador_fecha = True
                while (verificador_fecha):
                    fecha = input('Fecha de la premiacion (en formato YY-MM-DD): ')
                    if (Check_Date(fecha)):
                        #se puede continuar
                        verificador_fecha = False
                    else: 
                        escritura_lenta('Ingrese una fecha valida')
                
                #obtener nuevo dato
                veri = True
                while (veri):
                    escritura_lenta('A continuacion escriba el nuevo nombre de la premiacion')
                    premiacion = input('Premiacion: ')

                    escritura_lenta('\nEl dato ingresado fue: '+ str(premiacion))
                    escritura_lenta('¿Esta este correcto?')

                    correcto = input('(y/n)')

                    if (correcto == 'y'):
                        # Se puede continuar para modificar el dato
                        veri = False

                # Realizar la modificación del dato
                Mod_premiaciones_prem(premiacion, codigo_pelicula, fecha, reconocimiento)
                permanecer = False

            elif (op == '3'):
                #Modificar nombre del reconocimiento
                escritura_lenta("Por favor ingrese los datos que a continuación se le solicitaran\n")
                codigo_pelicula = input("Codigo de la pelicula: ")
                premiacion = input("Premiacion: ")
                fecha = ''
                verificador_fecha = True
                while (verificador_fecha):
                    fecha = input("Fecha de la premiacion (en formato YY-MM-DD): ")
                    if (Check_Date(fecha)):
                        #se puede continuar
                        verificador_fecha = False
                    else: 
                        escritura_lenta("Ingrese una fecha valida")

                #obtener nuevo dato
                veri = True 
                while(veri):
                    escritura_lenta("A continuacion escriba el nuevo nombre del reconocimiento")
                    reconocimiento = input("Reconocimiento: ")

                    escritura_lenta('\nEl dato ingresado fue: '+ str(reconocimiento))
                    escritura_lenta("¿Esta este correcto?")

                    correcto = input("(y/n)")

                    if (correcto == "y"):
                        # Se puede continuar para modificar el dato
                        veri = False

                #Realizar la modificacion del dato
                Mod_premiaciones_rec(reconocimiento, codigo_pelicula, premiacion, fecha)
                permanecer = False

            elif (op == '4'):
                #Modificar la fecha
                escritura_lenta("Por favor ingrese los datos que a continuación se le solicitaran\n")
                codigo_pelicula = input("Codigo e la pelicula: ")
                premiacion = input("Premiacion: ")
                reconocimiento = input("Reconocimiento: ")

                #obtener nuevo dato
                fecha = ''
                veri = True
                while (veri):
                    escritura_lenta("A continuacion escriba la nueva fecha")
                    verificador_fecha = True
                    while (verificador_fecha):
                        fecha = input("Fecha de la premiacion (en formato YY-MM-DD): ")
                        if (Check_Date(fecha)):
                            #se puede continuar
                            verificador_fecha = False
                        else: 
                            escritura_lenta("Ingrese una fecha valida")

                    escritura_lenta('\nEl dato ingresado fue: '+ str(fecha))
                    escritura_lenta("\n¿Esta este correcto?")

                    correcto = input("(y/n)")

                    if (correcto == 'y'):
                        # Se puede continuar para modificar el dato
                        veri = False

                # Realizar la modificación del dato
                Mod_premiaciones_fecha(fecha, codigo_pelicula, premiacion, reconocimiento)
                permanecer = False

            elif(op == '5'):
                #Eliminar una premiacion
                escritura_lenta("Por favor ingrese los datos que a continuación se le solicitaran")
                codigo_pelicula = input("Codigo de la pelicula: ")
                premiacion = input("Premiacion: ")
                reconocimiento = input("Reconocimiento: ")
                fecha = ''
                verificador_fecha = True
                while (verificador_fecha):
                    fecha = input("Fecha de la premiacion (en formato YY-MM-DD): ")
                    if (Check_Date(fecha)):
                        #se puede continuar
                        verificador_fecha = False
                    else: 
                        escritura_lenta("Ingrese una fecha valida")
                
                # Realizar la elminacion
                Delete_Premiacion(codigo_pelicula, premiacion, reconocimiento, fecha)
                permanecer = False

            elif (op == '6'):
                #salir
                permanecer = False

        except Exception as err:
            print(err)
            escritura_lenta('Error: Ingrese una respuesta valida')
            
def Mod_Correos():
    veri = True
    while (veri):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver cuentas')
            escritura_lenta('2) Modificar correos')
            escritura_lenta('3) Cancelar\n')
            op = int(input('Opcion: '))
            if (op == 1):
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        Get_Correos('cuenta', offset)
                        escritura_lenta('Pagina: '+str(pag))
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
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1
            elif (op == 2):
                #Modificar con correo
                permanecer2 = True
                while (permanecer2):
                    correo_u = input('Correo: ')
                    if (Get_Cuenta(correo_u)):
                        #existe
                            permanecer3 = True
                            while (permanecer3):
                                try:
                                    escritura_lenta('\nQue desea hacer?: ')
                                    escritura_lenta('1) Modificar Correo')
                                    escritura_lenta('2) Cancelar\n')
                                    nuevoDato =''
                                    dato_mod = int(input('Dato: '))
                                    
                                    if (dato_mod == 1):
                                        nuevoDato = input('Nuevo: ')
                                        '''
                                            Cambiar en la base de datos 
                                        '''
                                        Mod_CorreoU(nuevoDato, correo_u)
                                        print('Correo modificado exitosamente')
                                        permanecer3 = False
                                        permanecer2 = False
                                        
                                    elif(dato_mod == 2):
                                        escritura_lenta('[Cancelando...]\n')
                                        permanecer3 = False
                                        permanecer2 = False

                                    else:
                                        escritura_lenta('La opcion ingresada no es valida')  
                                except Exception as ex:
                                    escritura_lenta('Ingrese una opcion valida')
                                
                    else:
                        #no existe
                        escritura_lenta('El correo ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                veri = False
            
        except:
            print('Error, opcion invalida')

def Modificaciones_Admin(usuario):
    permanecer = True
    while (permanecer):
        try:
            print('\n-- Campos modificables --')
            print('1) Contenido (Peliculas)')
            print('2) Actores')
            print('3) Directores')
            print('4) Perfiles')
            print('5) Anunciantes')
            print('6) Anuncios')
            print('7) Premiaciones')
            print('8) Correos')
            print('9) Salir')
            print('Que desea modificar?\n')
            
            opc = int(input('Opcion: '))
            
            if (opc == 1):
                # Modificar peliculas
                ModContenido_pelicula()
                UploadBitacora(usuario)
            elif (opc == 2):
                # Modificar actores
                Mod_Actores()
                UploadBitacora(usuario)
            elif (opc == 3):
                # Modificar directores
                Mod_Directores()
                UploadBitacora(usuario)
            elif (opc == 4):
                # Modificar perfiles
                Mod_Perfiles()
                UploadBitacora(usuario)
            elif (opc == 5):
                # Modificar anunciantes
                ModAnunciantes()
                UploadBitacora(usuario)
            elif (opc == 6):
                # Modificar Anuncios
                ModAnuncios()
                UploadBitacora(usuario)
            elif (opc == 7):
                # Modificar premiaciones
                Mod_Premiaciones()
            elif (opc == 8):
                # Modificar correos
                Mod_Correos()
                UploadBitacora(usuario)
            elif (opc == 9):
                permanecer = False
            else:
                print('Opcion invalida')  

        except Exception as ex:
            escritura_lenta('Ingrese una respuesta valida\n')
            
def SimulacionOpera():
      
    ver = True
    while(ver):
        try:
            print('\nPara la simulacion de operaciones ingrese los siguientes datos: ')
            cant_visua = int(input('Cantidad de visualizaciones: '))
            ver1 = True
            fecha = ''
            while(ver1):
                fecha = input('\nFecha (YYYY-MM-DD): ')
                if (Check_Date(fecha)):
                    #se puede continuar
                    ver1 = False
                else: 
                    escritura_lenta('Ingrese una fecha valida')
            ver = False
                        
        except ValueError:
            print('Error, opcion invalida')  
    
    Generacion_visualizaciones(cant_visua, fecha)
    
    #Para realizar las simulaciones de todos los días por dos meses consecutivos (automatizando el trabajo)
    '''
    fechas = ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', 
              '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10', '2022-03-11', '2022-03-12', 
              '2022-03-13', '2022-03-14', '2022-03-15', '2022-03-16', '2022-03-17', '2022-03-18', 
              '2022-03-19', '2022-03-20', '2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', 
              '2022-03-25', '2022-03-26', '2022-03-27', '2022-03-28', '2022-03-29', '2022-03-30', 
              '2022-03-31', '2022-04-01', '2022-04-02', '2022-04-03', '2022-04-04', '2022-04-05', 
              '2022-04-06', '2022-04-07', '2022-04-08', '2022-04-09', '2022-04-10', '2022-04-11', 
              '2022-04-12', '2022-04-13', '2022-04-14', '2022-04-15', '2022-04-16', '2022-04-17', 
              '2022-04-18', '2022-04-19', '2022-04-20', '2022-04-21', '2022-04-22', '2022-04-23', 
              '2022-04-24', '2022-04-25', '2022-04-26', '2022-04-27', '2022-04-28', '2022-04-29', '2022-04-30']
    
    for fecha in fechas:
        Generacion_visualizaciones(750, fecha)'''
  
def SimulacionBusqueda(): 

    ver = True
    while (ver):
        try:
            print('¿Cuantas busquedas desea simular?')
            cant_busc = int(input('\nCant: '))

            Generar_busquedas(cant_busc)

            # Luego de que haya terminado
            cont = input('Se han terminado de ingresar los datos, ENTER para continuar')
            ver = False

        except ValueError:
            print('Ingrese un formato valido')

# Reportes proyecto 3
def Reportes_nuevos():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\nEscoja a continuacion el numero de reporte que desea obtener:\n')
            print('1) Top 5 de contenido visto en cada hora entre 9:00 a.m a 1:00 a.m para un mes dado')
            print('2) El  top  10  de  los  terminos  que  los  usuarios  buscan')
            print('3) El top 5 de los administradores que más modificaciones realizan en las cuentas de usuario para un rango de fechas dado')
            print('4) El  top  20  de  películas  que  comenzaron  a  verse  pero  que  llevan  más  de  20  días  sin finalizarse, para un rango de fechas dado.')
            print('5) CANCELAR')
            op = input('\nOp: ')

            if (op == '1'):
                # Reporte 1
                print('\n____________________________________________________________________________________')
                escritura_lenta('1) Top 5 de contenido visto en cada hora entre 9:00 a.m a 1:00 a.m para un mes dado')
                escritura_lenta('____________________________________________________________________________________\n')
                print('Ingrese los datos que a continuacion se le solicitan')

                mes = 0
                hora = ''

                revisar_mes = True
                while (revisar_mes):
                    try:
                        mes = int(input('Mes (1-12): '))
                        if (mes >= 1 and mes <= 12):
                            revisar_mes = False
                        else:
                            print('El mes ingresado se encuentra afuera del rango de meses')
                    except ValueError:
                        escritura_lenta('El valor ingresado no está en el formato solicitado')

                
                horas = ['9:00:00', '10:00:00', '11:00:00', 
                        '12:00:00', '13:00:00', '14:00:00', 
                        '15:00:00', '16:00:00', '17:00:00', 
                        '18:00:00', '19:00:00', '20:00:00', 
                        '21:00:00', '22:00:00', '23:00:00', 
                        '24:00:00']

                # Ejecución del procedimiento almacenado 
                for x in horas:
                    funcion_reporte_1(mes, x)

            
            elif (op == '2'):
                # Reporte 2
                print('\n____________________________________________________________________________________')
                escritura_lenta('1) El  top  10  de  los  terminos  que  los  usuarios  buscan\n')
                print('____________________________________________________________________________________\n')
                
                # Ejecución del procedimiento almacenado 
                funcion_reporte_2()
            
            elif (op == '3'):
                # Reporte 3
                print('\n____________________________________________________________________________________')
                escritura_lenta('3) El top 5 de los administradores que más modificaciones realizan en las cuentas de usuario para un rango de fechas dado')
                escritura_lenta('____________________________________________________________________________________\n')
                print('Ingrese los datos que a continuacion se le solicitan')

                fecha_i = ''
                fecha_f = ''

                revisar_fecha = True
                while (revisar_fecha):
                    fecha_i = input('Fecha inicio (YYY-MM-DD): ')
                    if(Check_Date(fecha_i)):
                        #se puede continuar
                        revisar_fecha = False

                revisar_fecha = True
                while (revisar_fecha):
                    fecha_f = input('Fecha fin (YYY-MM-DD): ')
                    if(Check_Date(fecha_f)):
                        #se puede continuar
                        revisar_fecha = False

                # Ejecución del procedimiento almacenado 
                funcion_reporte_3(fecha_i, fecha_f)

            elif (op == '4'):
                # Reporte 4
                print('\n_____________________________________________________________________________________________________________________________________________')
                escritura_lenta('4) El  top  20  de  películas  que  comenzaron  a  verse  pero  que  llevan  más  de  20  días  sin finalizarse, para un rango de fechas dado.')
                escritura_lenta('_____________________________________________________________________________________________________________________________________________\n')
                print('Ingrese los datos que a continuacion se le solicitan')

                fecha_i = ''

                revisar_fecha = True
                while (revisar_fecha):
                    fecha_i = input('Fecha (YYY-MM-DD): ')
                    if(Check_Date(fecha_i)):
                        #se puede continuar
                        revisar_fecha = False

                # Ejecución del procedimiento almacenado 
                funcion_reporte_4(fecha_i)

            elif (op == '5'):
                # Salir
                permanecer = False

            else:
                escritura_lenta('La opcion ingresada no es valida')

        except Exception as err:
            print(err)