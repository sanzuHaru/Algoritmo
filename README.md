# Servicio REST API de Predicción

Este proyecto proporciona un servicio REST API que simula el uso de un modelo de predicción utilizando Flask y Docker. El servicio permite realizar predicciones sobre datos proporcionados por el usuario y se encuentra configurado para ser ejecutado en contenedores Docker. Además, interactúa con una API de Spring Boot para enviar los resultados de las predicciones.

## Información del Servicio

- **Nombre del Servicio**: API de Predicción
- **Descripción**: Este servicio REST API permite a los usuarios enviar datos relacionados con municipios y recibir predicciones sobre la seguridad del lugar. Utiliza un modelo de predicción cargado desde un archivo y se integra con una API externa para enviar datos adicionales.
- **Tecnologías Utilizadas**: Flask, Docker, Pandas, NumPy, Joblib, Requests

## Requerimientos

- **Python 3.9 o superior**
- **Flask**
- **Pandas**
- **NumPy**
- **Joblib**
- **Requests**
- **Docker**

## Instalación

Para instalar y ejecutar este servicio, sigue estos pasos:

1. **Clona el repositorio**:

   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
## Crea un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows

## Instala las dependencias:

pip install -r requirements.txt
Configura Docker:

## Asegúrate de tener Docker instalado y en ejecución.

## Construye la imagen Docker:


docker build -t mi-flask-app .
Ejecuta el contenedor Docker:


## Copiar código
docker run -p 5000:5000 mi-flask-app

## Uso (Producción con Ejemplos de Cada Endpoint)
1. **Página Principal**
**Método: GET**
URL: http://localhost:5000/
**Descripción: Devuelve la página de inicio.**
2. **Página de Predicción**
## Método: POST

URL: http://localhost:5000/prediction

## Descripción: Envía datos del formulario para realizar una predicción.

## Parámetros del Cuerpo de la Solicitud (Form Data):

municipio (String): Nombre del municipio
habitantes (Número): Número de habitantes
accidentes (Número): Número de accidentes
muertos (Número): Número de muertos
heridos (Número): Número de heridos
Respuesta:

Código de Estado: 200 OK
Contenido: HTML que muestra el resultado de la predicción y una imagen relevante.
3. **Envío de Datos a la API de Spring Boot**
Método: POST

URL: http://localhost:8080/api/municipios/crear (URL configurada en el código, ajusta según tu configuración)

## Descripción: Envía los datos de predicción a la API de Spring Boot.

## Datos Enviados (JSON):

{
  "municipio": "Nombre del municipio",
  "habitantes": 12345,
  "accidentes": 12,
  "muertos": 3,
  "heridos": 5,
  "peligroso": true
}
Respuesta:

Código de Estado: 200 OK o el código correspondiente a la respuesta de la API de Spring Boot.
Uso (Desarrollo)
Para desarrollar y probar el servicio localmente:

## Inicia la aplicación Flask en modo desarrollo:


python app.py
La aplicación se ejecutará en http://localhost:5000.

## Realiza cambios en el código y actualiza el contenedor:

## Si realizas cambios en el código, puedes reconstruir la imagen Docker y reiniciar el contenedor para ver los cambios.

docker build -t mi-flask-app .
docker run -p 5000:5000 mi-flask-app
Prueba los endpoints utilizando herramientas como curl, Postman, o simplemente navegando en tu navegador.

## Ejemplo de curl para la página de predicción:

bash
curl -X POST http://localhost:5000/prediction -F "municipio=Nombre" -F "habitantes=12345" -F "accidentes=12" -F "muertos=3" -F "heridos=5"
Contribuciones
## Si deseas contribuir a este proyecto, por favor sigue las prácticas de bifurcación y envío de solicitudes de extracción. Asegúrate de probar tus cambios antes de enviarlos.

## Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
