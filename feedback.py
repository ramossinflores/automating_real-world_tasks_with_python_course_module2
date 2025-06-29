#! /usr/bin/env python3

import os
import requests

# Ruta del directorio donde están los comentarios
directory = "/data/feedback"
try:
    # Listado de todos los archivos con comentario
    files = os.listdir(directory)
    #  Lista vacía para almacenar los comentarios como diccionarios
    feedback_list = []
    # Se lee cada archivo
    for file in files:
        # para abrirlo, necesito la ruta asi que uno directorio más archivo
        file_path = os.path.join(directory,file)
        with open(file_path, "r") as f:
            # se crea una matriz llamada  lines donde cada línea es un elemento de dicha matriz
            lines = f.read().splitlines() # corta por línea, literal
            # ahora, se construye el diccionario:
            feedback = {
                "title": lines[0],
                "name": lines[1],
                "date": lines[2],
                "feedback": " ".join(lines[3:]) # uno con un espacio
            
            }
            # se añade a la lista de comentarios
            feedback_list.append(feedback)

            
            # lo sieguinte es envair cada comentario a la página de la coorporación:
            url = "http://127.0.0.1:80/feedback/"
            for feedback in feedback_list:
                # con ayuda de la librería request se transforma cada diccionario en JSON para hacerle post al servidor
                response = requests.post(url, json=feedback) 

                if response.status_code==201:
                    print("Feedback enviado correctamente")
                else:
                    print(" Error al enviar feedback")
                    print(response.text)
# Manejo de error no encontrar el directorio
except FileNotFoundError as e:
    print(f"El directorio {directory} no existe")
except Exception as e:
    print(f"No se puede continuar debido a la siguiente excepción: {e}")