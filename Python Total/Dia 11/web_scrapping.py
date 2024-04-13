import bs4
import requests

resultado = requests.get(
    "https://escueladirecta-blog.blogspot.com/2022/10/por-que-se-utiliza-python-en-ciencia-de.html")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')  # donde nos pide 2 argumentos, el primero sera el texto de
# la web y el tipo de motor para hacer el parsing

#print(sopa.select("title")[0].getText()) # el metodo .getText(), lo que dara es el contenido de la etiqueta por la cual
# se desea buscar

#  en esta parte del codigo extraemos los h3 de la pagina en resultado, en forma de texto puro que se encuentra dentro
# del div class="widget PopularPosts"
columna_lateral = sopa.select('.PopularPosts h3')
for h3 in columna_lateral:
    print(h3.getText())

''' todo el codigo siguiente es para saber como descargar archivos'''
resultado2 = requests.get("https://www.escueladirecta.com/courses/")

sopa2 = bs4.BeautifulSoup(resultado2.text, 'lxml')

imagen = sopa2.select(".course-box-image")[0]['src']
print("\nImagen: ")
print(imagen)

imagen_curso = requests.get(imagen)

f = open('mi_imagen.JPEG', 'wb') # write binary
f.write(imagen_curso.content) # donde el .content revelara el contenido en codigo binario y al escribir un archivo en
# codigo binario lo que hara es ejecutar el codigo y descargar dicha cosa que queramos, en este caso una imagen
f.close()

