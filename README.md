
# 📝🌐 Módulo 2 – Automatización con Python: Procesamiento de Archivos de Texto y Consumo de APIs

Este repo contiene el proyecto del Módulo 2 del curso **Google IT Automation with Python**, centrado en la automatización del procesamiento de archivos de texto y su integración con un servicio web mediante el uso del módulo `requests`.

## 🎯 Objetivo

Automatizar el procesamiento de archivos de texto que contienen comentarios de usuarios y enviarlos a una API web que los registra en una base de datos. Este ejercicio simula la automatización de una tarea administrativa común en empresas reales.

## ⁉️ ¿Qué se hace aquí?

* Leer múltiples archivos `.txt` desde un directorio específico.
* Extraer campos estructurados: título, nombre, fecha y contenido del comentario.
* Construir diccionarios a partir de los datos extraídos.
* Enviar los diccionarios a un endpoint HTTP utilizando el método `POST`.
* Verificar el código de estado de la respuesta y manejar errores.

## 📂 Estructura del repositorio

```
module02_requests_automating_real-world_tasks_with_python_course/
├── .gitignore
├── feedback.py               # Script principal para leer archivos y enviar los datos a la API
├── problem_statement.md      # Descripción del reto planteado por el módulo
├── README.md                 # Documentación del módulo
├── requirements.txt          # Dependencias requeridas 
```



## 🧪 Cómo probar este módulo

1. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

2. Asegúrate de que el servicio web de destino está activo y aceptando peticiones POST en el endpoint `/feedback/`.

3. Coloca los archivos `.txt` con retroalimentación en la carpeta `/data/feedback/`.

4. Ejecuta el script:

```bash
python feedback.py
```

5. Revisa los mensajes por consola. Si todo va bien, verás una confirmación por cada comentario enviado.



## 📌 Ejemplo de estructura de archivo `.txt`

```
Buena atención en el concesionario
Ana Torres
2023-06-18
Fueron muy amables durante todo el proceso de compra. Lo recomiendo.
```

Este contenido se convierte en un diccionario con el siguiente formato:

```python
{
  "title": "Buena atención en el concesionario",
  "name": "Ana Torres",
  "date": "2023-06-18",
  "feedback": "Fueron muy amables durante todo el proceso de compra. Lo recomiendo."
}
```



## 🔗 Recursos que me fueron útiles

* [Documentación oficial del módulo `requests`](https://docs.python-requests.org/en/latest/)
* [Cómo leer archivos línea por línea en Python – FreeCodeCamp](https://www.freecodecamp.org/news/how-to-read-files-in-python/)



## ✍ Autora

**Laura Ramos Granados**
Administradora de Sistemas Informáticos y Redes (ASIR)
Curso: Google IT Automation with Python – Módulo 2



## 📜 Licencia

Este proyecto se publica con fines educativos como parte del seguimiento al curso de Automatización con Python.
