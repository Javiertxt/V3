import requests
import schedule
import time
import dropbox
from datetime import datetime

# Configura tu token de acceso de Dropbox aquí
access_token = 'TU_TOKEN_DE_ACCESO'
dbx = dropbox.Dropbox(access_token)

# Función para descargar el archivo CSV y subirlo a Dropbox
def descargar_y_subir_csv():
url = 'https://cecobi.cecotec.cloud/ws/getstockfeedb2c.php?etiqueta=DROPES'
respuesta = requests.get(url)
nombre_archivo = f"archivo_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

# Guarda el archivo CSV temporalmente
with open(nombre_archivo, 'wb') as archivo:
archivo.write(respuesta.content)

# Sube el archivo a Dropbox
with open(nombre_archivo, 'rb') as archivo:
ruta_dropbox = f"/{nombre_archivo}"
dbx.files_upload(archivo.read(), ruta_dropbox, mute=True)

print(f"Archivo {nombre_archivo} descargado y subido a Dropbox")

# Programa la tarea para que se ejecute diariamente a las 08:00 AM hora de España
schedule.every().day.at("07:00").do(descargar_y_subir_csv)  # UTC Time

while True:
schedule.run_pending()
time.sleep(1)
