"""1. Desarrollar un programa para eliminar todos los comentarios de un programa escrito
en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
y que también se considera comentario a las cadenas de documentación
(docstrings)."""


def eliminar_comentarios(archivo, archivo_final):
    try:
        linea = archivo.readline()
        while linea:
            if linea.find("\"\"\"") == -1 and linea.find("\'\'\'") == -1:
                if linea.find("#") == -1:
                    archivo_final.write(linea)
                else:
                    pos = linea.find("#")
                    nueva_linea = linea[0:pos]
                    archivo_final.write(nueva_linea + "\n")
            else:
                pos_inicial = linea.find("\"\"\"")
                pos_final = linea.rfind("\"\"\"")
                
            linea = archivo.readline()
    except OSError as mensaje:
        print("No se puede leer el archivo", mensaje)
    finally:
        try:
            archivo.close()
            archivo_final.close()
        except NameError:
            pass


def abrir_archivo(): 
    try:
        archivo = open("programa_crudo.txt","rt")
        archivo_final = open("programa_procesado.txt","wt")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo", mensaje)
    return archivo, archivo_final


        








#------------Programa Principal------------
archivo, archivo_procesado = abrir_archivo()
eliminar_comentarios(archivo, archivo_procesado)


