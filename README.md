# Proyecto Wagtail

## Objetivos
Se finalizará la estructura iniciada:

gestión de páginas: padres/hijas
plantilla (navbar, sidebar, footer, etc)
El footer se podrá editar desde el CMS (snippet)
Añadir página de contacto.
Añadir noticias breves del sitio.

Tendrán un texto y una o más imágenes.
Se mostrarán las 5 últimas en la primera página de forma resumida y haciendo click la noticia completa.
Posibilidad de poner un aviso en la primera página.

Se mostrará debajo del menú principal si está activado
Completar blog de clase:

Habrá tres tipos de entradas de blog:
Genéricas
De películas. Se enlazará con una de las películas de nuestra sección de películas.
De viajes. Tendrá texto fotos y coordenadas. Se mostrará además del texto y las fotos un mapa con las coordenadas.
Otra a proponer.
Proponer organización y visualización.
Creación de una una nueva sección similar a la de las películas con en la que se instroducen datos en nuestro CMS a partir de una archivo json o csv.

Documentación de la sección.
Script para generar la sección.
Posibilidad de edición en un grupo del Admin justo debajo de las películas.
Creación de un tipo de páginas para la sección (index y de detalle)
Estas páginas podrán colgar de la principal (sólo el index)

## Instalacion
* Descarga de Proyecto:
```
git clone
```

* Creacion de entorno
```
python -m venv env
```

* Arranque entorno
```
source env/Script/activate
```

* Intalacion de proyecto
```
pip install -r requirements.txt
```

* Arranque del Proyecto
 ```
python manage.py runserver
```

## Acceso
* Navegador: 
 ```
localhost:8000
```
* Consola Admin:
 ```
localhost:8000/admin
```
* Usuario admin:alumno
* Pass admin:alumno

