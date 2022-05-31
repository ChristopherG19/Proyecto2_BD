'''
  Universidad del Valle de Guatemala
  Bases de datos 1
  Proyecto 2

  Integrantes:
    - Gabriel Vicente 20498
    - Maria Isabel Solano 20504
    - Christopher García 20541
'''

#librerías
from getpass import getpass
from logging import exception
from sympy import true
from Funciones import *
from ConnectionBD import *
from datetime import datetime

#Funciones utilizadas para suplir necesidades del usuario
def obtenerData2(entidad, offset):
    #Realizar query
    Conseguir_Data_2(entidad, offset)
    data = ''#Ingresar lista con toda la información
    return data

def ver_peliculas(Correo, PerfilActual):
    permanecer = True
    while (permanecer):
        try:
            #Ver contenido
            permanecer2 = True
            offset = 0
            pag = 1
            escritura_lenta("Catalogo de peliculas\n")
            while(permanecer2):
                if(offset >= 0):
                    obtenerData2('Peliculas', offset)
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
            
            permanecer3 = True
            while(permanecer3):
                escritura_lenta('\n¿Desea ver alguna pelicula?  ')

                op = input("(s/n) : ")

                if op == "s" or op == "S":
                    Fecha = datetime.date(datetime.now())
                    Hora = datetime.time(datetime.now())
                    siguiente = input('Ingrese codigo de la pelicula a ver: ')
                    if comprobar_pelicula(siguiente) != None:

                        open_link(comprobar_pelicula(siguiente))

                        escritura_lenta('\n ¿Terminaste de ver la pelicula?  ')
                        op2 = input("(s/n): ")
                        if op2 == "s" and Get_Sub(Correo) == "Gratis":
                            print("Registro en tablas")
                            
                            print("anuncios")

                            print("cantidad de anuncios: ", anuncios_cantidad(anuncios_tiempo(siguiente)))

                            print("cantidad de tiempo: ",anuncios_tiempo(siguiente))

                            anuncios_mostrar(anuncios_cantidad(anuncios_tiempo(siguiente)),anuncios_tiempo(siguiente), Correo)

                            #Contenido terminar, perfil reproducciones
                            Upload_PerfilReproducciones(Get_CodigoPerfil(Correo, PerfilActual),siguiente,Fecha,Hora)
                            Upload_ContenidoPerfil(Get_CodigoPerfil(Correo, PerfilActual), siguiente, minutos_consumidos, 'true',Fecha,Hora)
                            ContenidoFinalizadoRegistros(Get_CodigoPerfil(Correo, PerfilActual),siguiente)
                            
                        elif op2 == "s" and Get_Sub(Correo) != "Gratis":
                            print("Registro en tablas")
                            #Contenido terminado, perfil reproducciones
                            Upload_PerfilReproducciones(Get_CodigoPerfil(Correo, PerfilActual),siguiente,Fecha,Hora)
                            Upload_ContenidoPerfil(Get_CodigoPerfil(Correo, PerfilActual), siguiente, minutos_consumidos, 'true',Fecha,Hora)
                            ContenidoFinalizadoRegistros(Get_CodigoPerfil(Correo, PerfilActual),siguiente)
                        
                        else:
                            #Contenido sin terminar
                            escritura_lenta("¿En que minuto te quedaste? ")
                            minutos_consumidos = SolicitudNum2()
                            Upload_ContenidoPerfil(Get_CodigoPerfil(Correo, PerfilActual), siguiente, minutos_consumidos, 'false',Fecha,Hora)
                        
                        escritura_lenta('\n ¿Deseas agregarla a favoritos? ')
                        op3 = input("(s/n): ")

                        if op3 == "s":
                            print("agregar a favoritos")
                            Upload_FavPerfil(Get_CodigoPerfil(Correo, PerfilActual), siguiente, Correo,Fecha,Hora)
                            print()
                            permanecer3 = False
                        else:
                            permanecer3 = False
                    else:
                        escritura_lenta("Codigo de pelicula no encontrado\n")
                else:
                    permanecer3 = False
                    permanecer = False

        except Exception as ex:
            print(ex)
            escritura_lenta('Ingrese una respuesta válida')
            