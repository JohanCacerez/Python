'''
Docstring for Concurrencia.DownloadURL
Descarga concurrente (I/O bound simple)

Implementa una función que recibe una lista de URLs y las descarga en paralelo usando:
a) threading.Thread
b) ThreadPoolExecutor
c) asyncio + aiohttp
'''

# Generamos una lista con los url a descargar
urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.reddit.com',
    'https://www.wikipedia.org',
    'https://www.medium.com',
    'https://www.linkedin.com',]

'''
import threading
import requests

#En escenarios reales es mejor proteger la escritura en la lista compartida
lock = threading.Lock()

#Creamos una lista donde se almacenaran los objetos Thread
threads = []

# Creamos una lista donde se almacenaran los resultados
results = []


#Funcion para guaredar el resultado de la descarga
def worker(url):
    content = fetch_url(url)
    with lock:
        results.append((url, content))

#Funcion para obtener el contenido de la url
def fetch_url(url):
    response = requests.get(url)
    return response.text

#Ciclo para crear y arrancar los hilos
for url in urls:
    print(f"Iniciando descarga de {url} con threading.Thread")
    thread = threading.Thread(target=worker, args=(url,))
    threads.append(thread)
    thread.start()

#Ciclo para esperar a que terminen los hilos
for thread in threads:
    thread.join()   
print("Descarga con threading.Thread finalizada.")

print("Descargados: ", len(results))
'''

'''
Un Pool nos sirve para poder manejar de mejor manera multiples hilos sin tener que crearlos y manejarlos, ya que estos los crea
de manera autoamtica en el Pool
'''
'''
from concurrent.futures import ThreadPoolExecutor
import requests

results = []

def worker(url):
    content = fetch_url(url)
    results.append((url, content))

def fetch_url(url):
    response = requests.get(url)
    return response.text
with ThreadPoolExecutor(max_workers=len(urls)) as executor:
    for url in urls:
        print(f"Iniciando descarga de {url} con Pool") 
        executor.submit(worker, url)

print("Descarga con Pool finalizada.")

print("Descargados: ", len(results))
'''
